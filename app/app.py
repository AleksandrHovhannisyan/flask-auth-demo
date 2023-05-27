from app import app, database
from app.models import User

@app.shell_context_processor
def make_shell_context():
    return {'database': database, 'User': User}