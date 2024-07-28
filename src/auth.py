from flask import abort
from flask_jwt_extended import get_jwt_identity
from models.user import User
from init import db

def authorise(user_id=None):
    
    # Get the user ID from the JWT token
    jwt_user_id = get_jwt_identity()

    # Select the user from the database using the user ID from the JWT token
    stmt = db.select(User).filter_by(id=jwt_user_id)
    user = db.session.scalar(stmt)

    # Check if the user is admin or if the user ID in the JWT token matches the user ID in the URL
    if not (user.is_admin or (user_id and jwt_user_id == user_id)):
        abort(401)
