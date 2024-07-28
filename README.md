# T2A2_API_WEBSERVER


## Bible Notebook App

### Table of Contents
+ [**R1 - Explain the problem that this app will solve, and explain how this app solves or addresses the problem.**](#r1) 
+ [**R2 - Describe the way tasks are allocated and tracked in your project**](#r2) 
+ [**R3 - List and explain the third-party services, packages and dependencies used in this app.**](#r3) 
+ [**R4 - Explain the benefits and drawbacks of this app’s underlying database system.**](#r4) 
+ [**R5 - Explain the features, purpose and functionalities of the object-relational mapping system (ORM) used in this app.**](#r5) 
+ [**R6 - Design an entity relationship diagram (ERD) for this app’s database, and explain how the relations between the diagrammed models will aid the database design.**](#r6) 
+ [**R7 - Explain the implemented models and their relationships, including how the relationships aid the database implementation.**](#r7) 
+ [**R8 - Explain how to use this application’s API endpoints. Each endpoint should be explained, including the following data for each endpoint:HTTP verb, Path or route, Any required body or header data, Response.**](#r8) 

---

### **R1 - Explain the problem that this app will solve, and explain how this app solves or addresses the problem.** <a id="r1"></a>

I am developing this app to address the common issue that my friends and I currently facing and many of us have experienced the frustration of always having to buy new paper notebooks to write down our thoughts and reflections on Bible verses. These notebooks can be easily misplaced, and finding a specific entry among many can be a hassle. Moreover, sharing your insights and reflections with others becomes difficult when everything is confined to paper.

This project provides a seamless digital solution to this problem. Instead of relying on paper notebooks, you can now easily input Bible verses and add your personal reflections directly into the app. This digital approach ensures that your reflections are always accessible and organised, eliminating the need to keep buying and storing physical notebooks.

---

### **R2 - Describe the way tasks are allocated and tracked in your project** <a id="r2"></a>


In this project, I used Trello to effectively track and allocate tasks for building my app. I organized my workflow into four sections: Backlog, To Do, Doing, and Done. Additionally, I implemented a three-level priority scale: low, medium, and high. Each task is assigned a due date and categorised based on its priority level. This system ensures that tasks are managed efficiently and deadlines are met systematically. Please click the linked provided for the Trello reference 

[GitHub Projects](https://trello.com/invite/b/668c85dceb3c2b115bd9d62b/ATTIbc0776acf568829eba959edc062fc3687F9969C5/t2a2apiwebserverq)

Here are the screenshots from Trello throughout the developement.

![Trello](docs/1%20trello.png)
![Trello](docs/2%20trello.png)
![Trello](docs/3%20trello.png)
![Trello](docs/4%20trello.png)
![Trello](docs/5%20trello.png)
![Trello](docs/6%20trello.png)
![Trello](docs/7%20trello.png)
![Trello](docs/8%20trello.png)
![Trello](docs/9%20trello.png)
![Trello](docs/10%20trello.png)
![Trello](docs/11%20trello.png)
![Trello](docs/12%20trello.png)

---

### **R3 - List and explain the third-party services, packages and dependencies used in this app.** <a id="r3"></a>

#### Flask:
I use Flask to build the different parts of my app, such as routes, which determine what happens when someone makes a request. It's the framework that helps structure my app and handle requests seamlessly.

#### PostgreSQL:
PostgreSQL is the database where I store all the important information for my app. Think of it as an intelligent, organized filing cabinet that keeps everything in order for quick and easy access.

#### SQLAlchemy:
SQLAlchemy is my go-to tool for interacting with the database. It translates Python code into SQL queries, ensuring smooth communication between my app and the database without any complications.

#### Psycopg2:
Psycopg2 works like a reliable courier between my app and the PostgreSQL database. It ensures that whenever my app sends or requests data from the database, the information is delivered safely and correctly.

#### Marshmallow:
Marshmallow helps convert complex Python objects into a format that can be easily shared, like JSON. It ensures data is serialized and deserialized properly, making data exchange straightforward.

#### JWT Manager:
When users log in, they get a special token that lets them access parts of the app without having to log in each time. Think of it as a digital pass that keeps them logged in. JWT Manager creates and checks these tokens, ensuring that access is both secure and easy.

#### Bcrypt:
Bcrypt is used to hash passwords securely. It takes user-created passwords, converts them into a string of generated characters, and stores them safely, ensuring that passwords are protected.

#### Dotenv:
Reads key-value pairs from a .env file and can set them as environment variables.

---

### **R4 - Explain the benefits and drawbacks of this app’s underlying database system.** <a id="r4"></a>

The database system used for this application is Postgresql and this is perfect for my app for a number of reasons:

#### Benifits

- **Reliability:** PostgreSQL is known for its rock-solid reliability. It's great at handling complex transactions and keeping data accurate, which is crucial for any application where data integrity is essential.

- **ACID Compliance:** PostgreSQL adheres to the ACID principles (Atomicity, Consistency, Isolation, Durability), ensuring that our app's data remains consistent and secure even in the event of system failures or unexpected issues.

- **Extensibility:**  PostgreSQL is highly customizable. Its extensibility allows me to tailor the database to my app's specific needs, ensuring it can adapt and grow with my application over time.

- **Active Community Support:** The PostgreSQL community is vibrant and supportive, offering extensive resources, documentation, and forums. This support network is invaluable for troubleshooting and following industry best practices.

#### Drawbacks

- **Learning Curve:** Postgresql can be complex for beginners as it has a broad range of advanced features and extensive configuration options which can be overwhelming to set up and handle than other database systems. Despite this, the long-term benefits make the initial effort worthwhile.

- **Horizontal Scalability Challenges:** While PostgreSQL excels in many areas, it may face challenges with extreme horizontal scalability compared to some NoSQL databases designed for large, distributed systems. In such cases, alternative databases might offer more straightforward solutions.

Sources:
https://docs.digitalocean.com/glossary/acid/#:~:text=state%20ensuring%20durability.-,PostgreSQL,order%20to%20keep%20data%20consistent.
https://onesignal.com/blog/lessons-learned-from-5-years-of-scaling-postgresql/
https://www.guru99.com/introduction-postgresql.html

--- 

### **R5 - Explain the features, purpose and functionalities of the object-relational mapping system (ORM) used in this app.** <a id="r5"></a>

In my project, SQLAlchemy acts as a vital bridge between my code and the database. It serves as an Object-Relational Mapping (ORM) tool, making it easy for my app to interact with the database. By translating complex database queries into simple Python code, SQLAlchemy ensures smooth and efficient communication, allowing me to focus on developing features rather than managing database interactions.

#### Features and functionalities

- **Declarative Syntax:** Allows defining models using Python classes, making the code more readable and maintainable. For example in my User model:

```python
class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
```

- **Relationships:** Supports defining relationships between models using foreign keys and relationship properties. For example in my Follows model:


```python
class Follows(db.Model):
    __tablename__ = "follows"
    id = db.Column(db.Integer, primary_key=True)
    follower_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    following_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    follower = db.relationship("User", foreign_keys=[follower_id], back_populates="follows")
    following = db.relationship("User", foreign_keys=[following_id], back_populates="followed_by")
```

- **Querying:** Provides a powerful querying API for database interactions. For instance, if I wanted to delete a Bible entry from the database, SQLAlchemy makes this task straightforward and efficient.


```python
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
```


- **Serialization:** Uses Flask-Marshmallow for serializing and deserializing model instances. For example, the FollowsSchema:

```python
class FollowsSchema(ma.Schema):
    # Tell Marshmallow to nest a UserSchema instance when serializing the follower and following attributes    
    follower = fields.Nested("UserSchema", only=["id", "name"])
    following = fields.Nested("UserSchema", only=["id", "name"])
        
    class Meta:
        fields = ("id", "follower_id", "following_id","followed_at", "follower", "following")
        ordered = True  

follow_schema = FollowsSchema()
follows_schema = FollowsSchema(many=True)
```

---

### **R6 - Design an entity relationship diagram (ERD) for this app’s database, and explain how the relations between the diagrammed models will aid the database design.** <a id="r6"></a>


---

### **R7 - Explain the implemented models and their relationships, including how the relationships aid the database implementation.** <a id="r7"></a>

class User(db.Model):
	__tablename__ = "users"
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String)
	email = db.Column(db.String, nullable=False, unique=True)
	password = db.Column(db.String, nullable=False)
	is_admin = db.Column(db.Boolean, default=False)


---

#### Bible Model:


---

#### Reflection Model:


---

#### Follows Model:




---

### **R8 - Explain how to use this application’s API endpoints. Each endpoint should be explained, including the following data for each endpoint:HTTP verb, Path or route, Any required body or header data, Response.** <a id="r8"></a>


