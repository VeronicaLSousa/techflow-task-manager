from typing import List, Optional
from src.models.task import Task


class TaskRepository:
    """
    Repositório responsável por armazenar e recuperar tarefas.
    Utiliza armazenamento em memória para fins didáticos.
    """

    def __init__(self):
        self._tasks: List[Task] = []
        self._next_id = 1

    def add(self, task: Task) -> Task:
        """
        Adiciona uma nova tarefa ao repositório.
        """
        task.id = self._next_id
        self._next_id += 1
        self._tasks.append(task)
        return task

    def get_all(self) -> List[Task]:
        """
        Retorna todas as tarefas cadastradas.
        """
        return self._tasks

    def get_by_id(self, task_id: int) -> Optional[Task]:
        """
        Busca uma tarefa pelo ID.
        """
        for task in self._tasks:
            if task.id == task_id:
                return task
        return None

    def delete(self, task_id: int) -> bool:
        """
        Remove uma tarefa pelo ID.
        """
        task = self.get_by_id(task_id)
        if task:
            self._tasks.remove(task)
            return True
        return False
