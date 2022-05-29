from app.models import User
from functools import wraps
from flask import request, jsonify

def token_required(api_route):
    @wraps(api_route)
    def decorator_function(*args, **kwargs):
        token = request.headers.get('marvel-access-token')
        if not token:
            return jsonify({'Access denied': 'No API token- please register to receive your API token.'}), 401
        if not User.query.filter_by(api_token=token).first():
            return jsonify({'Invalid API token': 'Please check your API token or request a new one.'}), 403
        return api_route(*args, **kwargs)
    return decorator_function
            
