from flask import Flask
from database.db import initialize_db
from admin import entree
from flask_restful import Api
from resources.routes import initialize_routes

app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('config.py')
api = Api(app)

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost/flask-restaurant'
}

app.register_blueprint(entree.bp, url_prefix='/admin')
initialize_db(app)
initialize_routes(api)
