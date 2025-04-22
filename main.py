# todos = []

while True:
    # Get user input and remove space character from it
    user_action = input("Type add, show, edit or exit:")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo:") + "\n"
            
            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            todos.append(todo)

            with open('todos.txt', 'w') as file:
                file.writelines(todos)
        case 'show':
            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            # list comprehension 
            new_todos = [item.strip("\n") for item in todos] 
            
            for index, item in enumerate(new_todos):
                row = f"{index+1}-{item}"
                print(row)
        case 'edit':
            number = int(input("Number of the todo to edit:"))
            number = number - 1

            # example for context manager
            with open('todos.txt', 'r') as file: 
                todos = file.readlines()
            print("Here is todo list", todos)
            
            new_todo = input("Enter new todo:")
            todos[number] = new_todo + "\n"

            with open('todos.txt', 'w') as file:
                todos = file.writelines(todos)
        case 'complete':
            number = int(input("Number of the todo to complete"))
            
            with open('todos.txt', 'r') as file: 
                todos = file.readlines()
            todo_to_remove = todos[number-1].strip("\n")
            todos.pop(number - 1)

            with open('todos.txt', 'w') as file:
                todos = file.writelines(todos)

            message = f"Todo {todo_to_remove} was removed from the list"
            print(message)
        case 'exit':
            break

print("Bye!")