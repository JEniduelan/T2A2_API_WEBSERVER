from datetime import date

from flask import Blueprint

from init import db, bcrypt
from models.user import User
from models.bible import Bible
from models.reflection import Reflection
from models.group import Group



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
            is_groupmember=True
        ),
        User(
            name="Mark Tolentino",
            email="marktolentino@email.com",
            password=bcrypt.generate_password_hash("mark1").decode("utf-8"),
            is_admin=True,
            is_groupmember=True
        )
    ]
    db.session.add_all(users)
    
    bible = [
        Bible(
            book = "Genesis",
            chapter = "1",
            verse_number = "1",
            version = "nkjv",
            verse = "In the beginning God created the heavens and the earth.",
            user=users[0]
        ),
        Bible(
            book = "Romans",
            chapter ="5" ,
            verse_number = "8",
            version = "nkjv",
            verse = "But God demonstrates His own love toward us, in that while we were still sinners, Christ died for us.",
            user=users[1]
        )
    ]
    db.session.add_all(bible)
    
    reflection = [
        Reflection(
            message = "message1",
            date = date.today(),
            user=users[0],
            bible = bible[0]
        ),
        Reflection(
            message = "message2",
            date = date.today(),
            user=users[1],
            bible = bible[1]
        )
    ]
    db.session.add_all(reflection)
    
    group = [
        Group(
            group_name = "group1",
            date_created = date.today(),
            reflection = reflection[0]
        ),
        Group(
            group_name = "group2",
            date_created = date.today(),
            reflection = reflection[1]
        )
    ]
    db.session.add_all(group)
    db.session.commit()
    
    print("tables seeded")
    