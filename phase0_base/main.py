from task_manager import TaskManager

manager = TaskManager()


manager.save_tasks()  # Save tasks to storage

manager.show_tasks()

manager.complete_task(0)
manager.save_tasks()  # Save updated tasks to storage
print("\nAfter completion:")
manager.load_tasks()  # Load tasks from storage to reflect changes
manager.show_tasks()