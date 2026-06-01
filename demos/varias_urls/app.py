
import web

urls = (
    '/', 'Index',
    '/Clientes', 'Clientes',
    '/Usuarios','Usuarios',
)
app = web.application(urls, globals())
render = web.template.render('templates/')

class Index:
    def GET(self):
        return str(render.index())
   

class Clientes:
    def GET(self):
        return str(render.clientes())
class Usuario:
    def GET(self):
        return str(render.usuario())   
    
if __name__ == "__main__":
    app.run()