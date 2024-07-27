from init import db, ma
from marshmallow import fields

from marshmallow.validate import Regexp, Email, And, Length

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
    follows = db.relationship("Follows", foreign_keys="Follows.follower_id", back_populates="follower", primaryjoin="User.id == Follows.follower_id")
    followed_by = db.relationship("Follows", foreign_keys="Follows.following_id", back_populates="following", primaryjoin="User.id == Follows.following_id")
     
     
class UserSchema(ma.Schema):
    
    bibles = fields.List(fields.Nested("BibleSchema", exclude=["user", "reflections"]))
    reflections = fields.List(fields.Nested("ReflectionSchema", exclude=["user"]))
    follows = fields.Nested("FollowsSchema", only=["following_id", "followed_at"])
    followed_by = fields.Nested("FollowsSchema", only=["follower_id", "followed_at"])
    
    #VALIDATION
    # Name must be at least 1 character long and can only contain letters, spaces, and these characters: ,.'-
    name = fields.String(required=True, validate=And(Length(min=1), Regexp("^[a-zA-Z ,.'-]+$", error='Invalid name')))
    # Email must be a valid email address
    email = fields.String(required=True, validate=Email(error="Invalid email address"))
    # Password must be at least 6 characters long and must contain at least 1 letter, 1 number, and 1 special character
    password = fields.String(required=True, validate=Regexp("^(?=.*[a-zA-Z])(?=.*[0-9])(?=.*[!@#$%^&*()_+]).{6,}$", error="Password must be at least 6 characters, 1 number, and 1 special character"))
    
    class Meta:
        fields = ("id", "name", "email","password", "is_admin", "bibles", "reflections", "follows", "followed_by")
        ordered = True
        

user_schema = UserSchema(exclude=["password"])
users_schema = UserSchema(many=True, exclude=["password"])
