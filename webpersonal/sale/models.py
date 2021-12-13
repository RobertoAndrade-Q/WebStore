from sqlalchemy.orm import backref
from webpersonal import db

class Sale(db.Model):
    __tablename__ = 'sales'
    id = db.Column(db.Integer, primary_key = True)
    date = db.Column(db.Date)
    total = db.Column(db.Float)
    metodo_pago = db.Column(db.String(55))
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
    producto = db.relationship('Product', backref=db.backref('productos', lazy=True))
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'))
    cliente = db.relationship('Customer', backref=db.backref('clientes', lazy=True))
    

    def __init__(self, date, total, metodo_pago, product_id, customer_id):
        self.date = date
        self.total = total
        self.metodo_pago = metodo_pago
        self.product_id = product_id
        self.customer_id = customer_id
        

    def __repr__(self):
        return f'{self.total}, {self.date}'

        
    