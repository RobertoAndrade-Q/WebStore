from flask import render_template, Blueprint, request, redirect, url_for

from webpersonal.product.models import Product

from webpersonal import db

product = Blueprint('product', __name__)

@product.route('/product/')
@product.route('/product/index')
def index():
    products = Product.query.all()
    db.session.commit
    return render_template('product/index.html', products = products)

@product.route('/product/create')
def create():
    return render_template('product/create.html')

@product.route('/product/insert', methods=['POST'])
def insert():
    title = request.form.get('title')
    description = request.form.get('description')
    price = request.form.get('price')
    stock = request.form.get('stock')

    product = Product(title, description, price, stock)

    db.session.add(product)
    db.session.commit()

    return redirect(url_for('product.index'))

@product.route('/product/edit/<int:id>')
def edit(id):
    product = Product.query.get_or_404(id)
    return render_template('product/edit.html', product=product)

@product.route('/product/update/<int:id>', methods=['POST'])
def update(id):
    product = Product.query.get_or_404(id)
    product.title = request.form.get('title')
    product.description = request.form.get('description')
    product.price = request.form.get('price')
    product.stock = request.form.get('stock')

    db.session.add(product)
    db.session.commit()

    return redirect(url_for('product.index'))

@product.route('/product/delete/<int:id>')
def delete(id):
    product = Product.query.get_or_404(id)
    db.session.delete(product)
    db.session.commit()

    return redirect(url_for('product.index'))


@product.route('/product/view/')
def store():
    products = Product.query.all()
    db.session.commit
    return render_template('product/see.html', products = products)