# from webpersonal import app
from flask import render_template, Blueprint

from webpersonal.customer.models import Customer
from webpersonal.sale.models import Sale
from webpersonal.product.models import Product

# Importamos db para poder usar la base de datos 
from webpersonal import db

# Definimos nuestros blueprints
customer = Blueprint('customer', __name__)
sale = Blueprint('sale', __name__)
product = Blueprint('product', __name__)


base = Blueprint('base', __name__)

@base.route('/') # Ruta de la función
@base.route('/home') #Ruta de la función 
def home(): # Función principal
    customers = Customer.query.all()
    db.session.commit
    sales = Sale.query.all()
    db.session.commit
    products = Product.query.all()
    db.session.commit

    # Método para ganancias obtenidas(total)
    suma_ganancias = 0

    for sale in sales:
        suma_ganancias += sale.total

    # Método para el total de ventas
    total_ventas = 0
    for sale in sales:
        total_ventas += 1

    # Método para el número de clientes
    total_clientes = 0
    for customer in customers:
        total_clientes += 1

    # Método para el número de productos
    total_productos = 0
    for product in products:
        total_productos += 1

    return render_template('home.html', customers = customers, suma_ganancias = suma_ganancias, total_ventas=total_ventas, total_clientes=total_clientes, total_productos=total_productos)



