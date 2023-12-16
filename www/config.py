'''
配置文件
'''

from typing import Any
import config_default

class Dict(dict):
    '''
    Simple dict but support access as x.y style.
    '''
    def __init__(self,names=(),values=(),**kw):
        super(Dict,self).__init__(**kw)
        for k,v in zip(names,values):
            self[k]=v
            
    def __getattr__(self,key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)
     
    def __setattr__(self,key,value):
        self[key]=value

#将config_default与config_override合并
def merge(defaults,override):
    r={}
    for k,v in defaults.items():
        if k in override:
            if isinstance(v,dict):
                r[k]=merge(v,override[k])
            else:
                r[k]=override[k]
        else:
            r[k]=v
    return r

#将dict变为自己声明的Dict
def toDict(d):
    D=Dict()
    for k,v in d.items():
        D[k]=toDict(v) if isinstance(v,dict)  else v
    return D

#合并
configs=config_default.configs
try:
    import config_override
    configs=merge(configs,config_override.configs)
except ImportError:
    pass

#变为Dict
configs=toDict(configs)