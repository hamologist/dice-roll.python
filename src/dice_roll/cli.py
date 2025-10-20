import sys
import json
import typer
from typing_extensions import Annotated

from dice_roll import roller

app = typer.Typer()

@app.command()
def roll_from_input(input_file: Annotated[
        typer.FileText,
        typer.Argument(default_factory=lambda: sys.stdin, show_default="sys.stdin")
    ]
):
    roll_request: roller.RollRequest

    try:
        request = json.loads(input_file.read().strip())
    except json.JSONDecodeError:
        print('Malformed JSON payload provided')
        return

    print(f"You sent me this: {request}")

def main():
    typer.run(roll_from_input)
