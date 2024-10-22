
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
    
    # Foreign key - establishes a relationship at the database level
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    # SQLAlchemy relationship - nests an instance of a User model in this one
    user = db.relationship("User", back_populates="bibles")
    # SQLAlchemy relationship - nests an instance of a Reflection model in this one
    reflections = db.relationship("Reflection", back_populates="bible", cascade="all,delete")

    
class BibleSchema(ma.Schema):
       
        user = fields.Nested("UserSchema", only=["name"])
        reflections = fields.List(fields.Nested("ReflectionSchema", exclude=["bible"]))
     
     # VALIDATION
        # Book must contain letters and spaces only
        book = fields.String(
            required=True, 
            validate=Regexp(
                "^[a-zA-Z ,.'-]+$", error="Invalid book name"
                )
            )
        # Version must contain letters only
        version =fields.String(
            required=True, 
            validate=Regexp(
                "^[A-Za-z]+$", 
                error="Invalid book name"
                )
            )
     
        class Meta:
            fields = ("id", "book", "chapter", "verse_number", "version", "verse", "user", "reflections")
            ordered = True
            
bible_schema = BibleSchema()
bibles_schema = BibleSchema(many=True)
            
    