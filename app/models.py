from . import db


class Property(db.Model):
    __tablename__ = 'properties'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    num_rooms = db.Column(db.Integer, nullable=False)
    num_baths = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    type = db.Column(db.String(20), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    photo = db.Column(db.String(255), nullable=False)

    def __init__(self, title, description, num_rooms, num_baths, price, type, location, photo):
        self.title = title
        self.description = description
        self.num_rooms = num_rooms
        self.num_baths = num_baths
        self.price = price
        self.type = type
        self.location = location
        self.photo = photo

 