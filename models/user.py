from main import db, ma
from marshmallow import fields

class User(db.Model):
    __tablename__ = "users"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    
    
    
    
class UserSchema(ma.Schema):
    
    class Meta:
        fields = ("id", "name", "email", "password", "admin")
        

user_schema = UserSchema(exclude=["password"])

users_schema = UserSchema(many=True, exclude=["password"])
