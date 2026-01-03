from repositories.task_repository import TaskRepository
from services.task_service import TaskService



def main():
    """
    Simulação simples do sistema de gerenciamento de tarefas.
    """

    repository = TaskRepository()
    service = TaskService(repository)

    # Criação de tarefas
    service.create_task(
        title="Implementar CRUD de tarefas",
        description="Criar funcionalidades básicas do sistema",
        priority="Alta"
    )

    service.create_task(
        title="Configurar GitHub Actions",
        description="Adicionar pipeline de testes automatizados",
        priority="Média"
    )

    # Listagem de tarefas
    print("Tarefas cadastradas:")
    for task in service.list_tasks():
        print(f"- [{task.status}] {task.title} (Prioridade: {task.priority})")

    # Conclusão de uma tarefa
    service.complete_task(1)

    print("\nApós concluir a primeira tarefa:")
    for task in service.list_tasks():
        print(f"- [{task.status}] {task.title}")


if __name__ == "__main__":
    main()
