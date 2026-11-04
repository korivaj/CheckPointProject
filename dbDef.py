from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone
from app import db

class LockRatings(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    american = db.Column(db.Integer, nullable=False)
    link = db.Column(db.Integer, nullable=False)
    master_lock = db.Column(db.Integer, nullable=False)
    smart = db.Column(db.Integer, nullable=False)

    name = db.Column(db.String(50),nullable=False)
    created_at = db.Column(db.DateTime)

class AnimeRatings(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    
    dbz = db.Column(db.Integer, nullable=False)
    naruto = db.Column(db.Integer, nullable=False)
    onepiece = db.Column(db.Integer, nullable=False)
    inuyasha = db.Column(db.Integer, nullable=False)

    name = db.Column(db.String(50),nullable=False)
    created_at = db.Column(db.DateTime)

class BikeRatings(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    
    Panigale = db.Column(db.Integer, nullable=False)
    Diavel = db.Column(db.Integer, nullable=False)
    scout_bobber = db.Column(db.Integer, nullable=False)
    Ninja = db.Column(db.Integer, nullable=False)
    Indian = db.Column(db.Integer, nullable=False)

    name = db.Column(db.String(50),nullable=False)
    created_at = db.Column(db.DateTime)

class ResidentRatings(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    
    Chris = db.Column(db.Integer, nullable=False)
    Claire = db.Column(db.Integer, nullable=False)
    Jill = db.Column(db.Integer, nullable=False)
    Leon = db.Column(db.Integer, nullable=False)

    name = db.Column(db.String(50),nullable=False)
    created_at = db.Column(db.DateTime)
