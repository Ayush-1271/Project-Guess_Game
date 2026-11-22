# Console Number Guessing Game

A small Python terminal game that asks the player to guess a randomly selected integer from 1 to 1,000. It records the player's name, number of guesses, and elapsed time in `Score.csv`, and uses `high.txt` for the high-score value.

## Run

From the repository folder, use Python 3:

```bash
python Guess_Game.py
```

The game imports its welcome screen from `Welcome_File.py`. Keep that file beside `Guess_Game.py`.

## Existing score files

`Score.csv` and `high.txt` are used as local game state. The tracked `Score.csv` can contain player names and scores, so review its contents before sharing a copy of the repository. This README does not include any score values.
