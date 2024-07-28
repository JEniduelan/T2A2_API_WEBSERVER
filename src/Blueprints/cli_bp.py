from datetime import date

from flask import Blueprint


from init import db, bcrypt
from models.user import User
from models.bible import Bible
from models.reflection import Reflection
from models.follows import Follows



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
            password=bcrypt.generate_password_hash("matthew1!").decode("utf-8"),
            is_admin=True    
        ),
        User(
            name="Mark Tolentino",
            email="marktolentino@email.com",
            password=bcrypt.generate_password_hash("mark1234!").decode("utf-8"),
            
        ),
        User(
            name="john Nieves",
            email="johnn@email.com",
            password=bcrypt.generate_password_hash("john1234!").decode("utf-8"),
            
        )
    ]
   
    db.session.add_all(users)
    db.session.commit()
    
    bibles = [
        Bible(
            book = "Genesis",
            chapter = "1",
            verse_number = "1",
            version = "nkjv",
            verse = "In the beginning God created the heavens and the earth.",
            user=users[0], 
        ),
        Bible(
            book = "Romans",
            chapter ="5" ,
            verse_number = "8",
            version = "nkjv",
            verse = "But God demonstrates His own love toward us, in that while we were still sinners, Christ died for us.",
            user=users[1],
        ),
        Bible(
            book = "2 Timothy",
            chapter = "1",
            verse_number = "7",
            version = "niv",
            verse = "For God has not given us a spirit of fear and timidity, but of power, love, and self-discipline.",
            user=users[2]
        )
    ]
    db.session.add_all(bibles)
    db.session.commit()
    
    reflections = [
        Reflection(
            title = "Reflection1",
            message="Comment 1",
            date=date.today(),
            user=users[0],
            bible=bibles[0]
        ),
        Reflection(
            title = "Reflection2",
            message="Comment 2",
            date=date.today(),
            user=users[1],
            bible=bibles[1]
        ),
        Reflection(
            title = "Reflection3",
            message="Comment 3",
            date=date.today(),
            user=users[2],
            bible=bibles[2]
        )
    ]
    db.session.add_all(reflections)
    db.session.commit()
    
    follows = [
        # User 1 follows User 2 and User 3
        Follows(follower_id=users[0].id, 
                following_id=users[1].id
                ), 
        Follows(follower_id=users[0].id, 
                following_id=users[2].id
                ),

        # User 2 follows User 3
        Follows(follower_id=users[1].id,
                following_id=users[2].id
                ),

        # User 3 follows User 2
        Follows(follower_id=users[2].id,
                following_id=users[1].id
                )
    ]
    
    db.session.add_all(follows)
    db.session.commit()
    
    print("tables seeded")
    