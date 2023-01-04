from config.db import db
from sqlalchemy.sql import func
class Order(db.Model):
    id : int = db.Column(db.Integer, primary_key=True)
    customer_id: str = db.Column(db.String,db.ForeignKey('customer.id'),nullable=False)
    create_at : db.Column(db.DateTime(timezone=True),
                           server_default=func.now())

    def __repr__(self):
        return f'<Order {self.id} for {self.sender}>'