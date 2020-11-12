from flask import Blueprint, Response, request
from http import HTTPStatus

from proyecto_flask.app.products.models import get_all_categories, create_new_category, \
    get_all_products, get_product_by_id

products = Blueprint('product', __name__, url_prefix='/products')

EMPTY_SHELVE_TEXT = "Empty shelve!"
PRODUCTS_TITLE = "<h1> Products </h1>"
DUMMY_TEXT = "Dummy method to show how Response works"
RESPONSE_BODY = {
    "message": "",
    "data": [],
    "errors": [],
    "metadata": []
}

@products.route('/<string:name>', methods=['GET'])
def index(name):
    if name == "pygroup":
        return "<h1>ERROR! No se puede usar el nombre pygroup</h1>", 400
    else:
        return "<h1>Felicitaciones! Trabajo exitoso {}</h1>".format(name), 200


@products.route('/categories')
def get_categories():
    categories = get_all_categories()
    status_code = HTTPStatus.OK

    if categories:
        RESPONSE_BODY["message"] = "OK. Categories List"
        RESPONSE_BODY["data"] = categories
    else:
        RESPONSE_BODY["message"] = "OK. No categories found"
        RESPONSE_BODY["data"] = categories
        status_code = HTTPStatus.NOT_FOUND

    return RESPONSE_BODY, status_code


@products.route('/add-category', methods=['POST'])
def create_category():
    RESPONSE_BODY["message"] = "Method not allowed"
    status_code = HTTPStatus.METHOD_NOT_ALLOWED
    if request.method == "POST":
        data = request.json
        category = create_new_category(data["name"])
        RESPONSE_BODY["message"] = "OK. Category created!"
        RESPONSE_BODY["data"] = category
        status_code = HTTPStatus.CREATED

    return RESPONSE_BODY, status_code


@products.route('/')
def get_products():
    products_obj = get_all_products()

    RESPONSE_BODY["data"] = products_obj
    RESPONSE_BODY["message"] = "Products list"

    return RESPONSE_BODY, 200


@products.route('/product/<int:id>')
def get_product(id):
    product = get_product_by_id(id)

    RESPONSE_BODY["data"] = product
    return RESPONSE_BODY, 200


@products.route('/product-stock/<int:id>')
def get_product_stock(product_id):
    pass


@products.route('/need-restock')
def get_products_that_need_restock():
    pass


@products.route('/register-product-stock/<int:id>', methods=['PUT', 'POST'])
def register_product_refund_in_stock():
    pass

"""Se utiliza para renderizar plantillas, 
    es decir despues de una peticion se puede lanzar una pagina o alguna plantilla rapidamente,
    creeria que puede servir para cuando no existe una pagina, 
    entonces se crearia una plantilla explicando que dicha pagina no existe,
    mas alla de solo mostrar un error. para ultilizar render_template() se debe importar de la siguiente manera 

    from flask import render_template.     ejemplo 
    Aqui -> Definemos el route
    @app.route("/")
    Aqui -> Un segundo route con el nombre del parametro
    @app.route('/<nombre>')
    def render(nombre=None): # Inicializamos "nombre"
    Aqui -> Retornamos la plantilla "index.html" y Le pasamo el parametro a el método render_template
     return render_template("index.html", nombre=nombre)
 """