
from init import db, ma
from marshmallow import fields

from marshmallow.validate import Length, And, Regexp

class Bible(db.Model):
    __tablename__ = "bibles"
    
    id = db.Column(db.Integer, primary_key=True)
    
    book = db.Column(db.String, nullable=False)
    chapter = db.Column(db.Integer, nullable=False)
    verse_number = db.Column(db.Integer, nullable=False)
    version = db.Column(db.String, nullable=False)
    verse = db.Column(db.Text, nullable=False)  
    
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

     
    user = db.relationship("User", back_populates="bibles")
    reflections = db.relationship("Reflection", back_populates="bible", cascade="all,delete")

    
class BibleSchema(ma.Schema):
       
        user = fields.Nested("UserSchema", only=["name"])
        reflections = fields.List(fields.Nested("ReflectionSchema", exclude=["bible"]))
     
     #Validate list name input.
        bible = fields.String(required=True, validate=And(
        Length(min=3, error="List name must be a minimum 3 characters long."),
        Regexp("^[A-Za-z0-9 ]+$", error="Only alphanumeric characters allowed in grocery list names.")
        ))
     
     
        class Meta:
            fields = ("id", "book", "chapter", "verse_number", "version", "verse", "user", "reflections")
            ordered = True
            
bible_schema = BibleSchema()
bibles_schema = BibleSchema(many=True)
            
    