import sys
import json
import dataclasses
from typing_extensions import Annotated

from pydantic import ValidationError
import typer

from dice_roll import roller

app = typer.Typer()


@app.command()
def roll_from_input(
    input_file: Annotated[
        typer.FileText,
        typer.Argument(default_factory=lambda: sys.stdin, show_default="sys.stdin"),
    ],
):
    """
    Attempts to roll a provided set of dice based on JSON input from file or STDIN.
    """
    request: roller.RollRequest

    try:
        request = roller.RollRequest(**json.loads(input_file.read().strip()))
    except json.JSONDecodeError:
        print("Malformed JSON payload provided")
        return
    except ValidationError as err:
        print("Invalid JSON payload provided")
        print(err.json(indent=2))
        return

    print(json.dumps(dataclasses.asdict(roller.roll_dice(request)), indent=2))


def main():
    typer.run(roll_from_input)
