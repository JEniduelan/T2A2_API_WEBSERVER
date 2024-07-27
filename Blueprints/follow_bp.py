from flask import Blueprint
from flask_jwt_extended import jwt_required, get_jwt_identity
from sqlalchemy.exc import IntegrityError
from flask import request, jsonify
from datetime import date
from init import db
from models.follows import Follows
from models.user import User

follows_bp = Blueprint("follows", __name__, url_prefix="/auth")

# Follow a user
@follows_bp.route("/<int:user_id>/follow", methods=["POST"])
@jwt_required()
def follow_user():
    follower_id = request.form.get('follower_id')
    following_id = request.form.get('following_id')
    
    if not follower_id or not following_id:
        return jsonify({'error': 'follower_id and following_id are required'}), 400
    
    try:
        follow = Follows(
            follower_id=int(follower_id), 
            following_id=int(following_id), 
            followed_at=date.today()
        )
        db.session.add(follow)
        db.session.commit()
        return jsonify({'message': 'Followed successfully'}), 201
    except IntegrityError as e:
        db.session.rollback()
        return jsonify({'error': str(e.orig)}), 500
# Unfollow a user
@follows_bp.route("/<int:user_id>/unfollow", methods=["POST"])
@jwt_required()
def unfollow_user(user_id):
    current_user_id = get_jwt_identity()

    if user_id == current_user_id:
        return {"error": "Cannot unfollow yourself"}, 400

    # Check if the user to be unfollowed exists
    user_to_unfollow = User.query.get(user_id)
    if not user_to_unfollow:
        return {"error": "User not found"}, 404

    # Check if the follow relationship exists
    existing_follow = Follows.query.filter_by(follower_id=current_user_id, following_id=user_id).first()
    if not existing_follow:
        return {"error": "Not following this user"}, 400

    # Remove the follow relationship
    db.session.delete(existing_follow)
    db.session.commit()

    return {"message": "User unfollowed successfully"}, 200

# Get list of a user's followers
@follows_bp.route("/<int:user_id>/followers", methods=["GET"])
@jwt_required()
def get_followers(user_id):
    followers = Follows.query.filter_by(following_id=user_id).all()
    
    # Total number of followers
    total_followers = len(followers)
    
    # List of followers (following_id and name)
    followers_list = [{"follower_id": follow.follower_id, "name": follow.follower.name} for follow in followers]
    
    return {"total_followers": total_followers, "followers": followers_list}, 200

# Get list of users a user is following
@follows_bp.route("/<int:user_id>/following", methods=["GET"])
@jwt_required()
def get_following(user_id):
    following = Follows.query.filter_by(follower_id=user_id).all()
    
    # Total number of users being followed
    total_following = len(following)
    
    # List of users being followed (following_id)
    following_list = [{"following_id": follow.following_id, "name": follow.following.name} for follow in following]
    
    return {"total_following": total_following, "following": following_list}, 200