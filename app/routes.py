from flask import (
    Flask,
    request 
) 
from app.database import task              # from the flask module import the Flask class
from flask_cors import CORS                                         # oop--Object oriented paradigm
app = Flask(__name__)  
CORS(app)            # Create an instance of the flask class (app is now an oblect)

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
def get_all_tasks():
    tasks = task.scan()
    out = {
        "tasks": tasks,
        "ok":True
    }
    return out

@app.get("/tasks/<int:pk>/")
def get_task_by_id(pk):
    single_task = task.select_by_id(pk)
    if not single_task:
        return {"error": "Task not found"}, 404
    out = {
        "task": single_task,
        "ok": True
    } 
    return out

@app.get("/tasks")
def view_tasks():
    response = requests.get(BACKEND_URL)
    if response.status_code == 200:
        task_list = response.json().get("tasks")
        return render_template("list.html", tasks=task_list)
    return render_template("error.html", error=response.status_code), response.status_code

@app.get("/tasks/<int:pk>/edit/")
def edit_form(pk):
    url = f"{BACKEND_URL}/{pk}"
    response = requests.get(url)
    if response.status_code == 200:
        task_data = response.json().get("task")
        return render_template("edit.html", task=task_data)
    return render_template("error.html", error=response.status_code), response.status_code

@app.post("/tasks/<int:pk>/edit/")
def edit_task(pk):
    task_data = {
        "name": req.form.get("name"),
        "summary": req.form.get("summary"),
        "description": req.form.get("description"),
    }
    url = f"{BACKEND_URL}/{pk}"
    response = requests.put(url, json=task_data)
    if response.status_code == 204:
        return render_template("success.html", message="Task updated")
    return render_template("error.html", error=response.status_code), response.status_code


@app.post("/tasks")
def create_task():
    task_data = request.json
    task.insert(task_data)
    return "", 204

@app.post("/tasks/new/")
def create_task():
    task_data = {
        "name": req.form.get("name"),
        "summary": req.form.get("summary"),
        "description": req.form.get("description"),
    }
    response = requests.post(BACKEND_URL, json=task_data)
    if response.status_code == 204:
        return render_template("success.html", message="Task created")
    return render_template("error.html", error=response.status_code), response.status_code


@app.put("/tasks/<int:pk>/")
def update_task_by_id(pk):
    task_data = request.json
    task.update_by_id(task_data, pk)
    return "", 204

@app.delete("/tasks/<int:pk>/")
def delete_task_by_id(pk):
    task.delete_by_id(pk)
    return "", 204                           # when you return a dict in flask it is converted to JSON!