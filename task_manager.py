from datetime import datetime

from config import PRIORITIES, TASK_STATUSES, DATE_FORMAT
from storage import load_tasks, save_tasks
from utils import (
    get_text,
    get_date,
    get_choice,
    get_optional_date,
    get_optional_choice,
    days_until,
    current_timestamp
)


def generate_task_id(tasks):
    highest = 0

    for task in tasks:
        task_id = task.get("task_id", "")

        if task_id.startswith("TSK"):
            try:
                highest = max(highest, int(task_id[3:]))
            except ValueError:
                continue

    return f"TSK{highest + 1:04d}"


def get_task_status(task):
    return task.get("status", "Pending")


def add_task():
    tasks = load_tasks()

    print("\n--- Add Household Task ---")

    title = get_text("Task title: ")
    description = input("Description (optional): ").strip()
    assigned_to = get_text("Assign to: ")
    due_date = get_date("Due date (YYYY-MM-DD): ")
    priority = get_choice("Select priority: ", PRIORITIES)

    task = {
        "task_id": generate_task_id(tasks),
        "title": title,
        "description": description,
        "assigned_to": assigned_to,
        "due_date": due_date,
        "priority": priority,
        "status": "Pending",
        "created_at": current_timestamp(),
        "updated_at": current_timestamp(),
        "completed_at": None
    }

    tasks.append(task)
    save_tasks(tasks)

    print("\nTask added successfully!")
    print(f"Task ID: {task['task_id']}")
    print(f"Title: {task['title']}")


def display_task(task):
    status = get_task_status(task)
    remaining = days_until(task["due_date"])

    if status == "Completed":
        deadline_status = "Completed"
    elif remaining < 0:
        deadline_status = f"Overdue by {abs(remaining)} day(s)"
    elif remaining == 0:
        deadline_status = "Due today"
    else:
        deadline_status = f"{remaining} day(s) remaining"

    print("-" * 48)
    print(f"Task ID      : {task.get('task_id', '')}")
    print(f"Title        : {task.get('title', '')}")
    print(f"Description  : {task.get('description', '')}")
    print(f"Assigned To  : {task.get('assigned_to', '')}")
    print(f"Due Date     : {task.get('due_date', '')}")
    print(f"Priority     : {task.get('priority', 'Medium')}")
    print(f"Status       : {status}")
    print(f"Deadline     : {deadline_status}")
    print(f"Created At   : {task.get('created_at', '')}")
    print(f"Completed At : {task.get('completed_at') or 'Not completed'}")
    print("-" * 48)


def view_all_tasks():
    tasks = load_tasks()

    print("\n--- All Household Tasks ---")

    if not tasks:
        print("No tasks found.")
        return

    tasks.sort(
        key=lambda task: (
            task.get("status") == "Completed",
            task.get("due_date", "")
        )
    )

    for task in tasks:
        display_task(task)

    print(f"Total tasks: {len(tasks)}")


def search_tasks():
    tasks = load_tasks()

    if not tasks:
        print("No tasks available.")
        return

    keyword = input(
        "Search by task ID, title, description, or person: "
    ).strip().lower()

    if not keyword:
        print("Enter a search term.")
        return

    results = [
        task for task in tasks
        if keyword in task.get("task_id", "").lower()
        or keyword in task.get("title", "").lower()
        or keyword in task.get("description", "").lower()
        or keyword in task.get("assigned_to", "").lower()
    ]

    if not results:
        print("No matching tasks found.")
        return

    for task in results:
        display_task(task)


def find_task(tasks, task_id):
    return next(
        (
            task for task in tasks
            if task.get("task_id", "").upper() == task_id.upper()
        ),
        None
    )


def update_task_status():
    tasks = load_tasks()
    task_id = input("Enter task ID: ").strip().upper()

    task = find_task(tasks, task_id)

    if not task:
        print("Task not found.")
        return

    print(f"Current status: {task['status']}")

    new_status = get_choice(
        "Select new status: ",
        TASK_STATUSES
    )

    task["status"] = new_status
    task["updated_at"] = current_timestamp()

    if new_status == "Completed":
        if not task.get("completed_at"):
            task["completed_at"] = current_timestamp()
    else:
        task["completed_at"] = None

    save_tasks(tasks)
    print("Task status updated successfully.")


def edit_task():
    tasks = load_tasks()
    task_id = input("Enter task ID to edit: ").strip().upper()

    task = find_task(tasks, task_id)

    if not task:
        print("Task not found.")
        return

    print("Leave a field blank to keep its current value.")

    title = input(f"Title [{task['title']}]: ").strip()
    description = input(
        f"Description [{task.get('description', '')}]: "
    ).strip()
    assigned_to = input(
        f"Assigned to [{task['assigned_to']}]: "
    ).strip()

    if title:
        task["title"] = title

    if description:
        task["description"] = description

    if assigned_to:
        task["assigned_to"] = assigned_to

    task["due_date"] = get_optional_date(
        "Due date",
        task["due_date"]
    )

    task["priority"] = get_optional_choice(
        "priority",
        task.get("priority", "Medium"),
        PRIORITIES
    )

    task["status"] = get_optional_choice(
        "status",
        task.get("status", "Pending"),
        TASK_STATUSES
    )

    if task["status"] == "Completed":
        if not task.get("completed_at"):
            task["completed_at"] = current_timestamp()
    else:
        task["completed_at"] = None

    task["updated_at"] = current_timestamp()

    # Validate the date before saving.
    try:
        datetime.strptime(task["due_date"], DATE_FORMAT)
    except ValueError:
        print("Invalid due date. Changes were not saved.")
        return

    save_tasks(tasks)
    print("Task updated successfully.")


def delete_task():
    tasks = load_tasks()
    task_id = input("Enter task ID to delete: ").strip().upper()

    task = find_task(tasks, task_id)

    if not task:
        print("Task not found.")
        return

    display_task(task)

    confirm = input("Delete this task? (y/n): ").strip().lower()

    if confirm == "y":
        tasks.remove(task)
        save_tasks(tasks)
        print("Task deleted successfully.")
    else:
        print("Deletion cancelled.")


def view_overdue_tasks():
    tasks = load_tasks()

    overdue = [
        task for task in tasks
        if task.get("status") != "Completed"
        and days_until(task["due_date"]) < 0
    ]

    print("\n--- Overdue Tasks ---")

    if not overdue:
        print("There are no overdue tasks.")
        return

    for task in overdue:
        display_task(task)

    print(f"Total overdue tasks: {len(overdue)}")


def view_tasks_by_person():
    tasks = load_tasks()

    person = input("Enter family member's name: ").strip().lower()

    if not person:
        print("Enter a name.")
        return

    results = [
        task for task in tasks
        if person == task.get("assigned_to", "").lower()
    ]

    if not results:
        print("No tasks found for this person.")
        return

    print(f"\n--- Tasks assigned to {person.title()} ---")

    for task in results:
        display_task(task)


def view_tasks_by_priority():
    tasks = load_tasks()

    priority = get_choice("Select priority: ", PRIORITIES)

    results = [
        task for task in tasks
        if task.get("priority") == priority
    ]

    if not results:
        print(f"No {priority.lower()} priority tasks found.")
        return

    print(f"\n--- {priority} Priority Tasks ---")

    for task in results:
        display_task(task)
