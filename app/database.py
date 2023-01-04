from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from psycopg2.extras import RealDictCursor
import psycopg2
import time
from.config import settings

SQLALCHEMY_DATABASE_URL =f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

"""
while True:
  
    try:
           conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres', 
           password='raj1234', cursor_factory=RealDictCursor)      #to connect with the database
           cursor = conn.cursor()                              #calling cursor method and saving to variable name cursor
           print("database connection was successfull!!")
           break
    except Exception as error:
        print("connecting to database failed")
        print("error: ", error)
        time.sleep(2)    
        """    