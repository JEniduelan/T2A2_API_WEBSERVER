
from main import db, ma
from marshmallow import fields


class BibleScripture(db.Model):
    __tablename__ = "bible_scripture"
    
    id = db.Column(db.Integer, primary_key=True)
    
    book = db.Column(db.String, nullable=False)
    chapter = db.Column(db.Integer, nullable=False)
    verse = db.Column(db.Integer, nullable=False)
    version = db.Column(db.String, nullable=False)
    text = db.Column(db.Text, nullable=False)  
    
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    
    
    
    class BibleScriptureSchema(ma.Schema):
     
         class Meta:
            fields = ("id", "book", "chapter", "verse", "version", "text", "user_id")
            
bible_scripture_schema = BibleScriptureSchema()
bible_scriptures_schema = BibleScriptureSchema(many=True)
            
    