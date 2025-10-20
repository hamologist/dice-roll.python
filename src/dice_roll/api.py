import os
import uvicorn
from fastapi import FastAPI

from dice_roll import roller


app = FastAPI()


@app.post("/")
def roll_dice(roll_request: roller.RollRequest):
    return roller.roll_dice(roll_request)

def main():
    host = os.environ.get('DICE_ROLL_HOST', '0.0.0.0')
    port = int(os.environ.get('DICE_ROLL_PORT', 8000))

    uvicorn.run(app, host=host, port=port)
