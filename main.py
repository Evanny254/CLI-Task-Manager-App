from lib.database import session
from lib.models import User, Task, Category

def main():
    while True:
        print_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            add_task()
        elif choice == '2':
            delete_task()
        elif choice == '3':
            view_task()
        elif choice == '4':
            update_task()
        elif choice == '5':
            list_tasks()  
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please choose a valid option.")

def print_menu():
    print("=======Task Manager Application=======")
    print("1. Add Task")
    print("2. Delete Task")
    print("3. View Task")
    print("4. Update Task")
    print("5. List Tasks")
    print("6. Quit")

def add_task():
    username = input("Enter username: ")
    user = session.query(User).filter_by(username=username).first()

    if not user:
        user = User(username=username)
        session.add(user)
        session.commit()

    title = input("Enter task title: ")
    category_name = input("Enter category (optional): ")

    category = None
    if category_name:
        category = session.query(Category).filter_by(name=category_name).first()
        if not category:
            category = Category(name=category_name)
            session.add(category)
            session.commit()

    task = Task(title=title, user=user, category=category)
    session.add(task)
    session.commit()
    print(f"Task '{title}' added successfully for user {username}.")

def delete_task():
    username = input("Enter your username: ")
    user = session.query(User).filter_by(username=username).first()

    if user:
        tasks = session.query(Task).filter_by(user=user).all()
        if tasks:
            print(f"Tasks for user '{username}':")
            for task in tasks:
                category_name = task.category.name if task.category else 'None'
                print(f"ID: {task.id}, Title: {task.title}, Category: {category_name}")

            task_id_to_delete = int(input("Enter the task ID to delete: "))
            task_to_delete = session.query(Task).filter_by(id=task_id_to_delete, user=user).first()

            if task_to_delete:
                # Check if the user has only one task
                other_tasks_for_user = session.query(Task).filter(
                    Task.user == user, Task.id != task_to_delete.id
                ).count()

                # Check if the category is associated with any other tasks
                if task_to_delete.category:
                    other_tasks_with_category = session.query(Task).filter(
                        Task.category == task_to_delete.category, Task.id != task_to_delete.id
                    ).count()

                    # Delete the category if there are no other tasks with this category
                    if other_tasks_with_category == 0:
                        session.delete(task_to_delete.category)

                # Delete the task
                session.delete(task_to_delete)

                # Check if the user has no other tasks, then delete the user
                if other_tasks_for_user == 0:
                    session.delete(user)

                session.commit()

                print(f"Task '{task_to_delete.title}' deleted successfully for user {username}.")
            else:
                print("Invalid task ID or the task does not belong to the specified user.")
        else:
            # No tasks found for the user, delete the user
            session.delete(user)
            session.commit()
            print(f"No tasks found for user '{username}'. User '{username}' deleted.")
    else:
        print(f"User '{username}' not found.")


def view_task():
    username = input("Enter username to view tasks: ")
    user = session.query(User).filter_by(username=username).first()

    if user:
        tasks = session.query(Task).filter_by(user=user).all()
        if tasks:
            print(f"Tasks for user '{username}':")
            for task in tasks:
                category_name = task.category.name if task.category else 'None'
                print(f"ID: {task.id}, Title: {task.title}, Category: {category_name}")
        else:
            print(f"No tasks found for user '{username}'.")
    else:
        print(f"User '{username}' not found.")

def update_task():
    username = input("Enter username to update tasks: ")
    user = session.query(User).filter_by(username=username).first()

    if user:
        tasks = session.query(Task).filter_by(user=user).all()

        if tasks:
            print(f"Tasks for user '{username}':")
            for task in tasks:
                category_name = task.category.name if task.category else 'None'
                print(f"ID: {task.id}, Title: {task.title}, Category: {category_name}")

            task_id_to_update = int(input("Enter the task ID to update: "))
            task_to_update = session.query(Task).filter_by(id=task_id_to_update, user=user).first()

            if task_to_update:
                new_title = input("Enter new task title (press Enter to keep the existing title): ")
                new_category_name = input("Enter new category (optional, press Enter to keep the existing category): ")

                if new_category_name:
                    new_category = session.query(Category).filter_by(name=new_category_name).first()
                    if not new_category:
                        new_category = Category(name=new_category_name)
                        session.add(new_category)
                        session.commit()
                    task_to_update.category = new_category

                task_to_update.title = new_title
                session.commit()
                print(f"Task '{task_to_update.title}' updated successfully.")
            else:
                print("Invalid task ID or the task does not belong to the specified user.")
        else:
            print(f"No tasks found for user '{username}'.")
    else:
        print(f"User '{username}' not found.")

def list_tasks():
    admin_username = "Socrates"
    admin_password = "Socrates@254"
    print("Admin Access Only")
    entered_username = input("Enter your username: ")
    entered_password = input("Enter your password: ")

    if entered_username == admin_username and entered_password == admin_password:
        tasks = session.query(Task, User).join(User).all()
        if tasks:
            print("List of all tasks:")
            for task, user in tasks:
                category_name = task.category.name if task.category else 'None'
                print(f"User: {user.username}, ID: {task.id}, Title: {task.title}, Category: {category_name} ")
        else:
            print("No tasks found.")
    else:
        print("Permission denied. Only admin can list all tasks.")

if __name__ == '__main__':
    main()