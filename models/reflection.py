from init import db, ma
from marshmallow import fields
from datetime import datetime

class Reflection(db.Model):
    __tablename__ = "reflection"
    
    id = db.Column(db.Integer, primary_key=True)
    
    message = db.Column(db.String, nullable=False)
    date = db.Column(db.Date)
    
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    bible_id = db.Column(db.Integer, db.ForeignKey("bible.id"), nullable=False)
    
    user = db.relationship("User", back_populates="reflection")
    bible = db.relationship("Bible", back_populates="reflection")
    group = db.relationship("Group", back_populates="reflection")
class ReflectionSchema(ma.Schema):
    
        user = fields.Nested("UserSchema", only= ["id","name"])
        bible = fields.Nested("BibleSchema", only=["id", "name"])
        group = fields.Nested("GroupSchema", only=["id", "group_name"])
        
class Meta:
    fields = ("id", "message", "date", "user", "bible")

reflection_schema = ReflectionSchema()
reflections_schema = ReflectionSchema(many=True)