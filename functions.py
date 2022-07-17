from classes import TaskList, Task


# TODO: UNDO the last change to a task list
# TODO: REDO the last UNDO to a task list

def new_task_list(name:str=None):
    return TaskList(name)

def del_task_list(task_list: TaskList):
    del task_list
    print("A lista de tarefas foi apagada.")

def add_task(task_list:TaskList, new_task:Task):
    task_list.create_task(new_task)
    print("📝Tarefa criada!")

def del_task(task_list:TaskList, task:Task):
    task_list.rm_task(task)
    print("🗑Tarefa removida!")

def mark_task(task_list:TaskList, task:Task):
    task_list.complete(task)
    print("✔Tarefa finalizada!")


