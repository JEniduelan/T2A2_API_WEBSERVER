from init import db, ma
from marshmallow import fields


class Reflection(db.Model):
    __tablename__ = "reflections"
    
    id = db.Column(db.Integer, primary_key=True)
    
    title = db.Column(db.String, nullable=False)
    message = db.Column(db.Text, nullable=False)
    date = db.Column(db.Date)
    
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    bible_id = db.Column(db.Integer, db.ForeignKey("bibles.id"), nullable=False)
    
    
    user = db.relationship("User", back_populates="reflections")
    bible = db.relationship("Bible", back_populates="reflections")
    
    
    
    
class ReflectionSchema(ma.Schema):  
    
        user = fields.Nested("UserSchema", only=["name"])
        bible = fields.Nested("BibleSchema", only=["reflections"] ) 
        
        class Meta:
            fields = ("id","title" ,"message", "date", "user", "bible")
            ordered = True
            
reflection_schema = ReflectionSchema()
reflections_schema = ReflectionSchema(many=True)