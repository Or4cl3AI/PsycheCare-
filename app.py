import os
import json
from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/sqlite.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
api = Api(app)

from models import User, Therapist, Message
from resources import TherapistResource, UserResource, MessageResource
import routes

if __name__ == '__main__':
    app.run()