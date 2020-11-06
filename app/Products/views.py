from flask import Blueprint, Response

products=Blueprint('products', __name__, url_prefix='/products')



@products.route('/<string:name>', methods=['GET'])
def get_products(name):
    txt="Felicitaciones! Trabajo Exitoso {}"
    stat=200
    if(name=="pygroup"):
        txt="ERROR! No se puede usar el nombre {}"
        stat=400
    return Response(("<h1 align=center>"+txt+"</h1>").format(name), status=stat)
    
"""
Método render_template()

Es utilizado para desplegar una plantilla HTML para principalmente enlazar los datos estáticos
incluidos con HTML y los dinámicos implementados con python, permitiendo modularizar todo el contenido de HTML
en un solo archivo, sin necesidad de que este se encuentre mezclado con código de otras funcionalidades.

Utiliza varios parámetros como lo son:

- Nombre de la plantilla HTML:  el primer parámetro que utiliza esta función es para indicar la ruta del archivo de extensión
                                .html el cual será utilizado por la aplicación.

- Variable a pasar a la plantilla:  el segundo parámetro es para indicar los datos dinámicos que serán renderizados con la
                                    plantilla, relacionados con una o más variables.

"""