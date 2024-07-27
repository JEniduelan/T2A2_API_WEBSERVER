from datetime import timedelta

from flask import Blueprint, request
from flask_jwt_extended import get_jwt_identity, jwt_required, create_access_token
from sqlalchemy.exc import IntegrityError
from psycopg2 import errorcodes


from init import db, bcrypt
from models.user import User, UserSchema, user_schema, users_schema
from auth import authorize


user_bp = Blueprint("users", __name__, url_prefix="/users")


# Resigter a user
@user_bp.route("/register", methods=["POST"])
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

# Login a user
@user_bp.route("/login", methods = ["POST"])
def login():
    
    data = request.get_json()
    stmt = db.select(User).filter_by(email=data.get("email"))
    user = db.session.scalar(stmt)
    
    if user and bcrypt.check_password_hash(user.password, data.get("password")):
     
     jwt_token = create_access_token(identity=str(user.id), expires_delta=timedelta(minutes=30))
     
     return{"email": user.email,"is_admin": user.is_admin, "token": jwt_token}
 
    else:
     return{"error": "Please enter a valid username or password"}, 401   
 
# Get all users
@user_bp.route("/")
@jwt_required()
def all_users():
    stmt = db.select(User)
    users = db.session.scalars(stmt).all()
    return users_schema.dump(users)
    
# Get one users    
@user_bp.route("/<int:user_id>")
def one_user(user_id):
    stmt = db.select(User).filter_by(id=user_id)
    user = db.session.scalar(stmt)
    
    if user:
        return user_schema.dump(user)
    else:
        return{"error": f"Sorry! no users with id '{user_id}' is found"}, 404
    

# Delete a user
@user_bp.route("/<int:user_id>", methods=["DELETE"])
@jwt_required()
def delete_user(user_id):
    authorize()
    stmt = db.select(User).filter_by(id=user_id)
    user = db.session.scalar(stmt)
    
    if user:
        db.session.delete(user)
        db.session.commit()
        return {"message": f"user {user.username} has been deleted"}
    else:
        return {"error": "Sorry no user was found"}, 404
    

@user_bp.route("/<int:id>/make-admin", methods=["PATCH"])
@jwt_required()
def update_user(id):
    authorize() # Check if the user is admin
    stmt = db.select(User).filter_by(id=id)
    user = db.session.scalar(stmt)

    # Check if the user exists
    if user:
        # Update the user to admin
        user.is_admin = True
        db.session.commit()
        return {"message": "User updated successfully"}
    else:
        return {"error": "Sorry no user was found"}, 404
    
@user_bp.route("/<int:id>/remove-admin", methods=["PATCH"])
@jwt_required()
def remove_admin(id):
    authorize() # Check if the user is admin
    stmt = db.select(User).filter_by(id=id)
    user = db.session.scalar(stmt)

    # Check if the user exists
    if user:
        # Update the user"s is_admin to False
        user.is_admin = False
        db.session.commit()
        return {"message": "User updated successfully"}
    else:
        return {"error": "Sorry no user was found"}, 404