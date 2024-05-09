from tkinter import *
import tkinter as tk
from datetime import datetime

def update_time_label():
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    time_label.config(text=current_time)
    root.after(1000, update_time_label)

def save_task():
    task_text = task_entry.get()
    if task_text:
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        task_with_time = f"{current_time} - {task_text}\n"
        with open("todo.txt", "a") as file:
            file.write(task_with_time)
        task_entry.delete(0, END)  # Clear the entry after saving

# GUI setup
root = Tk()
root.title('TODO LIST')
root.geometry("700x500+250+180")
root.configure(bg="#2f4155")

Label(root, text="MY TODO LIST", bg='#2d4155', fg='white', font="arial 25 bold").place(x=100, y=20)

time_label = tk.Label(root, font=('Helvetica', 18), bg="#2f4155", fg="white")
time_label.place(x=200, y=400)  

task_entry = Entry(root, font=('Helvetica', 14))
task_entry.place(x=100, y=100, width=500)

save_button = Button(root, text="Save Task", command=save_task, font=('Helvetica', 14), bg='#4CAF50', fg='white')
save_button.place(x=300, y=150)

update_time_label()
root.mainloop()
