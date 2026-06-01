import web

urls = (
    '/', 'Index'
    '/Clientes', 'Clientes'
    )
app = web.application(urls, globals())

class Index:
    def GET(self):
        return 'Hola mundo desde web.py'
    
class Clientes:
    def GET(SELF):
        return 'Esta es la pagina de Clientes'
    
if __name__ == "__main__":
    app.run()
