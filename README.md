# Dice Roll
**Dice Roll** is a simple Python package for simulating dice rolls with varying sides and counts.

## Installation
To install and start using dice-roll you'll first need [uv](https://docs.astral.sh/uv/) installed on your machine.
After that you can install both the API and CLI frontends using:
```bash
$ uv tool install git+https://github.com/hamologist/dice-roll.git@main
```

Likewise, you can uninstall the application using:
```bash
$ uv tool uninstall dice-roll
```

## Usage
Once the dice-roll frontends have been installed, you can start interfacing with both.
### CLI
A `dice-roll-cli` command will be intalled on your system.
Help can be pulled up using the help flag:
```bash
$ dice-roll-cli --help
```

The command takes a dice roll instruction using either JSON sent via STDIN or using a file on your local machine.
Here is an example of what using the tool looks like:
```bash
$ echo '{
    "dice": [
        {
            "count": 1,
            "sides": 20,
            "modifier": 1
        },
        {
            "count": 2,
            "sides": 4,
            "modifier": 2
        }
    ],
    "count": 1
}' | dice-roll-cli
```
The above will return a JSON string of the resulting roll like so:
```bash
{
  "step": [
    {
      "rolls": [
        {
          "count": 1,
          "sides": 20,
          "modifier": 1,
          "rolls": [
            19
          ],
          "total": 20
        },
        {
          "count": 2,
          "sides": 4,
          "modifier": 2,
          "rolls": [
            3,
            2
          ],
          "total": 7
        }
      ],
      "total": 27
    }
  ]
}
```
### API
A `dice-roll-api` command will be installed on your system.
If executed, the server will start running on host 0.0.0.0 and port 8000 by default.
These values can be changed via the `DICE_ROLL_HOST` and `DICE_ROLL_PORT` environment variables respectively.
The server takes requests on its "/" endpoint. Requests must be a POST.

The endpoint's accepted payload uses the following structure:
```json
{
    "dice": [
        {
            "count": {num-of-dice-with-provided-side-count-to-roll},
            "sides": {num-of-how-many-sides-current-dice-instance-should-have},
            "modifier": {optional-num-for-what-modifier-should-be-applied-to-dice-instance}
        }
    ],
    "count": {num-of-times-the-roll-described-above-should-be-attempted}
}
```

You can hit the server using curl like this:
```bash
curl --location --request POST 'localhost:8000' \
--header 'Content-Type: application/json' \
--data-raw '{
    "dice": [
        {
            "count": 1,
            "sides": 20,
            "modifier": 1
        },
        {
            "count": 1,
            "sides": 4,
            "modifier": 2
        }
    ],
    "count": 1
}'
```
