from database import session
from models import User, Task, Category

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
            break
        else:
            print("Invalid choice. Please choose a valid option.")

def print_menu():
    print("=======Task Manager Application=======")
    print("1. Add Task")
    print("2. Delete Task")
    print("3. View Task")
    print("4. Update Task")
    print("5. Quit")

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
    task_id = int(input("Enter task ID to delete: "))
    task = session.query(Task).get(task_id)

    if task:
        session.delete(task)
        session.commit()
        print(f"Task '{task.title}' deleted successfully.")
    else:
        print(f"Task with ID {task_id} not found.")

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
    task_id = int(input("Enter task ID to update: "))
    task = session.query(Task).get(task_id)

    if task:
        new_title = input("Enter new task title (press Enter to keep the existing title): ")
        new_category_name = input("Enter new category (optional, press Enter to keep the existing category): ")

        if new_category_name:
            new_category = session.query(Category).filter_by(name=new_category_name).first()
            if not new_category:
                new_category = Category(name=new_category_name)
                session.add(new_category)
                session.commit()
            task.category = new_category

        task.title = new_title
        session.commit()
        print(f"Task '{task.title}' updated successfully.")
    else:
        print(f"Task with ID {task_id} not found.")

if __name__ == '__main__':
    main()