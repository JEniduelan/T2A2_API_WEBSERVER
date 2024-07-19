from main import db, ma
from marshmallow import fields
from datetime import datetime

class Reflection(db.Model):
    __tablename__ = "reflection"
    
    id = db.Column(db.integer, primary_key=True)
    message =db.Column(db.text)
    date_created =db.Column(db.Date, default=datetime.now().strftime("%Y-%m-%d"))
    
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    bible_id = db.Column(db.Integer, db.ForeignKey("bible.id"), nullable=False)
    
    
class ReflectionSchema(ma.Schema):
        
    class Meta:
        fields = ("id", "message", "date_created", "user", "bible")

reflection_schema = ReflectionSchema()
reflections_schema = ReflectionSchema(many=True)