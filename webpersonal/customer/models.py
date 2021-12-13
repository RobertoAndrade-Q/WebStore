from webpersonal import db

class Customer(db.Model):
    __tablename__ = 'customers'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    phone = db.Column(db.String(15))
    city = db.Column(db.String(50))
    

    def __init__(self, name, phone, city):
        self.name = name
        self.phone = phone
        self.city = city

    def __repr__(self):
        return f'{self.name}, {self.phone}'

