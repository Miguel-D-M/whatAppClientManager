
from config.db import db
from flask import request

from model.item import Item



def get_stocks():
    stocks = db.session.execute(db.select(Item))
    return stocks



def post_stocks():
    for item_data in request.get_json():
        item = Item(
            description=item_data["description"],
            quantity=item_data["quantity"],
            photo=item_data["photo"])
        db.session.add(item)
    db.session.commit()



def get_stock(id):
    stock = db.get_or_404(Item, id)
    return stock
    pass



def update_stock(id):
    item = get_stock(id)
    item.description = request.form["description"]
    item.quantity = request.form["quantity"]
    item.photo = request.form["photo"]
    db.session.add(item)
    db.session.commit()

def delete_stock(id):
    db.session.delete(get_stock(id))
    db.session.commit()
