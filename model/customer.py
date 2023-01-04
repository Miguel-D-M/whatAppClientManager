from config.db import db

class Customer(db.Model):
    id : str = db.Column(db.String, primary_key=True)
    verified: bool = db.Column(db.Boolean)
    orders = db.relationship('Order', backref='customer', lazy=True)
    messages = db.relationship('Message', backref='customer', lazy=True)

    def __repr__(self):
        return f'<Order {self.id} for {self.sender}>'