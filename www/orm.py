'''
Object-Relational Mapping:用面向对象的方式来操作数据库
'''

import logging
from typing import Any;logging.basicConfig(level=logging.INFO)

import aiomysql
import asyncio
from app import sj
#自定义log
def log(sql,args=()):
    logging.info('SQL:%s'%sql)
#创建连接池
async def create_pool(**kw):
    logging.info('connect mysql')
    __pool=await aiomysql.create_pool(
        host=kw.get('host','localhost'),
        port=kw.get('port',3306),
        user=kw['user'],
        password=kw['password'],
        db=kw['db'],
        autocommit=kw.get('autocommit',True),
        charset=kw.get('charset','utf8mb4'),
        maxsize=kw.get('maxsize',10),
        minsize=kw.get('minsize',1),
    )
    return __pool

#select
async def select(sql,args,size=None):
    log(sql,args)
    __pool=await create_pool(**sj)
    async with __pool.acquire() as conn:
        async with conn.cursor(aiomysql.DictCursor) as cur:
            await cur.execute(sql.replace('?','%s'),args or ())
            if size:
                rs=await cur.fetchmany(size)
            else:
                rs=await cur.fetchall()
        logging.info('rows returned: %s' % len(rs))
        return rs   

#insert,update,delate
async def in_up_de(sql,args,autocommit=True):
    log(sql)
    __pool=await create_pool(**sj)
    async with __pool.get() as conn:
        if not autocommit:
            await conn.begin()
        try:
            async with conn.cursor(aiomysql.DictCursor) as cur: 
                await cur.execute(sql.replace('?','%s'),args or ())
                affected=await cur.rowcount
            if not autocommit:
                await conn.commit()
        except BaseException as e:
            if not autocommit:
                await conn.rollback()
            raise
        return affected

#储存字段名和类型(列)
class Field(object):
    
    def __init__(self,name,column_type,primary_key,default):
        self.name=name
        self.column_type=column_type
        self.primary_key=primary_key
        self.default=default
        
    def __str__(self):
        return '<%s %s:%s>'%(self.__class__.__name__,self.name,self.column_type)

#column_type为String
class StringField(Field):
    
    def __init__(self,name=None,column_type='varchar(100)',primary_key=False,default=None):
        super().__init__(name,column_type,primary_key,default)

#column_type为boolean
class BooleanField(Field):
    
    def __init__(self, name=None,default=False):
        super().__init__(name,'boolean',False, default)
        
#column_type为intteger
class Intteger(Field):
    
    def __init__(self, name=None,primary_key=False, default=0):
        super().__init__(name,'bigint', primary_key, default)
        
#column_type为float
class FloatField(Field):
    
    def __init__(self, name=None,primary_key=False,default=0.0):
        super().__init__(name, 'real', primary_key,default)
        
#column_type为text
class TextField(Field):
    
    def __init__(self, name=None, default=None):
        super().__init__(name, 'text',False, default)
        
#用于返回文号个数
def the_num(num):
    l=[]
    for i in range(num):
        l.append('?')
    return ','.join(l)

#元类用于创建Model类
class ModelMetaclass(type):
    
    def __new__(cls,name,bases,attrs):
        if name=='Model':
            return type.__new__(cls,name,bases,attrs)
        tablename=(attrs.get('__table__',None) or name)
        logging.info('found tablename is %s'%tablename)
        mappings=dict()
        fields=[]
        primary=None
        for k,v in attrs.items():
            if isinstance(v,Field):
                logging.info('mappings found %s ==> %s'%(k,v))
                mappings[k]=v
                if v.primary_key:#查找主键
                    if primary:#已有主键
                        raise BaseException('Duplicate primary key for field: %s '% k)
                    primary=k
                else:
                    fields.append(k)#处主键以外的
        if not primary:
            raise BaseException('not found paimary_key')
        for k in list(attrs.keys()):
            attrs.pop(k)#清空attrs
        escaped_fields=list(map(lambda f:'%s'%f,fields))#让字符适用于SQL
        attrs['__mappings__']=mappings
        attrs['__fields__']=fields
        attrs['__primary__']=primary
        attrs['__tablename__']=tablename
        attrs['__select__']='select %s,%s from %s'%(primary,','.join(escaped_fields),tablename)
        attrs['__update__']='update %s set %s where %s=?'%(tablename,','.join(map(lambda f:'%s=?'%(mappings.get(f).name or f),fields)),primary)
        attrs['__insert__']='insert into %s (%s,%s) values (%s)'%(tablename,','.join(escaped_fields),primary,the_num(len(escaped_fields)+1))
        attrs['__delete__']='delete from %s where %s=?'%(tablename,primary)
        return type.__new__(cls,name,bases,attrs)

