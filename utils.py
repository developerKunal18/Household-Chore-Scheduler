from datetime import date, datetime
from config import DATE_FORMAT, PRIORITIES, TASK_STATUSES


def get_text(prompt):
    while True:
        value = input(prompt).strip()

        if value:
            return value

        print("This field cannot be empty.")


def get_date(prompt):
    while True:
        value = input(prompt).strip()

        try:
            parsed = datetime.strptime(value, DATE_FORMAT).date()

            if parsed.strftime(DATE_FORMAT) != value:
                raise ValueError

            return value

        except ValueError:
            print("Enter a valid date in YYYY-MM-DD format.")


def get_optional_date(prompt, current_value):
    value = input(f"{prompt} [{current_value}]: ").strip()

    if not value:
        return current_value

    try:
        parsed = datetime.strptime(value, DATE_FORMAT).date()

        if parsed.strftime(DATE_FORMAT) != value:
            raise ValueError

        return value

    except ValueError:
        print("Invalid date. Keeping the previous date.")
        return current_value


def get_choice(prompt, options):
    print("\nAvailable options:")

    for number, option in enumerate(options, start=1):
        print(f"{number}. {option}")

    while True:
        value = input(prompt).strip()

        if value.isdigit():
            number = int(value)

            if 1 <= number <= len(options):
                return options[number - 1]

        print(f"Choose a number between 1 and {len(options)}.")


def get_optional_choice(prompt, current_value, options):
    print(f"Current value: {current_value}")
    change = input(f"Change {prompt}? (y/n): ").strip().lower()

    if change == "y":
        return get_choice(f"Select {prompt}: ", options)

    return current_value


def days_until(due_date):
    due = datetime.strptime(due_date, DATE_FORMAT).date()
    return (due - date.today()).days


def current_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def pause():
    input("\nPress Enter to continue...")
