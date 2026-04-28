"""Laboratorio 8 - Módulo de persistencia para lista de tareas."""

def read_todo_file(file_path):
    """Reads tasks from a file. Returns a list of tasks."""
    try:
        archivo = open(file_path, "r")
        lista = []

        for linea in archivo:
            lista.append(linea.strip())

        archivo.close()
        return lista

    except:
        print(f"File {file_path} not found! Returning an empty to-do list.")
        return []

def write_todo_file(file_path, tasks):
    archivo = open(file_path, "w")

    for tarea in tasks:
        archivo.write(tarea + "\n")

    archivo.close()