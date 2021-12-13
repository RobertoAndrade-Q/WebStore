from webpersonal import db

class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100))
    description = db.Column(db.Text)
    price = db.Column(db.Float)
    stock = db.Column(db.String(5))

    def __init__(self, title, description, price, stock):
        self.title = title
        self.description = description
        self.price = price
        self.stock = stock

    def __repr__(self):
        return f'Product: {self.title}'

        