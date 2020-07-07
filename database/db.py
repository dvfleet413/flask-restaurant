from flask_mongoengine import MongoEngine
import click
from flask.cli import with_appcontext

db = MongoEngine()


def initialize_db(app):
    db.init_app(app)


@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    initialize_db()
    click.echo('Initialized the database.')