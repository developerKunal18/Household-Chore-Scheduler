import json
from config import DATA_DIR, TASKS_FILE


def initialize_storage():
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    if not TASKS_FILE.exists():
        with TASKS_FILE.open("w", encoding="utf-8") as file:
            json.dump([], file, indent=4)


def load_tasks():
    initialize_storage()

    try:
        with TASKS_FILE.open("r", encoding="utf-8") as file:
            tasks = json.load(file)

        if not isinstance(tasks, list):
            print("Warning: Task data must be a JSON list.")
            return []

        return tasks

    except (json.JSONDecodeError, OSError) as error:
        print(f"Could not load tasks: {error}")
        return []


def save_tasks(tasks):
    initialize_storage()

    with TASKS_FILE.open("w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=4, ensure_ascii=False)
