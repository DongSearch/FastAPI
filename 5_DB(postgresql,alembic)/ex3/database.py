from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# DATABASE_URL = "sqlite:///./test.db"
DATABASE_URL = "postgresql://gidong:1234@localhost:5432/testdb"

engine = create_engine(DATABASE_URL,echo=True)
SessionLocal = sessionmaker(bind = engine)