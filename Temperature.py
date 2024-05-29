from __main__ import db


class Temperature(db.Model):
    __tablename__ = 'data'
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.String(120), nullable=False, unique=True)
    value = db.Column(db.Double, nullable=False, unique=True)


    def to_json(self):
        return {
            "id": self.id,
            "timestamp": self.timestamp,
            "value": self.value
        }