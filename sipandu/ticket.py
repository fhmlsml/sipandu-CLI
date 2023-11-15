import typer

sipandu = typer.Typer()


@sipandu.command()
def claim(ticket_id: str):
    print(f"Claimed Ticket: {ticket_id}")


@sipandu.command()
def pending(ticket_id: str):
    print(f"Pending Ticket: {ticket_id}")