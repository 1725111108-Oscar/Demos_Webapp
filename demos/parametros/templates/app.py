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
        titulo = "Titulo desde python"
        descripcion = """Lorem ipsum dolor sit amet consectetur adipiscing elit curabitur parturient, velit ut sapien nunc vehicula ante vulputate cursus, platea fringilla dui scelerisque vivamus enim purus ac. Tempor augue torquent egestas dis taciti, habitant ultrices platea ullamcorper nunc, ornare accumsan tincidunt rutrum. Lobortis sagittis platea porta habitasse enim primis rhoncus fusce, ullamcorper cum feugiat risus ut faucibus.
        A torquent pulvinar augue accumsan nisl vitae morbi at purus, cursus aliquam ultricies enim imperdiet dignissim semper cubilia mattis, mollis tellus ante litora magna varius placerat convallis. Duis mi iaculis eget ridiculus nisl sed porttitor mus libero, sollicitudin pretium nostra vivamus tristique euismod facilisis ante, rhoncus maecenas ultricies urna ut suspendisse potenti scelerisque. Suspendisse et eleifend nostra iaculis nisi tempus porttitor nascetur, quisque potenti odio turpis penatibus varius tempor quam libero, erat platea egestas a mattis dignissim duis."""
        return str(render.parametros(titulo,descripcion))