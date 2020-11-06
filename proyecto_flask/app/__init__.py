from flask import Flask
from proyecto_flask.app.products.views import product


app = Flask(__name__)
app.register_blueprint(product)

if __name__ == "__main__":
    app.run(debug=True)
