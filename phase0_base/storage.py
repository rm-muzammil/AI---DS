import json

class Storage:
    def save(self, tasks):
        data = [{"title": t.title, "completed": t.completed} for t in tasks]
        with open("tasks.json", "w") as f:
            json.dump(data, f)

    def load(self):
        try:
            with open("tasks.json", "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return []