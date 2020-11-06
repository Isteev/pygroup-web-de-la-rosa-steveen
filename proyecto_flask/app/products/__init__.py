from flask import Flask
from flask import Blueprint
app = Flask (__name__)

product = Blueprint('auth', __name__, url_prefix='/product')

@product.route('/<name>')
def product_info(name):
    return "Bienvenido {}".format(name)