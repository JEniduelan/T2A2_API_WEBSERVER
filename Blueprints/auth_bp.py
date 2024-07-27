from init import bcrypt, db

from datetime import timedelta

from flask import Blueprint, request
from flask_jwt_extended import create_access_token,jwt_required, get_jwt_identity
from sqlalchemy.exc import IntegrityError
from psycopg2 import errorcodes

from models.user import User, users_schema, user_schema


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
     
     return{"email": user.email,"is_admin": user.is_admin, "token": jwt_token}
 
    else:
     return{"error": "Please enter a valid username or password"}, 401   
    
    
@auth.route("/")
@jwt_required()
def all_users():
    stmt = db.select(User)
    users = db.session.scalars(stmt).all()
    return users_schema.dump(users)
    
    
@auth.route("/<int:user_id>")
def one_user(user_id):
    stmt = db.select(User).filter_by(id=user_id)
    user = db.session.scalar(stmt)
    
    if user:
        return user_schema.dump(user)
    else:
        return{"error": f"Sorry! no users with id '{user_id}' is found"}, 404
    
    