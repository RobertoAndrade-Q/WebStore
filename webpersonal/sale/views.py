from flask import render_template, Blueprint, request, redirect, url_for
from webpersonal.customer.models import Customer
from webpersonal.product.models import Product

from webpersonal.sale.models import Sale

from webpersonal import db

sale = Blueprint('sale', __name__)


@sale.route('/sale/')
@sale.route('/sale/index')
def index():
    sales = Sale.query.all()
    db.session.commit()
    productos = Product.query.all()
    db.session.commit()
    clientes = Customer.query.all()
    db.session.commit()
    return render_template('sale/index.html', sales = sales, productos = productos, clientes = clientes)

@sale.route('/sale/create')
def create():
    sales = Sale.query.all()
    db.session.commit()
    productos = Product.query.all()
    db.session.commit()
    clientes = Customer.query.all()
    db.session.commit()
    return render_template('sale/create.html', sales=sales, productos=productos, clientes = clientes)

@sale.route('/sale/insert', methods=['POST'])
def insert():
    date = request.form.get('date')
    total = request.form.get('total')
    metodo_pago = request.form.get('metodo_pago')
    product_id = request.form.get('product_id')
    customer_id = request.form.get('customer_id')

    sale = Sale(date, total, metodo_pago, product_id, customer_id)

    db.session.add(sale)
    db.session.commit()

    return redirect(url_for('sale.index'))

@sale.route('/sale/edit/<int:id>')
def edit(id):
    sale = Sale.query.get_or_404(id)
    productos = Product.query.all()
    db.session.commit()
    clientes = Customer.query.all()
    db.session.commit()
    
    return render_template('sale/edit.html', sale=sale, productos=productos, clientes=clientes)

@sale.route('/sale/update/<int:id>', methods=['POST'])
def update(id):
    sale = Sale.query.get_or_404(id)
    sale.date = request.form.get('date')
    sale.total = request.form.get('total')
    sale.metodo_pago = request.form.get('metodo_pago')
    sale.product_id = request.form.get('product_id')
    sale.customer_id = request.form.get('customer_id')

    db.session.add(sale)
    db.session.commit()

    return redirect(url_for('sale.index'))

@sale.route('/sale/delete/<int:id>')
def delete(id):
    sale = Sale.query.get_or_404(id)
    db.session.delete(sale)
    db.session.commit()

    return redirect(url_for('sale.index'))


@sale.route('/home/')
def currency():
    sales = Sale.query.all()
    db.session.commit

    # Método para ganancias obtenidas(total)
    suma = 0

    for sale in sales:
        suma += sale.total

    # Método para el total de ventas
    total_ventas = 0
    for sale in sales:
        total_ventas += 1

    return render_template('home.html', sales=sales, suma=suma, total_ventas = total_ventas)

