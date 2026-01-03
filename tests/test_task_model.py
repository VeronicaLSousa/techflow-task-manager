from src.models.task import Task
from datetime import datetime


def test_task_creation():
    task = Task(
        id=1,
        title="Testar modelo",
        description="Teste de criação da tarefa",
        priority="Alta"
    )

    assert task.id == 1
    assert task.title == "Testar modelo"
    assert task.status == "A Fazer"
    assert isinstance(task.created_at, datetime)
    assert task.completed_at is None


def test_task_complete():
    task = Task(
        id=1,
        title="Finalizar tarefa",
        description="Teste de conclusão",
        priority="Média"
    )

    task.complete()

    assert task.status == "Concluído"
    assert task.completed_at is not None
