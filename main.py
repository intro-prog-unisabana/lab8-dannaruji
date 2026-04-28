"""Laboratorio 8 - CLI del gestor de tareas."""

import sys
from todo_manager import read_todo_file, write_todo_file
try:
    if len(sys.argv) < 2:
        raise IndexError("Insufficient arguments provided!")

    if sys.argv[1] == "--help":
        print("""Usage: python main.py <file_path> <command> [arguments]...

Commands:
  add "task"    - Add a task to the list.
  remove "task" - Remove a task from the list.
  view          - Display all tasks.

Examples:
  python main.py tasks.txt add "Buy groceries"
  python main.py tasks.txt remove "Do laundry"
  python main.py tasks.txt view
  python main.py tasks.txt add "Call mom" remove "Take out trash" view""")
    else:
        file_path = sys.argv[1]
        tasks = read_todo_file(file_path)
        i = 2

        while i < len(sys.argv):
            comando = sys.argv[i]
            if comando == "add":
                if i + 1 >= len(sys.argv):
                    raise IndexError('Task description required for "add".')

                tarea = sys.argv[i + 1]
                tasks.append(tarea)
                print(f'Task "{tarea}" added.')
                i = i + 2

            elif comando == "remove":
                if i + 1 >= len(sys.argv):
                    raise IndexError('Task description required for "remove".')

                tarea = sys.argv[i + 1]

                if tarea in tasks:
                    tasks.remove(tarea)
                    print(f'Task "{tarea}" removed.')
                else:
                    print(f'Task "{tarea}" not found.')

                i = i + 2

            elif comando == "view":
                print("Tasks:")
                for t in tasks:
                    print(t)
                i = i + 1

            else:
                raise ValueError("Command not found!")

        write_todo_file(file_path, tasks)

except IndexError as e:
    print(e)

except ValueError as e:
    print(e)