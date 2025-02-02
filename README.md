# Task Management System
The Task Management System is designed to provide a simple and user-friendly interface for managing tasks. It allows users to add tasks, view lists of assigned and completed tasks separately, and perform various task management operations such as deleting, updating, and marking tasks as completed.

## Features:
<ul>
  <li>Add Tasks: Easily add new tasks to your to-do list.</li>
  <li>View Tasks: View lists of both assigned tasks and completed tasks separately for better organization.</li>
  <li>Delete Tasks: Remove tasks that are no longer needed.</li>
  <li>Update Tasks: Modify existing tasks to reflect changes in your plans.</li>
  <li>Mark as Completed: Mark tasks as completed to keep track of your progress.</li>
</ul>

## How to Use
### Clone the Repository
```bash
# 1. Clone the repository
git clone https://github.com/naveennokhwal/task-management-system.git

# 2. Enter the directory
cd task-management-system
```

### Set Up a Virtual Environment
```python
pip install venv  # Install venv

python -m venv env  # Create a virtual environment

./env/Scripts/Activate.ps1  # Activate the virtual environment

```

### Install Required Modules
```python
pip install flask
pip install flask_sqlalchemy  # Install SQLAlchemy for the dataset
```

### Create SQL Data
```flask shell
from app import db
db.create_all()
```
### Run the Application
Run app.py and click on the generated link. This will direct you to a website running locally.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
