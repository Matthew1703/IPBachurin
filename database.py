from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///sql_app.sqlite.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
Session = sessionmaker(autoflush=False, autocommit=False, bind=engine)

Base = declarative_base()

async def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()
