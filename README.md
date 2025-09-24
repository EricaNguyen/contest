# Contest
A text-based ORAS-style Pokemon contest simulator. For five rounds, the player competes with three other NPC opponents to see who can excite the audience the most with their Pokemon's moves.

## Prereqs
- Python 3.10+

## How to run the program
If you are on Windows, simply double-click the `RunContest.bat` file to run the program.

Otherwise, you can run the program from the command line by going into the project directory and entering the command: `py contestRunner.py`

### Game settings
You can change the game modes and your Pokemon before running the program.

<details>

<summary>How to change the game modes</summary>

**To change the game modes**, edit `init.txt` in a text editor (ex: Notepad).

1. The first line of the txt file denotes the main game mode. The possible modes are `ORAS` (only uses moves introduced in Gens I-VI) or `NatDex` (includes moves introduced after Gen VI, with contest effects assigned to the new moves based on what I felt made sense).
2. The second line of the txt file denotes the contest category. The possible categories are `cool`, `tough`, `beauty`, `clever`, or `cute`.

</details>

<details>

<summary>How to change your Pokemon</summary>

**To change your Pokemon**, go to the folder `data/<your desired game mode>` and edit `player_data.csv` using a spreadsheet application (ex: Google Sheets, Microsoft Excel, etc).
Each row of the csv file has different Pokemon presets for each contest category. Feel free to edit the Pokemon data for whichever contest categories you want to play. Make sure the data is spelled correctly and has correct capitalization.

The data fields for your Pokemon are:

1. name: *the nickname of your Pokemon*
2. species: *the species of your Pokemon*
3. contest condition stats (coolStat, toughStat, etc): *The Pokemon with the highest contest condition stats will move earlier during the first round of the game. Realistically, these values should be integer between 0 - 255 inclusive, and one of these values can go up to 275 if the Pokemon would not use a mega stone to mega evolve.*
4. moves (move1, move2, etc): *These are the names of the moves that you want your Pokemon to learn.*
5. canMega: *write TRUE if your Pokemon is capable of mega evolution, and FALSE otherwise*
6. types (type1, type2): *The type(s) of your Pokemon species, such as Grass, Fire, Water, etc. For Pokemon that can mega evolve, write the types that match the mega-evolved form. If your Pokemon does not have a secondary type, leave the cell under the type2 column blank.*

</details>

After you are done editing the relevant files and have saved your changed, run the program to play the game under your new settings!
