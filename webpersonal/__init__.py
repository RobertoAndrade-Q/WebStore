# Importamos el framework Flask y la base de datos utilizada
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Definimos la app 
app = Flask(__name__)

# Configuración del modo de la app
app.config.from_object('config.DevelopmentConfig')

# Declaramos una variable (db) que contendrá el SQLAlchemy
db = SQLAlchemy(app)

# Importamos las vistas de los diferentes módulos 
from webpersonal.views import base
from webpersonal.customer.views import customer
from webpersonal.product.views import product
from webpersonal.sale.views import sale

# Tenemos que registrar en este punto los blueprints para poder usarlos en nuestro proyecto
app.register_blueprint(base)
app.register_blueprint(customer)
app.register_blueprint(product)
app.register_blueprint(sale)


# Ejecutar todas las consultas
db.create_all()