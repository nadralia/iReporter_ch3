from flask import Flask,jsonify
from api.routes.user import user_blueprint
from api.routes.incident import incident_blueprint
from api.helpers.welcome import welcome_message


app = Flask(__name__)

app.register_blueprint(user_blueprint)
app.register_blueprint(incident_blueprint)

@app.route('/')
def index():
   return welcome_message

@app.errorhandler(404)
def route_not_found(error):
    """
    Return a custom 404 Http response message for missing or not found routes.
    """
    return jsonify({'message': 'Endpoint not found'}), 404


@app.errorhandler(405)
def method_not_found(error):
    """
    Custom response for methods not allowed for the requested URLs
    """
    return jsonify({'message': 'This method is not allowed for the requested URL'}), 405


@app.errorhandler(500)
def internal_server_error(error):
    """
    Return a custom message for a 500 internal error
    """
    return jsonify({'message': 'Internal server error'}), 500
