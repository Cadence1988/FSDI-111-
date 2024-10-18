from flask import (
    Flask,
    render_template,
    request as req
) 
from app.database import task               # from the flask module import the Flask class
# oop--Object oriented paradigm
app = Flask(__name__)              # Create an instance of the flask class (app is now an oblect)

@app.get("/")                       # Flask decorator to map routes to view functions
def get_home():                     # flask view function
    me = {                           # python dictionary (key-value pairs)
        "first_name": "Ryan",
        "last_name": "Marlow",
        "hobbies": "Music",
        "is_online": True
    }
    return me
    
@app.get("/tasks")
def det_all_tasks():
    tasks = task.scan()
    out = {
        "task": tasks,
        "ok":True
    }
    return out

@app.get("/tasks/<int:pk>/")
def get_task_by_id(pk):
    single_task = task.select_by_id(pk)
    out = {
        "task": single_task,
        "ok": True
    } 
    return out

@app.post("/tasks")
def create_task():
    task_data = request.json
    task.insert(task_data)
    return "", 204

@app.put("/tasks/<int:pk>/")
def update_task_by_id(pk):
    task_data = request.json
    task.update_by_id(task_data, pk)
    return "", 204

@app.delete("/tasks/<int:pk>/")
def delete_task_by_id(pk):
    task.delete_by_id(pk)
    return "", 204                           # when you return a dict in flask it is converted to JSON!