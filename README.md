# Household Chore Scheduler

A beginner-friendly Python application for organizing household chores, assigning responsibilities to family members, tracking due dates, and monitoring task completion.

## Features

- Add, view, edit, and delete household tasks
- Assign tasks to family members
- Set due dates and priorities
- Track Pending, In Progress, and Completed tasks
- Identify overdue tasks
- Search tasks by title, description, ID, or assigned person
- Filter tasks by family member or priority
- View tasks due within the next seven days
- Generate summary and completion reports
- Store data in JSON format

## Technologies Used

- Python 3
- JSON
- datetime
- collections

## Project Structure

```text
Household-Chore-Scheduler/
├── main.py
├── config.py
├── storage.py
├── utils.py
├── task_manager.py
├── report_manager.py
├── requirements.txt
├── .gitignore
├── README.md
└── data/
    └── tasks.json
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Household-Chore-Scheduler.git
```

### 2. Open the project folder

```bash
cd Household-Chore-Scheduler
```

### 3. Run the application

```bash
python main.py
```

No external packages are required.

## Date Format

Enter dates in `YYYY-MM-DD` format.

Example: `2026-11-15`

## How to Use

1. Add a household task.
2. Assign it to a family member.
3. Set its due date and priority.
4. Update the task status as work progresses.
5. View overdue tasks and upcoming deadlines.
6. Review reports to monitor household responsibilities.

## Learning Outcomes

- Python functions and modules
- Lists and dictionaries
- JSON file handling
- Date validation and calculations
- Searching, sorting, and filtering
- Exception handling
- Command-line application development

## Future Improvements

- Add a graphical user interface
- Add recurring chores
- Add task reminders
- Export reports to CSV
- Integrate SQLite or MySQL
- Add individual user accounts

## Author

Python Project Challenge

## License

Free to use for educational and personal learning purposes.
