from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# Connect to DB(SQLite), generate ./test.db
engine = create_engine("sqlite:///./test.db")
# Basic Class
Base = declarative_base()

# define table
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True) # autmoatically increase
    name = Column(String)

# create table
Base.metadata.create_all(bind=engine) # if there's not table, it generates

# generate session
SessionLocal = sessionmaker(bind=engine) # that is exactly part to handle data
db = SessionLocal()

# create data
user = User(name = "Dong")
user2 = User(name = "Min")
db.add(user) # ready
db.add(user2)
db.commit() # action!

users = db.query(User).all() # users is object
if user in users :
    print(user.id,user.name)