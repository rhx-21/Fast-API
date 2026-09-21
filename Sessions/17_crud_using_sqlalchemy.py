from fastapi import FastAPI,Depends,HTTPException
from sqlalchemy import create_engine,Column,String,Integer
from sqlalchemy.orm import sessionmaker,declarative_base,Session

app = FastAPI()

class User(BaseModel):
    id:int
    title:str
    completed:str


DATABASE_URL="sqlite:///./user.db"

engine = create_engine(DATABASE_URL,connect_args={"check_same_thread":False})

sessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

class Todo(Base):
    __tablename__="MyTodos"
    
    id = Column(Integer,primary_key=True,index=True)
    title = Column(String)
    completed = Column(String)
    
Base.metadata.create_all(bind=engine)

def get_db():
    
    db = sessionLocal()
    
    try:
        yield db
    finally:
        db.close()
        
@app.post('/todos')
def create_todo(title:str,completed:str, db: Session = Depends(get_db)):
    todo = Todo(title=title,completed=completed)
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return{
        "message":"Todo Created",
        "Data": todo  
        }

@app.get('/todos')
def get_todo(db: Session = Depends(get_db)):
    todos = db.query(Todo).all()
    return{
        "Total":len(todos),
        "Data": todos
    }

@app.get('/todos/{todo_id}')
def get_todo(todo_id:int, db:Session=Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id==todo_id).first()
    if not todo:
        raise HTTPException(status_code=404,detail="Todo not found")
    return todo

@app.put("/todos/{todo_id}")
def update_todo(todo_id:int,title:str,db:Session=Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id==todo_id).first()
    if not todo:
        raise HTTPException(status_code=404,detail="Todo not found")
    todo.title = title
    db.commit()
    db.refresh(todo)
    return{
            "Message":"Todo Updated",
            "Data": todo
        }

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id:int,db:Session=Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id==todo_id).first()
    if not todo:
        raise HTTPException(status_code=404,detail="Todo not found")
    db.delete(todo)
    db.commit()
    return{
        "message":"Todo Deleted"
    }
