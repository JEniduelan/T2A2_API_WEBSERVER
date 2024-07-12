from main import app
from Blueprints.cli_bp import db_commands




app.register_blueprint(db_commands)



