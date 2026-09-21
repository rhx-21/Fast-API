# pip install sqlalchemy
# ORM - Database ko python code k through handle karne ka tareeka hai

from sqlalchemy import create_engine,Column,Integer,String
from sqlalchemy.orm import sessionmaker,declarative_base,Session
from fastapi import FastAPI,Depends

app = FastAPI()

# Database URL
DATABASE_URL = "sqlite:///./test.db"

# connect database
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread":False}
)

# Create Sessions - interact with db (operation handle in db)
sessionLocal = sessionmaker(bind=engine)

# Model banane k liye base
Base = declarative_base()

# Table (Model)
class Todo(Base):
    __tablename__ = "Todos"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    completed = Column(String)
    
# Table Create
Base.metadata.createall(bind=engine)

# Dependency(DB Session Provide Karega)
def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get('/')
def home(db: Session = Depends(get_db)):
    return{
        "message":"DB Connected"
    } 


