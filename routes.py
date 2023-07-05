from flask import Blueprint
from flask_restful import Api
from resources import TherapistResource, UserResource, MessageResource

routes = Blueprint('routes', __name__)
api = Api(routes)

api.add_resource(TherapistResource, '/therapist/<int:therapist_id>')
api.add_resource(UserResource, '/user/<int:user_id>')
api.add_resource(MessageResource, '/message/<int:message_id>')