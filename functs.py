import pandas as pd 

# Funcion para agregar tareas
def add_task():
    task = input("Describe la tarea: ")
    priority = input("Prioridad (Alta, Media, Baja): ")
    new_task = pd.DataFrame([[task, priority, 'Incompleto']], columns=['Tarea', 'Prioridad', 'Estado'])
    # Intentar leer y concatenar la nueva informacion en el archivo csv  
    try:
        tasks = pd.read_csv('tasks.csv')
        tasks = pd.concat([tasks, new_task], ignore_index=True)
    except FileNotFoundError:
        tasks = new_task
# Guarda el archivo actualizado
    tasks.to_csv('tasks.csv', index=False)
    print("Tarea añadida.")

# Funcion para ver las tareas
def view_tasks():
    #Intentar leer el archivo
    try:
        tasks = pd.read_csv('tasks.csv')
        print(tasks)
    except FileNotFoundError:
        print("No hay tareas para mostrar.")

# Funcion para remover una tarea.
def remove_task():
    try:
        tasks = pd.read_csv('tasks.csv')
        print(tasks)

        task_num = int(input("¿Qué tarea quieres eliminar? Ingresa el número: "))
        tasks = tasks.drop(index=task_num - 1).reset_index(drop=True)
        
        tasks.to_csv('tasks.csv', index=False)
        print("Tarea eliminada.")
    except FileNotFoundError:
        print("No hay tareas para eliminar.")
    except IndexError:
        print("Número de tarea inválido.")

# Funcion para completar una tarea
def complete_task():
    try:
        tasks = pd.read_csv('tasks.csv')
        print(tasks)

        task_num = int(input("¿Qué tarea quieres marcar como completada? Ingresa el número: "))
        tasks.at[task_num - 1, 'Estado'] = 'Completada'
        
        tasks.to_csv('tasks.csv', index=False)
        print("Tarea marcada como completada.")
    except FileNotFoundError:
        print("No hay tareas para completar.")
    except IndexError:
        print("Número de tarea inválido.")