
from init import db, ma
from marshmallow import fields


class Bible(db.Model):
    __tablename__ = "bible"
    
    id = db.Column(db.Integer, primary_key=True)
    
    book = db.Column(db.String, nullable=False)
    chapter = db.Column(db.Integer, nullable=False)
    verse_number = db.Column(db.Integer, nullable=False)
    version = db.Column(db.String, nullable=False)
    verse = db.Column(db.Text, nullable=False)  
    
    #foreign key which establishes the relationship at the database level
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    # group_id = db.Column(db.Integer, db.ForeignKey("group.id"), nullable=False)
    
   
    user = db.relationship("User", back_populates="bible")
    # group = db.relationship("Group", back_populates="bible")
    reflection = db.relationship("Reflection", back_populates="bible", cascade="all,delete")
    

    
class BibleSchema(ma.Schema):
       
        user = fields.Nested("UserSchema", only=["id", "name"])
        reflection = fields.List(fields.Nested("ReflectionSchema", exclude=["bible"]))
        # group = fields.Nested("GroupSchema",only=["id"] )
     
        class Meta:
            fields = ("id", "book", "chapter", "verse_number", "version", "verse", "user", "reflection")
            ordered = True
            
bible_schema = BibleSchema()
bibles_schema = BibleSchema(many=True)
            
    