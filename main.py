import os 

from flask import Flask

from init import db, ma, bcrypt, jwt
from Blueprints.cli_bp import db_commands
from Blueprints.auth_bp import auth
from Blueprints.bible_bp import bible_bp

# from Blueprints.group_bp import group_bp
def create_app():
    app = Flask(__name__)
    
    app.json.sort_keys = False

    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
                
    app.config["JWT_SECRET_KEY"] = os.environ.get("JWT_SECRET_KEY")

    db.init_app(app)
    ma.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)
 
    app.register_blueprint(db_commands)
    app.register_blueprint(auth)
    app.register_blueprint(bible_bp)
   
    # app.register_blueprint(group_bp)
    
    return app