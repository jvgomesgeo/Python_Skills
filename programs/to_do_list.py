tasks = {"Exercitar Programas": {'status': True},
         "Estudar OOP": {'status': True},
         "Estudar Django": {'status': False},
         "Estudar Tecnologia Git": {'status': False},
         "Estudar HTML": {'status': True},
         "Estudar JavaScript": {'status': False},
         "Estudar Banco de Dados": {'status': False}
}

options = [
    '1. Adicionar Tarefa',
    '2. Concluir Tarefa',
    '3. Ver tarefas pendentes'
    'q. Sair'
]

def add_task():
    while True:
        try:
            new_task = input("Enter you new task (Q to quit): ")
            if "q" in new_task.lower():
                break
            status_task = bool(input("Enter the status of your task (True: concluída, False: não concluida): "))
            
            if status_task != True or status_task != False:
                print("Only True or False")
            elif "q" in status_task.lower():
                break
            else:
                tasks[new_task] = {'status': status_task}
        except ValueError:
            print(f"Invalid Input !")
        
        print()
        print("-" * 15)
        for key, value in tasks.items():
            print(f"Task: {key}, Status: {list(value.values())[0]}")


def select_task():
    while True:
        try:
            increment = 1
            for key in tasks.keys():
                print(increment, key)
                increment += 1
                
            status_select = input("Select a task to get status (Q to quit): ")
            if "q" in status_select.lower():
                break
            elif not status_select.isdigit():
                print("Choose a number !")
            
            elif status_select.isdigit(): 
                status_select = int(status_select)
                print(f'The status of {list(tasks.keys())[status_select -1]} Task is {list(tasks.values())[status_select -1]['status']}')        
        except ValueError:
            print("Invalid input !")
                

def remove_task():
    while True:
        try:
            increment = 1
            for key in tasks.keys():
                print(increment, key)
                increment += 1          
            task_rem = input("Select a task to remove (Q to quit): ")    
            if 'q' in task_rem.lower():
                break
            elif not task_rem.isdigit():
                print("Choose a number")      
            elif task_rem.isdigit():
                task_rem = int(task_rem)
                tasks.pop(list(tasks.keys())[task_rem -1])
                print(f"Task {list(tasks.keys())[task_rem -1]} REMOVIDA ")
                
                for key, value in tasks.items():
                    print("--- Lefted Tasks ---")
                    print(f"Tasks: {key}, Status {list(value.values())[0]}")
                    print("---------------")
                    
        except ValueError:
            print("Invalid Input")
        
        
def main():
    while True:
        for opt in options:
            print(opt)
                
        user_input = input("Choose an option: ")
        if user_input == "1":
            add_task()
        elif user_input == "2":
            select_task
        elif user_input == "3":
            remove_task()


if __name__ == "__main__":
    main()