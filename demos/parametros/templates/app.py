import web
##permite saber la direccion de la pagina
urls = (
    '/', 'Index',
    '/parametros', 'Parametros',
)
##hace que todoo funcione 
app = web.application(urls, globals())
render = web.template.render('templates')

class Index:
    def GET(self):
        return str(render.index())