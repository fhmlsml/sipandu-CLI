import typer

from typing import Optional, Any
from typing_extensions import Annotated
from rich.prompt import Prompt

try:
    from . import task, ticket, utils
except ImportError:
    import task, ticket, utils


sipandu = typer.Typer()

sipandu.add_typer(task.sipandu, name="task")
sipandu.add_typer(ticket.sipandu, name="ticket")

handler = utils.SipanduHandler()

@sipandu.command()
def login(
    user_email: Annotated[str, typer.Option(
        prompt="Email: "
    )],
    user_password: Annotated[str, typer.Option(
        prompt="Password Sipandu: ",
        confirmation_prompt=True,
        hide_input=True
    )]):

    user_login = handler.login(user_email=user_email, user_password=user_password)
    return user_login


if __name__ == "__main__":
    sipandu()
