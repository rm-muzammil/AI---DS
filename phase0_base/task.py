class Task:
    def __init__(self, title):
        self.title = title
        self.completed = False

    def mark_complete(self):
        self.completed = True

    def __str__(self):
        status = "✅" if self.completed else "❌"
        return f"{self.title} [{status}]"