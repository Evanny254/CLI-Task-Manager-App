# CLI Task Manager App
The Task Manager CLI Application is a command-line interface tool that allows users to manage tasks associated with specific users. Users can add tasks, delete tasks, view tasks, and update task information using simple commands in the terminal.

## Installation
1. Clone the repository:
https://github.com/Evanny254/CLI-Task-Manager.git

cd task-manager-cli

2. Install dependencies:
pip install -r requirements.txt

## Usage
1. Ensure the SQLite database is set up:
python database.py
2. Run the Task Manager CLI Application:
python main.py

3. Follow the on-screen instructions to perform various tasks, such as adding, deleting, viewing, and updating tasks.

## Commands
The application supports the following commands:
1. Add Task: Add a new task associated with a user.
2. Delete Task: Delete a task by providing its ID.
3. View Task: View tasks associated with a specific user.
4. Update Task: Update task details, including the task title and category.

## Example
=======Task Manager Application=======
1. Add Task
2. Delete Task
3. View Task
4. Update Task
5. Quit
Enter your choice: 1

Enter username: Evans
Enter task title: Complete project
Enter category (optional): Work
Task 'Complete project' added successfully for user Evans.

## Database
The application uses an SQLite database to store user, task, and category information. The database schema is defined in models.py.

## Contributing
If you'd like to contribute to the development of this application, feel free to open an issue or submit a pull request.