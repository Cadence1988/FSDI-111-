from flask import Flask            # from the flask module import the Flask class
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
    return me                       # when you return a dict in flask it is converted to JSON!