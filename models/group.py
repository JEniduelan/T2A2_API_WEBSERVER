from init import db, ma
from marshmallow import fields
from datetime import datetime



class Group(db.Model):
    __tablename__ = "groups"
    
    id = db.Column(db.Integer, primary_key=True)
    
    group_name = db.Column(db.String(100), nullable=False)
    date_created = db.Column(db.Date,default=datetime.now().strftime("%Y-%m-%d"))
    
    reflection_id = db.Column(db.Integer,db.ForeignKey("reflections.id"), nullable = False)
   
    users = db.relationship("User", back_populates="group")
    bible = db.relationship("Bible", back_populates="groups")
    reflections = db.relationship('Reflection', back_populates="group")
    
class GroupSchema(ma.Schema):
    
    user = fields.List(fields.Nested("UserSchema", only=["id", "name"]))
    bible = fields.List(fields.Nested("BibleSchema", only=["id", "book", "chapter", "verse_number", "version", "verse"]))
    reflection = fields.List(fields.Nested("ReflectionSchema", only=["id", "title", "message", "date"]))
    
    class Meta:
        fields = ("id", "group_name","date_created", "user","bible","reflection")  
        
group_schema = GroupSchema()
groups_schema = GroupSchema(many=True)
    