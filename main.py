from functs import *

def main ():
    while True:
        print('\n Administrador de tareas')
        print('1. Añadir tarea.')
        print('2. Ver tareas.')
        print('3. Eliminar tarea.')
        print('4. Marcar completa una tarea.')
        print('5. Salir.')

        choice = input('Elige un numero: ')
        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            remove_task()
        elif choice == '4':
            complete_task()
        elif choice == '5':
            break
        else: 
            print('Opcion invalida. Intentelo nuevamente.')            

if __name__ == '__main__':
    main()