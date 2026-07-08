import sqlite3
import pandas as pd

conn = sqlite3.connect ("tasks.db")
cursor = conn.cursor

def add_task():
    cursor.execute("""
    INSERT INTO tasks (title, descrition, status, due_date)
    VALUES ()
    """, (title, description, status, due_date))
    conn.commit()

def get_tasks():
    cursor.execute("SELECT * FROM tasks")
    return cursor.fetchall()

def update_task_status(task_id, new_status):
    cursor.execute("UPDATE tasks SET status=? WHERE id=?", (new_status, task_id))
    conn.commit()

def delete_task(task_id):
    cursor.execute("DELETE FROM tasks WHERE id=?", (task_id,))
    conn.commit()

