from sqlalchemy.sql import func
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Advert(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(25), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    owner = db.Column(db.String(30), nullable=False)
    owner_email = db.Column(db.String(40), nullable=False)
