from collections import Counter
from config import PRIORITIES
from storage import load_tasks
from utils import days_until


def task_summary():
    tasks = load_tasks()

    total = len(tasks)
    completed = sum(
        1 for task in tasks
        if task.get("status") == "Completed"
    )
    pending = sum(
        1 for task in tasks
        if task.get("status") == "Pending"
    )
    in_progress = sum(
        1 for task in tasks
        if task.get("status") == "In Progress"
    )
    overdue = sum(
        1 for task in tasks
        if task.get("status") != "Completed"
        and days_until(task["due_date"]) < 0
    )

    print("\n========== TASK SUMMARY ==========")
    print(f"Total tasks    : {total}")
    print(f"Pending        : {pending}")
    print(f"In Progress    : {in_progress}")
    print(f"Completed      : {completed}")
    print(f"Overdue        : {overdue}")

    if total:
        print(f"Completion rate: {completed / total * 100:.1f}%")

    print("=" * 35)


def priority_report():
    tasks = load_tasks()

    if not tasks:
        print("No tasks available.")
        return

    counts = Counter(task.get("priority", "Medium") for task in tasks)

    print("\n--- Tasks by Priority ---")

    for priority in PRIORITIES:
        print(f"{priority}: {counts.get(priority, 0)}")


def member_report():
    tasks = load_tasks()

    if not tasks:
        print("No tasks available.")
        return

    members = {}

    for task in tasks:
        person = task.get("assigned_to", "Unassigned")
        members.setdefault(person, {"total": 0, "completed": 0})
        members[person]["total"] += 1

        if task.get("status") == "Completed":
            members[person]["completed"] += 1

    print("\n--- Family Member Task Report ---")

    for person, data in sorted(members.items()):
        print(
            f"{person}: {data['completed']}/{data['total']} "
            "tasks completed"
        )


def upcoming_tasks_report():
    tasks = load_tasks()

    upcoming = [
        task for task in tasks
        if task.get("status") != "Completed"
        and 0 <= days_until(task["due_date"]) <= 7
    ]

    upcoming.sort(key=lambda task: task["due_date"])

    print("\n--- Tasks Due Within 7 Days ---")

    if not upcoming:
        print("No tasks due within the next 7 days.")
        return

    for task in upcoming:
        remaining = days_until(task["due_date"])
        print(
            f"{task['task_id']} | {task['title']} | "
            f"Assigned to: {task['assigned_to']} | "
            f"Due: {task['due_date']} | "
            f"{remaining} day(s) remaining"
        )
