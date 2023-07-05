from flask_restful import Resource
from flask_restful import marshal_with
from models import User, Therapist, Message

class TherapistResource(Resource):

    @marshal_with(Therapist.fields())
    def get(self, therapist_id):
        therapist = Therapist.query.get(therapist_id)
        return therapist

class UserResource(Resource):

    @marshal_with(User.fields())
    def get(self, user_id):
        user = User.query.get(user_id)
        return user

class MessageResource(Resource):

    @marshal_with(Message.fields())
    def get(self, message_id):
        message = Message.query.get(message_id)
        return message