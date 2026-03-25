from model import User

def create_user(db, name : str,content : str):
    user = User(name = name,content=content)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_users(db) :
    return db.query(User).all()


