from models import User

def create_user(db,name : str):
    user = User(name = name)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_users(db):
    return db.query(User).all()