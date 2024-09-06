import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime

# Function to add a new task
def add_task():
    task_name = task_entry.get()
    due_date = date_entry.get()
    due_time = time_entry.get()
    
    if task_name:
        if due_date:
            if due_time:
                task_with_datetime = f"{task_name} (Due {due_date} at {due_time})"
            else:
                task_with_datetime = f"{task_name} (Due {due_date})"
        else:
            task_with_datetime = task_name
        
        tasks.append(task_with_datetime)
        update_task_list()
        save_tasks()
        clear_entries()
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

# Function to clear entry fields
def clear_entries():
    task_entry.delete(0, tk.END)
    date_entry.delete(0, tk.END)
    time_entry.delete(0, tk.END)

# Function to update the task list in the ListBox
def update_task_list():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        task_listbox.insert(tk.END, task)

# Function to save tasks to a file
def save_tasks():
    with open('tasks.txt', 'w') as f:
        for task in tasks:
            f.write(task + '\n')

# Function to load tasks from a file
def load_tasks():
    try:
        with open('tasks.txt', 'r') as f:
            for line in f:
                tasks.append(line.strip())
    except FileNotFoundError:
        pass

# Function to mark a task as completed
def mark_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        tasks.pop(selected_task_index)
        update_task_list()
        save_tasks()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to mark as completed.")

root = tk.Tk()
root.title("To-Do List App")

tasks = []

load_tasks()

entry_frame = ttk.Frame(root)
entry_frame.pack(pady=10)

task_label = ttk.Label(entry_frame, text="Task:")
task_label.grid(row=0, column=0, padx=5, pady=5)

task_entry = ttk.Entry(entry_frame, width=40)
task_entry.grid(row=0, column=1, padx=5, pady=5)

date_label = ttk.Label(entry_frame, text="Due Date:")
date_label.grid(row=1, column=0, padx=5, pady=5)

date_entry = ttk.Entry(entry_frame, width=15)
date_entry.grid(row=1, column=1, padx=5, pady=5)

time_label = ttk.Label(entry_frame, text="Due Time:")
time_label.grid(row=1, column=2, padx=5, pady=5)

time_entry = ttk.Entry(entry_frame, width=10)
time_entry.grid(row=1, column=3, padx=5, pady=5)

button_frame = ttk.Frame(root)
button_frame.pack(pady=10)

add_button = ttk.Button(button_frame, text="Add Task", command=add_task)
add_button.grid(row=0, column=0, padx=5)

mark_button = ttk.Button(button_frame, text="Delete Selected", command=mark_task)
mark_button.grid(row=0, column=1, padx=5)

task_listbox = tk.Listbox(root, width=60, height=15)
task_listbox.pack(pady=10)

update_task_list()

root.mainloop()
