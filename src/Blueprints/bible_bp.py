from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from init import db
from models.bible import Bible, bible_schema, bibles_schema

from Blueprints.reflection_bp import reflections_bp 

bible_bp = Blueprint("bibles", __name__, url_prefix="/bibles")

bible_bp.register_blueprint(reflections_bp)

@bible_bp.route("/")
def all_bible():
    stmt = db.select(Bible)
    bibles = db.session.scalars(stmt).all()
    return bibles_schema.dump(bibles)

@bible_bp.route("/<int:bible_id>")
def one_bible(bible_id):
    stmt = db.select(Bible).filter_by(id=bible_id)
    bible = db.session.scalar(stmt)
    
    if bible:
        return bible_schema.dump(bible)
    else:
        return{"error": f"Sorry! no Bible card with id '{bible_id}' is found"}, 404

@bible_bp.route("/", methods=["POST"])
@jwt_required()
def create_bible():
    
    body_data = bible_schema.load(request.get_json())
    
    bible = Bible(
        book = body_data.get("book"),
        chapter = body_data.get("chapter"),
        verse_number = body_data.get("verse_number"),
        version = body_data.get("version"),
        verse = body_data.get("verse"),
        user_id = get_jwt_identity()
    )
    
    db.session.add(bible)
    db.session.commit()
    return bible_schema.dump(bible)

@bible_bp.route("/<int:bible_id>", methods=["DELETE"])
@jwt_required()
def delete_bible(bible_id):
    stmt = db.session.query(Bible).filter_by(id=bible_id)
    bible = db.session.scalar(stmt)
    
    if bible:
        
        db.session.delete(bible)
        db.session.commit()
        return {"message":f"This bible with id '{bible.id}' has been successfuly deleted"}
    
    else:
        return {"error": f"Sorry! no Bible card with id '{id}' is found"}, 404