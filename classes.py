# TODO: history class that saves every change inside a task list

class Task:
    """A class used to represent a task.
    
    Requires a description parameter to be instantiated.

    Attributes
    ----------
    __state : bool
        A bool that represent the state of the task.
    _description : str
        A string that holds the task description.

    Methods
    -------
    set_completed()
        Mark the task as completed.
    """
    def __init__(self, description):
        """
        Parameters
        ----------
        __state : bool
            A bool that represent the state of the task. Instantiated as False.
        _description : str
            A string that holds the task description.
        """
        self._state = False
        self._description = description

    def set_completed(self):
        """Mark the task as completed.

        Change the __state attribute to True.
        """
        self._state = True

    def __str__(self) -> str:
        symbol = '[x]' if self._state else '[ ]'
        description:str = self._description
        string = f"{symbol} {description.capitalize()}."

        return string

class TaskList:
    """A class that represents a task list.

    Attributes
    ----------
    _task : list
        A list that contains all task objects.
    name : str
        A string to represent the task list name.

    Methods
    -------
    create_task(description)
        Create a new task with a given description.
    rm_task(task)
        Remove the refered task from the task list.
    end_task(completed_task)
        Search for the refered completed task. If exists, marks as completed.
    """
    
    def __init__(self, name:str):
        """
        Parameters
        ----------   
        name : str
            A string to represent the task list name.
        """
        self.name = name
        self._tasks = []

    @property
    def tasks(self):
        string = f"** {self.name} **"
        if len(self._tasks) == 0:
            string += "\n\tNenhuma tarefa foi adicionada..."
        else:
            for code, state, task in  self._tasks:
                string += f"\n\t•[{code}] {state} {task}"

        return string

    def create_task(self, description:str):
        """Create a new task with a given description.

        Parameters
        ----------
        description : str
            A short descriptions of the new task.
        """
        self._tasks.append(Task(description))
    
    def rm_task(self, task:Task):
        """Remove the refered task from the task list.
        
        If the referd task is not in the task list returns a error message.

        Parameters
        ----------
        task : Task
            The task to be removed.
        """
        try:
            self._tasks.remove(task)
        except ValueError:
            print("Tarefa não encontrada.")

    def end_task(self, completed_task:Task):
        """Mark a task as completed.

        Search for the refered completed task. If it exists, calls for the task
        set_completed method, else returns an error message.
        
        Parameters
        ----------
        completed_task : Task
            The task to be marked as completed.
        """
        for task in self._tasks:
            if task == completed_task:
                task.set_completed()
                break  
        else:
            print("Tarefa não encontrada.")        
