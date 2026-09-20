from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Todo(BaseModel):
    id: int
    title: str
    completed: bool
    
todos = []

# create todo

@app.post("/todos")
def create_todo(todo:Todo):
    todos.append(todo)
    return{
        "message":"Todo Created",
        "Data": todo
    }   

# fetch todo

@app.get("/todos")
def get_todos():
    return todos

# fetch todo by id

@app.get("/todos/{todo_id}")
def get_todo(todo_id:int):
    for todo in todos:
        if todo.id == todo_id:
            return todo
    return {
        "Error":"Todo not found"
        }

# update todo

@app.put("/todos/{todo_id}")
def todo_update(todo_id:int, updated_todo:Todo):
    for index,todo in enumerate(todos):
        if todo.id == todo_id:
            todos[index] = updated_todo
            return {
                "Message":"Data updated",
                "Data": updated_todo
            }
    return "Todo not found"

# delete todo

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id:int):
    for index,todo in enumerate(todos):
        if todo.id == todo_id:
            todos.pop(index)
            return "Todo Deleted"
    return "Todo not found"
