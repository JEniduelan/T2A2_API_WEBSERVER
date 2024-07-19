from main import db, ma
from marshmallow import fields

class GroupMember(ma.Model):
    __tablename__ = "groupmember"
    
    id = db.column (db.integer, primary_key=True)
    
    role = db.Column(db.String, nullable=True)
    
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    
class GroupMemberSchema(ma.Schema):
    
    class Meta:
        fields = ("id", "user", "role")
        
groupmember_schema = GroupMemberSchema()
groupmembers_schema = GroupMemberSchema(many=True)
    