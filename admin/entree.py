from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort
from database.models import Entree

bp = Blueprint('entree', __name__)


@bp.route('/')
def index():
    entrees = Entree.objects().to_json()
    return render_template('entree/index.html', entrees=entrees)


@bp.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        name = request.form['name']
        wines = request.form['wines']
        allergens = request.form['allergens']
        error = None

        if not name:
            error = "Entree name is required"

        if error is not None:
            flash(error)
        else:
            Entree(name=name, wines=wines, allergens=allergens).save()
            return redirect(url_for('entree.index'))

    return render_template('entree.create.html')


def get_entree(id):
    entree = Entree.objects().get(id=id)
    if entree is None:
        abort(404, "Entree id {0} doesn't exist.".format(id))

    return entree


@bp.route('/<id>/update', methods=('GET', 'POST'))
def update(id):
    entree = get_entree(id)

    if request.method == 'POST':
        name = request.form['name']
        wines = request.form['wines']
        allergens = request.form['allergens']
        error = None

        if not name:
            error = "Entree name is required"

        if error is not None:
            flash(error)
        else:
            entree.name = name
            entree.wines = wines
            entree.allergens = allergens
            entree.save()
            return redirect(url_for('entree.index'))

    return render_template('entree/update.html', entree=entree)


@bp.route('/<id>/delete', methods=('POST',))
def delete(id):
    entree = get_entree(id)
    entree.delete()
    return redirect(url_for('entree.index'))
