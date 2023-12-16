
import jinja2,aiohttp_jinja2
from aiohttp import web
from models import User
def create_web():
    #路由器装饰
    routes=web.RouteTableDef()

    #创建web app
    app=web.Application()

    #设置模板路径
    aiohttp_jinja2.setup(
        app,
        loader=jinja2.FileSystemLoader(r'D:\Web_Python\wesome-python3-webapp\www\templates'),
        enable_async=True
    )

    #异步查询数据库函数
    async def get_users_all():
        return await User.findAll()

    #异步模板渲染函数
    async def rander_template(request,template_name,context):
        context['request']=request
        template=aiohttp_jinja2.get_env(request.app).get_template(template_name)
        return web.Response(
            text=await template.render_async(context),
            content_type='text/html'
        )
    
    #响应
    @routes.get('/')
    async def index(request):
        users_all=await get_users_all()
        return await rander_template(request,'test.html',{'users':users_all})

    #添加路由器
    app.add_routes(routes)
    return app
if __name__=='__main__':
    app=create_web()
    web.run_app(app, host='127.0.0.1', port=5000)