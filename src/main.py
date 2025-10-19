from random import randint
from dataclasses import dataclass
from typing import Annotated
from fastapi import FastAPI
from pydantic import AfterValidator, BaseModel, StrictInt


def bound_int_validator(lower_bound: int, upper_bound: int):
    def validator(v: int):
        if v > upper_bound or v < lower_bound:
            raise ValueError(f"{v} is not between {lower_bound} and {upper_bound}")
        return v

    return validator


class Dice(BaseModel):
    count: Annotated[StrictInt, AfterValidator(bound_int_validator(1, 100))]
    sides: Annotated[StrictInt, AfterValidator(bound_int_validator(1, 1000))]
    modifier: StrictInt


class RollRequest(BaseModel):
    count: Annotated[StrictInt, AfterValidator(bound_int_validator(1, 100))]
    dice: list[Dice]


@dataclass
class Roll:
    count: int
    sides: int
    modifier: int
    rolls: list[int]
    total: int


@dataclass
class Step:
    rolls: list[Roll]
    total: int


@dataclass
class RollResponse:
    step: list[Step]


app = FastAPI()


@app.post("/")
def roll_dice(rollRequest: RollRequest):
    payload = RollResponse(step=[])

    for _ in range(0, rollRequest.count):
        step = Step(rolls=[], total=0)
        for dice in rollRequest.dice:
            rolls = []
            rollsTotal = dice.modifier
            for _ in range(0, dice.count):
                roll = randint(1, dice.sides)
                rolls.append(roll)
                rollsTotal += roll
            step.total += rollsTotal
            step.rolls.append(
                Roll(
                    count=dice.count,
                    sides=dice.sides,
                    modifier=dice.modifier,
                    rolls=rolls,
                    total=rollsTotal,
                )
            )
        payload.step.append(step)

    return payload
