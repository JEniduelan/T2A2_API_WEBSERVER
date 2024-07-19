from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from init import db
from models.bible import Bible, BibleSchema, bible_schema, bibles_schema

bible_bp = Blueprint("bible", __name__, url_prefix="/bibles")

@bible_bp.route("/")
def all_bible():
    stmt = db.select(Bible)
    bibles = db.session.scalars(stmt)
    return bibles_schema.dump(bibles)

@bible_bp.route("/<int:id>")
def one_bible(id):
    stmt = db.select(Bible).filter_by(id=id)
    bible = db.session.scalar(stmt)
    
    if bible:
        return bible_schema.dump(bible)
    else:
        return{"error": f"Sorry! no Bible with id {id} is found"}, 404

@bible_bp.route("/", methods=["POST"])
@jwt_required()
def create_bible():
    
    user_id = get_jwt_identity()
    
    bible_info = BibleSchema().load(request.json)
    
    new_bible = Bible(
        book = bible_info.get("book"),
        chapter = bible_info.get("chapter"),
        verse = bible_info.get("verse"),
        version = bible_info.get("verse"),
        text = bible_info.get("text"),
        user_id = user_id
    )
    db.session.add(new_bible)
    db.session.commit()
    
    return BibleSchema(only=["id","name"]).dump(new_bible), 201
    
    
    

    