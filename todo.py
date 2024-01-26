import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")

        #Task list
        self.tasks = []

        #Entry for new task
        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.pack(pady=10)

        #Buttons
        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=5)

        self.view_button = tk.Button(root, text="View Tasks", command=self.view_tasks)
        self.view_button.pack(pady=5)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            messagebox.showinfo("Success", f'Task "{task}" added successfully.')
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")


    def view_tasks(self):
        if not self.tasks:
            messagebox.showinfo("Info", "No tasks available.")
        else:
            task_list = "\n".join([f"{i + 1}. {task}" for i, task in enumerate(self.tasks)])
            messagebox.showinfo("Tasks", task_list)

def main():
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
        
