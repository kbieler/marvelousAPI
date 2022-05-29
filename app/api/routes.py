from flask import Blueprint, jsonify, request
from .services import token_required
from app.models import M_Character, db

api = Blueprint('api', __name__, url_prefix='/api')


@api.route('/test', methods=['GET'])
def test():
    super = M_Character.query.all()[0]
    return jsonify(super.to_dict()), 200



