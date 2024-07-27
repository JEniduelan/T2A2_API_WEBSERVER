from init import db, ma
from marshmallow import fields
from marshmallow.validate import Length, And, Regexp

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
    
        user = fields.Nested("UserSchema", only=["id"])
        bible = fields.Nested("BibleSchema", only=["user"] ) 
 
    # VALIDATION
        # Title must be at least 2 characterslong and alphanumerics only 
        title = fields.String(required=True, validate=And(
        Length(min=2, error="Title must be at least 2 characters long"),
        Regexp('^[A-Za-z0-9 ]+$', error="Title must have alphanumerics characters only")
    ))
        # Message must be at least 1 character long and no more than 200 characters long
        message = fields.String(required=True, validate=Length(min=1, max=500), error="message must be between 1 and 500 characters long")  
             
        class Meta:
            fields = ("id","title" ,"message", "date", "user", "bible")
            ordered = True
            
reflection_schema = ReflectionSchema()
reflections_schema = ReflectionSchema(many=True)