from init import db, ma
from marshmallow import fields

from models.follows import Follows

class User(db.Model):
    __tablename__ = "users"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    
    
      
    bibles = db.relationship("Bible", back_populates="user")
    reflections = db.relationship("Reflection", back_populates="user")

    followers = db.relationship("Follows", foreign_keys= "Follows.follower_id", back_populates="follower", primaryjoin='User.id == Follows.follower_id')
    following = db.relationship("Follows", foreign_keys="Follows.following_id", back_populates="following", primaryjoin="User.id == Follows.following_id")

class UserSchema(ma.Schema):
    
    bibles = fields.List(fields.Nested("BibleSchema", exclude=["user"]))
    reflections = fields.List(fields.Nested("ReflectionSchema", exclude=["user"]))

    follows = fields.Nested("FollowsSchema", only=["following_id", "followed_at"])
    followed_by = fields.Nested("FollowsSchema", only=["follower_id", "followed_at"])
    
    
    class Meta:
        fields = ("id", "name", "email", "groupmember","password", "is_admin", "bibles", "reflections", "follows", "followed_by")
      
        

user_schema = UserSchema(exclude=["password"])
users_schema = UserSchema(many=True, exclude=["password"])
