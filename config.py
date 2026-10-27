from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
TASKS_FILE = DATA_DIR / "tasks.json"

PRIORITIES = ["Low", "Medium", "High"]
TASK_STATUSES = ["Pending", "In Progress", "Completed"]
DATE_FORMAT = "%Y-%m-%d"
