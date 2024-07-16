from init import bcrypt, db

from datetime import timedelta

from flask import Blueprint, request
from flask_jwt_extended import create_access_token
from sqlalchemy.exc import IntegrityError
from psycopg2 import errorcodes


from models.user import User, user_schema

auth = Blueprint("auth", __name__, url_prefix="/auth")

@auth.route("/register", methods=["POST"])
def register():
    try:
        data = request.get_json()
            
        user = User(
                name = data.get("name"),
                email = data.get("email")
            )
            
        password = data.get("password")
            
        if password:
                user.password = bcrypt.generate_password_hash(password).decode("utf-8")
                
        db.session.add(user)
        db.session.commit()  
            
        return user_schema.dump(user), 201
    
    except IntegrityError as err:
        if err.orig.pgcode == errorcodes.NOT_NULL_VIOLATION:
            return {"error": f"The column {err.orig.diag.column_name} is required"}, 409
        if err.orig.pgcode == errorcodes.UNIQUE_VIOLATION:
            return {"error": "Email already exist, please try another email."}, 409


@auth.route("/login", methods = ["POST"])
def login():
    
    data = request.get_json()
    stmt = db.select(User).filter_by(email=data.get("email"))
    user = db.session.scalar(stmt)
    if user and bcrypt.check_password_hash(user.password, data.get("password")):
     
     jwt_token = create_access_token(identity=str(user.id), expires_delta=timedelta(minutes=30))
     return{"email": user.email, "token": jwt_token}
 
    else:
        return{"error": "Please enter a valid username or password"}, 401   
    
    
    
    
    
    