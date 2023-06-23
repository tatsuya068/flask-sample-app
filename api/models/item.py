from api.database import db

class Item(db.Model):
    __tablename__ = 'item'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    price = db.Column(db.Integer)

    def searchBy(id):
        return db.session.query(Item)\
            .filter(Item.id == id)\
            .one()