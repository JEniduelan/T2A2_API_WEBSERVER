from datetime import date

from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from init import db
from models.reflection import Reflection, reflection_schema, reflections_schema
from models.bible import Bible

reflection = Blueprint("reflection", __name__)

@reflection.route("/bibles/<int:id>/reflection", methods=["POST"])
@jwt_required()
def create_reflection(id):
    
    body_data = request.get_json()
    stmt = db.select(Bible).filter_by(id=id)
    bible = db.session.scalar(stmt)
    
    if bible:
        reflection = Reflection(
            message = body_data.get("message"),
            date = date.today(),
            bible=bible,
            user_id = get_jwt_identity()
        )
        db.session.add(reflection)
        db.session.commit()
        return reflection_schema.dump(reflection), 201
    
    else:
        return{"error": f"Sorry! no Bible card with id '{id}' is found"}, 404
    

# @reflection.route("/<int:id>", methods=["DELETE"])
# @jwt_required()
# def delete_reflection(relfection_id):
#     stmt = db.select(Reflection).filter_by(id=relfection_id)
#     reflection = db.session.scalar(stmt)
    
#     if reflection:
#         db.session.delete(reflection)
#         db.session.commit()
#         return {"messsage":f"reflection with id '{reflection.message}' has been successfully deleted"}
    
#     else:
#         return {"error": f"Sorry! no reflection with id '{relfection_id}' is found"}, 404
    
    

# @reflection.route("/<int:id>", methods=["PUT", "PATCH"])
# @jwt_required()
# def 