from init import db, ma
from marshmallow import fields
from datetime import datetime



class Group(db.Model):
    __tablename__ = "groups"
    
    id = db.Column(db.Integer, primary_key=True)
    
    group_name = db.Column(db.String(100), nullable=False)
    date_created = db.Column(db.Date,default=datetime.now().strftime("%Y-%m-%d"))
    
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"), nullable = False)
    reflection_id = db.Column(db.Integer,db.ForeignKey("reflection.id"), nullable = False)
   
    
class GroupSchema(ma.Schema):
    
    user = fields.List(fields.Nested("UserSchema", only=["id", "name"]))
    bible = fields.List(fields.Nested("BibleSchema", only=["id", "book", "chapter", "verse_number", "version", "verse"]))
    reflection = fields.List(fields.Nested("ReflectionSchema", only=["id", "message", "date"]))
    
    class Meta:
        fields = ("id", "group_name","date_created", "user", "reflections")  
        
group_schema = GroupSchema()
groups_schema = GroupSchema(many=True)
    