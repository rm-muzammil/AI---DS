from task import Task
from storage import Storage

class TaskManager:
    def __init__(self):
        self.tasks = []
        self.storage = Storage()  # ✅ composition
        
    def save_tasks(self):
        self.storage.save(self.tasks)
        
    def load_tasks(self):
        data = self.storage.load()
        self.tasks = [Task(d["title"]) for d in data]
        for task, d in zip(self.tasks, data):
            if d["completed"]:
                task.mark_complete()

    def add_task(self, title):
        task = Task(title)
        self.tasks.append(task)

    def show_tasks(self):
        for i, task in enumerate(self.tasks):
            print(f"{i}: {task}")

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_complete()