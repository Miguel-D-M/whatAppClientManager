from config.db import db
from sqlalchemy.sql import func
class Order_Line(db.Model):
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'),primary_key=True)
    id : int = db.Column(db.Integer, primary_key=True)
    item_id: int = db.Column(db.String,db.ForeignKey('item.id'),nullable=False)
    quantity : db.Column(db.DateTime(timezone=True),
                           server_default=func.now())

    def __repr__(self):
        return f'<Order {self.order_id} : {self.item_id} for {self.quantity} >'