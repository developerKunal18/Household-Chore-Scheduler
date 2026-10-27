from storage import initialize_storage
from task_manager import (
    add_task,
    view_all_tasks,
    search_tasks,
    edit_task,
    delete_task,
    update_task_status,
    view_overdue_tasks,
    view_tasks_by_person,
    view_tasks_by_priority
)
from report_manager import (
    task_summary,
    priority_report,
    member_report,
    upcoming_tasks_report
)
from utils import pause


def show_menu():
    print("\n" + "=" * 44)
    print("        HOUSEHOLD CHORE SCHEDULER")
    print("=" * 44)
    print("1. Add Task")
    print("2. View All Tasks")
    print("3. Search Tasks")
    print("4. Edit Task")
    print("5. Delete Task")
    print("6. Update Task Status")
    print("7. View Overdue Tasks")
    print("8. View Tasks by Family Member")
    print("9. View Tasks by Priority")
    print("10. Task Summary Report")
    print("11. Priority Report")
    print("12. Family Member Report")
    print("13. Tasks Due Within 7 Days")
    print("0. Exit")
    print("=" * 44)


def main():
    initialize_storage()

    actions = {
        "1": add_task,
        "2": view_all_tasks,
        "3": search_tasks,
        "4": edit_task,
        "5": delete_task,
        "6": update_task_status,
        "7": view_overdue_tasks,
        "8": view_tasks_by_person,
        "9": view_tasks_by_priority,
        "10": task_summary,
        "11": priority_report,
        "12": member_report,
        "13": upcoming_tasks_report
    }

    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "0":
            print("Thank you for using Household Chore Scheduler!")
            break

        action = actions.get(choice)

        if action:
            try:
                action()
            except (OSError, ValueError, KeyError, TypeError) as error:
                print(f"An error occurred: {error}")

            pause()
        else:
            print("Invalid choice. Select a number from 0 to 13.")
            pause()


if __name__ == "__main__":
    main()
