from tkinter import *
from tkinter import messagebox

App = Tk()
App.geometry("300x400")
App.title("To-Do List App")

tasks = []

def add_task():
    task = task_entry.get()
    if task.strip() == "":
        messagebox.showinfo("Info", "Task cannot be blank!")
    else:
        tasks.append(task)
        update_tasks()
        task_entry.delete(0, END)

def remove_task():
    try:
        selected_task = task_listbox.get(ACTIVE)
        tasks.remove(selected_task)
        update_tasks()
    except:
        messagebox.showwarning("WARNING", "No task selected to remove!")

def clear_tasks():
    if messagebox.askyesno("Confirm", "Are you sure you want to clear all tasks?"):
        tasks.clear()
        update_tasks()

def update_tasks():
    task_listbox.delete(0, END)
    for task in tasks:
        task_listbox.insert(END, task)

def quit_app():
    App.destroy()

Label(App, text="To-Do List App", font=("Arial", 12)).pack()

frame = Frame(App)
frame.pack(pady=10)

task_entry = Entry(frame, width=20)
task_entry.pack(side=LEFT, padx=5)

add_btn = Button(frame, text="Add Task", command=add_task)
add_btn.pack(side=LEFT)

task_listbox = Listbox(App, width=30, height=10)
task_listbox.pack(pady=10)

remove_btn = Button(App, text="Remove Task", command=remove_task)
remove_btn.pack(pady=5)

clear_btn = Button(App, text="Clear All", command=clear_tasks)
clear_btn.pack(pady=5)

quit_btn = Button(App, text="Quit", command=quit_app)
quit_btn.pack(pady=10)

App.mainloop()