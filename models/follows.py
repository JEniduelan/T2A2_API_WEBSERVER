from init import db, ma
from marshmallow import fields
from datetime import datetime

class Follows(db.Model):
    __tablename__ = "follows"
    
    id = db.Column(db.Integer, primary_key=True) 
    # Foreign key - establishes a relationship at the database level
    follower_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    following_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    
    followed_at = db.Column(db.Date, default=datetime.now().strftime('%Y-%m-%d'))
    
    
    # Specify the foreign keys in the relationships
    follower = db.relationship(
        "User", 
        foreign_keys=[follower_id], 
        back_populates="follows"
        )
    following = db.relationship(
        "User", 
        foreign_keys=[following_id], 
        back_populates="followed_by"
        )


 
class FollowsSchema(ma.Schema):
    # Tell Marshmallow to nest a UserSchema instance when serializing the follower and following attributes    
    follower = fields.Nested("UserSchema", only=["id", "name"])
    following = fields.Nested("UserSchema", only=["id", "name"])
        
    class Meta:
        fields = ("id", "follower_id", "following_id","followed_at", "follower", "following")
        ordered = True  

follow_schema = FollowsSchema()
follows_schema = FollowsSchema(many=True)