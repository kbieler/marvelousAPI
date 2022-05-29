from app import app
from app.models import db, M_Character, User

@app.shell_context_processor
def shell_context():
    return {'db': db, 'M_Character': M_Character, 'User': User}

    