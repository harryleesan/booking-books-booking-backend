# from datetime import datetime
from app import db
def dump_date(value):
    """Deserialize datetime object into string form for JSON processing."""
    if value is None:
        return None
    return value.strftime("%Y-%m-%d")

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64), index=True)
    last_name = db.Column(db.String(64), index=True)
    created_at = db.Column(db.TIMESTAMP, nullable=False, server_default=db.text("CURRENT_TIMESTAMP"))
    updated_at = db.Column(db.TIMESTAMP, nullable=False, server_default=db.text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    bookings = db.relationship('Booking', backref='booker', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.first_name)


class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    book_id = db.Column(db.String(64), index=True)
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    created_at = db.Column(db.TIMESTAMP, nullable=False, server_default=db.text("CURRENT_TIMESTAMP"))
    updated_at = db.Column(db.TIMESTAMP, nullable=False, server_default=db.text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))

    def __repr__(self):
        return '<Booking {}>'.format(self.book_id)

    @property
    def serialize(self):
        return {
            'book_id': self.book_id,
            'start_date': dump_date(self.start_date),
            'end_date': dump_date(self.end_date)
        }
