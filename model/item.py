from config.db import db
from sqlalchemy.sql import func
class Item(db.Model):
    id : int = db.Column(db.Integer, primary_key=True)
    description: str = db.Column(db.String ,nullable=False)
    quantity : int = db.Column(db.Integer)
    photo : str = db.Column(db.String)

    def __repr__(self):
        return f'<Iteam {self.id} : {self.description}>'