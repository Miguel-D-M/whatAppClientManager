import app
from flask import request



@app.route('/stock', methods=['GET'])
def get_stocks():
    # to do
    pass
@app.route('/stock', methods=['POST'])
def post_stocks():
    # to do
    pass
@app.route('/stock', methods=['PUT'])
def update_stocks():
    # to do
    pass
@app.route('/stock', methods=['DELETE'])
def delete_stocks():
    # to do
    pass
@app.route('/stock/item/<id>', methods=['GET'])
def get_stock():
    # to do
    pass
@app.route('/stock/item/<id>', methods=['POST'])
def post_stock():
    # to do
    pass
@app.route('/stock/item/<id>', methods=['PUT'])
def update_stock():
    # to do
    pass
@app.route('/stock/item/<id>', methods=['DELETE'])
def delete_stock():
    # to do
    pass


