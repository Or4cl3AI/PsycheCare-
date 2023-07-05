from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    password = db.Column(db.String(255))

class Therapist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    therapist_id = db.Column(db.Integer, db.ForeignKey('therapist.id'))
    content = db.Column(db.Text)