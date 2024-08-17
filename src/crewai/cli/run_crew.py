import subprocess

import click
from security import safe_command


def run_crew() -> None:
    """
    Run the crew by running a command in the Poetry environment.
    """
    command = ["poetry", "run", "run_crew"]

    try:
        result = safe_command.run(subprocess.run, command, capture_output=False, text=True, check=True)

        if result.stderr:
            click.echo(result.stderr, err=True)

    except subprocess.CalledProcessError as e:
        click.echo(f"An error occurred while running the crew: {e}", err=True)
        click.echo(e.output, err=True)

    except Exception as e:
        click.echo(f"An unexpected error occurred: {e}", err=True)
