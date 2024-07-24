from init import db, ma
from marshmallow import fields

class User(db.Model):
    __tablename__ = "users"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    is_groupmember = db.Column(db.Boolean, default=False)
    
    group_id = db.Column(db.Integer, db.ForeignKey('groups.id')) 
    
    bible = db.relationship("Bible", back_populates="user")
    reflection = db.relationship("Reflection", back_populates="user")
    group = db.relationship("Group", back_populates="user")
    
class UserSchema(ma.Schema):
    
    bible = fields.List(fields.Nested("BibleSchema", exclude=["user"]))
    reflection = fields.List(fields.Nested("ReflectionSchema", exclude=["user"]))
    group = fields.Nested("GroupSchema", exclude=["user", "reflection","bible"] )

    
    
    class Meta:
        fields = ("id", "name", "email", "password", "is_admin","is_groupmember", "bible", "reflection")
      
        

user_schema = UserSchema(exclude=["password"])
users_schema = UserSchema(many=True, exclude=["password"])
