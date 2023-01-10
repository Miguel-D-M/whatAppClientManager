from app import app
from config.db import db
from flask import request

from model.item import Item


@app.route('/stock', methods=['GET'])
def get_stocks():
    stocks = db.session.execute(db.select(Item))
    return stocks


@app.route('/stock', methods=['POST'])
def post_stocks():
    for item_data in request.get_json():
        item = Item(
            description=item_data["description"],
            quantity=item_data["quantity"],
            photo=item_data["photo"])
        db.session.add(item)
    db.session.commit()


@app.route('/stock/item/<int:id>', methods=['GET'])
def get_stock(id):
    stock = db.get_or_404(Item, id)
    return stock
    pass


@app.route('/stock/item/<int:id>', methods=['PUT'])
def update_stock(id):
    item = get_stock(id)
    item.description = request.form["description"]
    item.quantity = request.form["quantity"]
    item.photo = request.form["photo"]
    db.session.add(item)
    db.session.commit()


@app.route('/stock/item/<int:id>', methods=['DELETE'])
def delete_stock(id):
    db.session.delete(get_stock(id))
    db.session.commit()
