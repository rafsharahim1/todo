import tkinter as tk
from tkinter import messagebox
import re

def add_task():

    task = task_entry.get()
    start_time = start_time_entry.get()
    end_time = end_time_entry.get()


    if not validate_time(start_time) or not validate_time(end_time):
        messagebox.showerror("Error", "Invalid time format. Please use HH:MM.")
        return

    task_with_time = f"{task} (from {start_time} to {end_time})"

    if task and start_time and end_time:
        task_listbox.insert(tk.END, task_with_time)
        task_entry.delete(0, tk.END)
        start_time_entry.delete(0, tk.END)
        end_time_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task and time range.")

def delete_task():
    # Function to delete a selected task
    try:
        index = task_listbox.curselection()[0]
        task_listbox.delete(index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def validate_time(time_str):

    pattern = re.compile(r'^\d{2}:\d{2}$')
    return bool(pattern.match(time_str))

if __name__ == "__main__":
    root = tk.Tk()
    root.title("To-Do List App")


    task_label = tk.Label(root, text="Enter task:")
    task_label.pack(pady=5)

    task_entry = tk.Entry(root, width=30)
    task_entry.pack()

    time_label = tk.Label(root, text="Enter time range (HH:MM - HH:MM):")
    time_label.pack(pady=5)

    time_frame = tk.Frame(root)
    time_frame.pack()

    start_time_label = tk.Label(time_frame, text="From:")
    start_time_label.pack(side=tk.LEFT)

    start_time_entry = tk.Entry(time_frame, width=10)
    start_time_entry.pack(side=tk.LEFT)

    end_time_label = tk.Label(time_frame, text="To:")
    end_time_label.pack(side=tk.LEFT)

    end_time_entry = tk.Entry(time_frame, width=10)
    end_time_entry.pack(side=tk.LEFT)

    task_listbox = tk.Listbox(root, height=10, width=50)
    task_listbox.pack(pady=10)


    add_button = tk.Button(root, text="Add Task", width=20, command=add_task)
    add_button.pack()

    delete_button = tk.Button(root, text="Delete Task", width=20, command=delete_task)
    delete_button.pack()

    root.mainloop()
