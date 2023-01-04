from config.db import db
class Message(db.Model):
    id : int = db.Column(db.Integer, primary_key=True)
    customer_id: str = db.Column(db.String,db.ForeignKey('customer.id'),nullable=False)
    date = db.Column(db.DateTime(timezone=True), nullable=False)
    message : str = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Sent by {self.sender}>'