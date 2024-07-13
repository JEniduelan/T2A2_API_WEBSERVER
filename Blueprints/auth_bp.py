from flask import Blueprint, request
from init import bcrypt, db
from flask_jwt_extended import create_access_token

from models.user import User, user_schema

auth = Blueprint("auth", __name__, url_prefix="/auth")

@auth.route("/register", methods=["POST"])
def register_user():
    
        body_data = request.get_json()
        
        user = User(
            name = body_data.get("name"),
            email = body_data.get("email")
        )
        
        password = body_data.get("password")
        
        if password:
            user.password = bcrypt.generate_password_hash(password).decode("utf-8")
            
        db.session.add(user)
        db.session.commit()  
        
        return user_schema.dump(user), 201
    
    
# @auth.route("/login",)