from flask import Blueprint, request

from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity


from init import db
from models.group import Group, group_schema, groups_schema

group_bp = Blueprint("group", __name__, url_prefix="/groups")

@group_bp.route("/")
def all_groups():
    stmt = db.select(all_groups)
    groups = db.session.scalars(stmt).all()
    return groups_schema.dump(groups)

@group_bp.route("/<int:id>")
def one_group(id):
    stmt = db.select(groups).filter_by(id=id)
    groups = db.session.scalar(stmt)
    
    if groups:
        return group_schema.dump(groups)
    else:
        return{"error": f"Sorry! no groups with id '{id}' is found"}, 404

@group_bp.route("/", methods=["POST"])
@jwt_required()
def create_group():
    
    body_data = request.get_json()
    
    group = Group(
        group_name = body_data.get("group_name"),
        date = body_data.get("date"),
        user_id = get_jwt_identity()
    )
    
    db.session.add(group)
    db.session.commit()
    return group_schema.dump(group)

@group_bp.route("/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_group(id):
    stmt = db.session.query(Group).filter_by(id=id)
    group = db.session.scalar(stmt)
    
    if group:
        db.session.delete(group)
        db.session.commit()
        return {"message":f"This group with id '{group.id}' has been successfuly deleted"}
    
    else:
        return {"error": f"Sorry! no group with id '{id}' is found"}, 404