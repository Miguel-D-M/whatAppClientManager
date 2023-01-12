from config.db import db
from flask import request

from model.order_line import Order_Line
from model.order import Order


def validate_order(customer_id,order_data):
    order = create_order(customer_id)
    for order_line in order_data:
        add_order_line(order,order_line.item,order_line.quantity)
    db.session.commit()
def get_all_orders() -> list[Order]:
    return db.session.execute(db.select(Order))


def get_order(id) -> Order:
    return db.get_or_404(Order, id)


def create_order(customer_id) -> Order:
    order = Order(customer_id=customer_id)
    db.session.add(order)
    db.session.commit()
    return order


def add_order_line(order, item, quantity) ->None:
    order_line = Order_Line(
        order_id=order.id,
        item_id=item.id,
        quantity=quantity
    )
    db.session.add(order_line)


def get_order_line(order_id, id) -> Order_Line:
    return db.get_or_404(Order_Line, order_id, id)


def delete_stock(order_id, id) -> None:
    db.session.delete(get_order_line(order_id, id))
    db.session.commit()
