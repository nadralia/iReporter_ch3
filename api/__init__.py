from flask import Flask
from api.routes.user import user_blueprint


app = Flask(__name__)

app.register_blueprint(user_blueprint)

@app.route('/')
def index():
   pass
