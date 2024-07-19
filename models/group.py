from init import db, ma
from marshmallow import fields
from datetime import datetime



class Group(db.Model):
    __tablename__ = "group"
    
    id = db.Column(db.Integer, primary_key=True)
    
    group_name = db.Column(db.String(100), nullable=False)
    date_created = db.Column(db.Date,default=datetime.now().strftime("%Y-%m-%d"))
    
    member_id = db.Column(db.Integer,db.Foreign_key("member.id"), nullable = False)
    # reflection_id = db.Column(db.Integer,db.Foreign_key("reflection.id"), nullable = False)
    
class GroupSchema(ma.Schema):
    
    
    class Meta:
        fields = ("id", "group_name","date_created", "member", "reflection")  
        
group_schema = GroupSchema()
groups_schema = GroupSchema(many=True)
    