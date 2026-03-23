# SQLAlchemy
It is a Python ORM that allows you to interact with databases using Python objects instead of raw SQL.
*ORM(Object Relational Mapping)

# Basic DB Pipeline
1. Create engine(connect to DB)
2. define models(table)
3. create tables
```
Base.metadata.create_all(bind=engine)
```
4. create session (session is a really worker by engaging directly to manage db
5. manage data(crud)


# Modulize files and connect to FastAPI
1. models.py
- define data type in DB

2. database.py
- create DB model and generate Session

3. crud.py
- using data type defined in models.py, it defines the function to manage data in DB

4. schemas.py
- Pydantic models for request/response validation (!!!seperate data for users and servers)
- > why should they be seperated? security(like password..), flexibility, control API structure

5. main.py
- main function for FastAPI

# Should know
1. Depends
- It is a dependency injection system in FastAPI.
- It allows you to declare dependencies (e.g., database, authentication).
- FastAPI automatically executes the dependency function before the endpoint runs and injects the result.

2. basic crud
```
db.add(user) # Read
db.commit() # action
db.refresh(user) # synchronoization
```
