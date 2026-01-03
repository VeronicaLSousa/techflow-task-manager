import pytest
from src.repositories.task_repository import TaskRepository
from src.services.task_service import TaskService


def setup_service():
    repository = TaskRepository()
    return TaskService(repository)


def test_create_task_success():
    service = setup_service()

    task = service.create_task(
        title="Criar tarefa",
        description="Teste de criação",
        priority="Alta"
    )

    assert task.id == 1
    assert task.title == "Criar tarefa"
    assert task.priority == "Alta"


def test_create_task_without_title():
    service = setup_service()

    with pytest.raises(ValueError):
        service.create_task(
            title="",
            description="Sem título",
            priority="Baixa"
        )


def test_create_task_invalid_priority():
    service = setup_service()

    with pytest.raises(ValueError):
        service.create_task(
            title="Prioridade inválida",
            description="Erro esperado",
            priority="Urgente"
        )


def test_list_tasks():
    service = setup_service()

    service.create_task("Tarefa 1", "Desc 1", "Alta")
    service.create_task("Tarefa 2", "Desc 2", "Média")

    tasks = service.list_tasks()

    assert len(tasks) == 2


def test_complete_task():
    service = setup_service()

    task = service.create_task("Finalizar", "Completar tarefa", "Baixa")
    completed_task = service.complete_task(task.id)

    assert completed_task.status == "Concluído"
    assert completed_task.completed_at is not None


def test_complete_task_not_found():
    service = setup_service()

    with pytest.raises(ValueError):
        service.complete_task(999)


def test_delete_task():
    service = setup_service()

    task = service.create_task("Excluir", "Remover tarefa", "Média")
    result = service.delete_task(task.id)

    assert result is True
    assert len(service.list_tasks()) == 0
