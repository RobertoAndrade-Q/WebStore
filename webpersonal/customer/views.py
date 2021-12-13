from flask import render_template, Blueprint, request, redirect, url_for
# from webpersonal.project.models import proyectos
from webpersonal.customer.models import Customer

from webpersonal import db

customer = Blueprint('customer', __name__)

@customer.route('/customer/')
@customer.route('/customer/index')
def index():
    customers = Customer.query.all()
    db.session.commit

    return render_template('customer/index.html', customers = customers)

@customer.route('/customer/create')
def create():
    return render_template('customer/create.html')

@customer.route('/customer/insert', methods=['POST'])
def insert():
    name = request.form.get('name')
    phone = request.form.get('phone')
    city = request.form.get('city')

    customer = Customer(name, phone, city)

    db.session.add(customer)
    db.session.commit()

    return redirect(url_for('customer.index'))

@customer.route('/project/edit/<int:id>')
def edit(id):
    customer = Customer.query.get_or_404(id)
    return render_template('customer/edit.html', customer=customer)

@customer.route('/customer/update/<int:id>', methods=['POST'])
def update(id):
    customer = Customer.query.get_or_404(id)
    customer.name = request.form.get('name')
    customer.phone = request.form.get('phone')
    customer.city = request.form.get('city')

    db.session.add(customer)
    db.session.commit()

    return redirect(url_for('customer.index'))

@customer.route('/customer/delete/<int:id>')
def delete(id):
    customer = Customer.query.get_or_404(id)
    db.session.delete(customer)
    db.session.commit()

    return redirect(url_for('customer.index'))


