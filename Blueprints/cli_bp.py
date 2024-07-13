from flask import Blueprint

from main import db, bcrypt
from models.user import User


db_commands = Blueprint("db", __name__)

@db_commands.cli.command("create")
def db_create():
    db.create_all()
    print("Tables have been created")
    
@db_commands.cli.command("drop")
def db_drop():
    db.drop_all()
    print("Tables have been dropped")
    
@db_commands.cli.command("seed")
def db_seed():
    users = [
        User(
            name="Matthew Santos",
            email="matthew@email.com",
            password=bcrypt.generate_password_hash("matthew1").decode("utf-8"),
            is_admin=True
        ),
        User(
            name="Mark Tolentino",
            email="marktolentino@email.com",
            password=bcrypt.generate_password_hash("mark123").decode("utf-8"),
            is_admin=False
        )
    ]
 
    db.session.add_all(users)
    db.session.commit()
    
    print("tables seeded")