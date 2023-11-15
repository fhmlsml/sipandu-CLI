import typer

sipandu = typer.Typer()

@sipandu.command()
def create(task: str):
    print(f"Creating Task: {task}")


@sipandu.command()
def pending(task_id: str):
    print(f"Pending Task: {task_id}")


@sipandu.command()
def close(task_id: str):
    print(f"Close Task: {task_id}")