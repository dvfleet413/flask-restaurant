from flask import Flask, render_template
from database.db import initialize_db
from os import environ
from admin import entree
from flask_restful import Api
from resources.routes import initialize_routes

app = Flask(__name__, instance_relative_config=True)
api = Api(app)

app.config['MONGODB_SETTINGS'] = {
    'host': environ.get('MONGODB_URI')
}

app.register_blueprint(entree.bp, url_prefix='/admin')
initialize_db(app)
initialize_routes(api)


@app.route("/")
def home():
    return render_template("/home.html")
    