#Model类，用ModelMateclass创建
class Model(dict,metaclass=ModelMetaclass):

    def __init(self,**kw):
        super(Model,self).__init__(**kw)
    
    #创建快捷的方式存储数据
    def __getattr__(self,key):
        try:   
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)
    
    def __setattr__(self,key,value):
        self[key]=value

    #获取数据
    def getValue(self,key):
        return getattr(self,key,None)

    def getValueORdefault(self,key):
        value=getattr(self,key,None)
        if value is None:
           field=self.__mappings__[key]
           if field.default is not None:
               value=field.default() if callable(field.default) else field.default
               logging.debug('using default value for %s: %s' % (key, str(value)))
               setattr(self,key,value)
        return value
           
    #select方法的实现
    @classmethod
    async def findAll(cls,where=None,args=None,**kw):#类方法
        # find objects by where clause. 
        sql=[cls.__select__]
        #where条件语句
        if where:
            sql.append('where')
            sql.append(where)
        #参数
        if args is None:
            args=[]
        #排序方式
        orderby=kw.get('orderby',None)
        if orderby is not None:
            sql.append('order by')
            sql.append(orderby)
        #限制条件
        limit=kw.get('limit',None)
        if limit is not None:
            sql.append('limit')
            if isinstance(limit,int):
                sql.append('?')
                args.append(limit)
            elif isinstance(limit,tuple) and len(limit)==2:
                sql.append('?, ?')
                args.extend(limit)
            else:
                raise ValueError('the %s is error'%str(limit))
        #调用select方法
        rs=await select(' '.join(sql),args)
        #返回结果
        return [cls(**r) for r in rs]
    
    #select方法的实现(只返回指定的列，且为一行)
    @classmethod
    async def findNumber(cls,selectField,where=None,args=None):
        logging.info(' find number by select and where.')
        sql=['select %s _num_ from %s'%(selectField,cls.__tablename__)]#_num_为别名
        if where:
            sql.append('where')
            sql.append(where)
        rs= await select(' '.join(sql),args,1)
        if len(rs)==0:
            return None
        return rs[0]['_num_']
    
    #select方法的实现(之返回指定主键值的一行，且为一行)
    @classmethod
    async def find(cls,pk):#pk要查找的行的主键的数值
        logging.info(' find object by primary key. ')
        rs= await select('%s where %s=?'%(cls.__select__,cls.__primary__),[pk],1)
        if len(rs)==0:
            return None
        return cls(**rs[0])
    
    #保存数据
    @classmethod
    async def save(self):
        args=list(map(self.getValueORdefault,self.__fields__))#通过dict获得列的数据
        args.append(self.getValueORdefault(self.__primary__))#通过dict获取主键的值
        rows=await in_up_de(self.__insert__,args)
        if rows!=1:
            logging.warn('failed to insert record: affected rows: %s' % rows)
    
    #更新数据
    @classmethod
    async def update(self):
        args=list(map(self.getValue,self.__fields__))#通过dict获得列的数据
        args.append(self.getValue(self.__primary__))#通过dict获取主键的值
        rows=await in_up_de(self.__update__,args)
        if rows!=1:
            logging.warn('failed to update by primary key: affected rows: %s' % rows)
        
    #删除数据
    @classmethod
    async def remove(self):
        args=[self.getValue(self.__primary__)]#通过dict获取主键的值
        rows=await in_up_de(self.__delete__,args)
        if rows!=1:
            logging.warn('failed to remove by primary key: affected rows: %s' % rows)