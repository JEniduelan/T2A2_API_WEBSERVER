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

- **Reliability:** PostgreSQL is known for its rock-solid reliability. It's great at handling complex transactions and keeping data accurate, which is crucial for any application where data integrity is essential.

- **ACID Compliance:** PostgreSQL adheres to the ACID principles (Atomicity, Consistency, Isolation, Durability), ensuring that our app's data remains consistent and secure even in the event of system failures or unexpected issues.

- **Extensibility:**  PostgreSQL is highly customizable. Its extensibility allows me to tailor the database to my app's specific needs, ensuring it can adapt and grow with my application over time.

- **Active Community Support:** The PostgreSQL community is vibrant and supportive, offering extensive resources, documentation, and forums. This support network is invaluable for troubleshooting and following industry best practices.

However, there are some drawbacks:

- **Learning Curve:** Postgresql can be complex for beginners as it has a broad range of advanced features and extensive configuration options which can be overwhelming to set up and handle than other database systems. Despite this, the long-term benefits make the initial effort worthwhile.

- **Horizontal Scalability Challenges:** While PostgreSQL excels in many areas, it may face challenges with extreme horizontal scalability compared to some NoSQL databases designed for large, distributed systems. In such cases, alternative databases might offer more straightforward solutions.

Sources:
https://docs.digitalocean.com/glossary/acid/#:~:text=state%20ensuring%20durability.-,PostgreSQL,order%20to%20keep%20data%20consistent.
https://onesignal.com/blog/lessons-learned-from-5-years-of-scaling-postgresql/
https://www.guru99.com/introduction-postgresql.html

--- 

### **R5 - Explain the features, purpose and functionalities of the object-relational mapping system (ORM) used in this app.** <a id="r5"></a>


---

### **R6 - Design an entity relationship diagram (ERD) for this app’s database, and explain how the relations between the diagrammed models will aid the database design.** <a id="r6"></a>


---

### **R7 - Explain the implemented models and their relationships, including how the relationships aid the database implementation.** <a id="r7"></a>

#### User Model:


---

#### Bible Model:


---

#### Reflection Model:


---

#### Follows Model:




---

### **R8 - Explain how to use this application’s API endpoints. Each endpoint should be explained, including the following data for each endpoint:HTTP verb, Path or route, Any required body or header data, Response.** <a id="r8"></a>


