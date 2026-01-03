from typing import List
from src.models.task import Task
from src.repositories.task_repository import TaskRepository


class TaskService:
    """
    Serviço responsável pelas regras de negócio do sistema de tarefas.
    """

    def __init__(self, repository: TaskRepository):
        self.repository = repository

    def create_task(self, title: str, description: str, priority: str) -> Task:
        """
        Cria uma nova tarefa após validações básicas.
        """
        if not title:
            raise ValueError("O título da tarefa é obrigatório.")

        if priority not in ["Alta", "Média", "Baixa"]:
            raise ValueError("Prioridade inválida. Use: Alta, Média ou Baixa.")

        task = Task(
            id=0,  # será definido pelo repositório
            title=title,
            description=description,
            priority=priority
        )

        return self.repository.add(task)

    def list_tasks(self) -> List[Task]:
        """
        Retorna todas as tarefas.
        """
        return self.repository.get_all()

    def complete_task(self, task_id: int) -> Task:
        """
        Marca uma tarefa como concluída.
        """
        task = self.repository.get_by_id(task_id)
        if not task:
            raise ValueError("Tarefa não encontrada.")

        task.complete()
        return task

    def delete_task(self, task_id: int) -> bool:
        """
        Remove uma tarefa do sistema.
        """
        return self.repository.delete(task_id)
