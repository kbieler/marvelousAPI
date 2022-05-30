from flask import Blueprint, jsonify, request, flash, redirect, url_for, render_template
from .services import token_required
from app.models import M_Character, db
from app.forms import CreateForm

api = Blueprint('api', __name__, url_prefix='/api')


@api.route('/test', methods=['GET'])
def test():
    super = M_Character.query.all()[0]
    return jsonify(super.to_dict()), 200

@api.route('/create', methods=['GET', 'POST'])
def create():
    try:
        form = CreateForm()
        super = M_Character(form.alias.data, form.name.data, form.description.data, form.comics_appear.data, \
            form.super_power.data, form.owner.data)
    except:
        return jsonify({'error': 'improper request or body data'}), 400
    try:
        db.session.add(super)
        db.session.commit()
        flash(f'Excelsior! {super.alias} is in your team!', category='info')
    except:
        return jsonify({'error': 'alias already exists in the database.'}), 400
    
    return render_template('create.html', form=form)

