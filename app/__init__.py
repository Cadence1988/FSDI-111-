from flask import g
import sqlite3


DB_URI = "main.db"

def get_db():
    db = getattr(g, "_database", None)
    if not db:
        db = g._database = sqlite3.connect(DB_URI)
    return db