import utils
import time

now = time.strftime('%b %d, %Y %H:%M:%S')
print("It is", now)
while True:
    user_action = input("Type add, show, edit, complete, or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:] + '\n'
        todos = utils.get_todos()
        todos.append(todo)
        utils.write_todos(todos)
    elif user_action.startswith('show'):
        todos = utils.get_todos()
        for index, item in enumerate(todos):
            item = item.strip('\n')
            print(f"{index + 1}. {item}")
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            index = number - 1
            todos = utils.get_todos()
            changing_task = todos[index].strip('\n')
            todos[index] = input(f"Enter the new todo to replace ({changing_task}): ") + '\n'
            utils.write_todos(todos)
        except IndexError:
            print(f"There is no item with number ({number}). Please try again.")
        except ValueError:
            print("Invalid command. Please try again.")
    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])
            todos = utils.get_todos()
            todo_to_remove = todos.pop(number - 1).strip('\n')
            utils.write_todos(todos)
            print(f"Todo ({todo_to_remove}) was removed from the list.")
        except IndexError:
            print(f"There is no item with number ({number}). Please try again.")
        except ValueError:
            print("Invalid command. Please try again.")
    elif user_action.startswith('exit'):
        break
    else:
        print("Unknown command. Please try again.")

print("Bye!")
