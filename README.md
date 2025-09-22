# Contest
A text-based ORAS-style Pokemon contest simulator.

## Prereqs
- Python 3.10+

## How to run the program
If you are on Windows, simply double-click the `RunContest.bat` file to run the program.

Otherwise, you can run the program from the command line by going into the project directory and entering the command: `py contestRunner.py`

### Game modes
You can change the contest category and the moveset of your Pokemon by editing **contestRunner.py**

To change the contest category, set the **myCategory** variable (line 66 of **contestRunner.py**) to either `"cool"`, `"tough"`, `"beauty"`, `"clever"`, or `"cute"`.

To change your Pokemon's moveset, go to the **initPlayerMon** method (starts at line 13 of **contestRunner.py**) and then edit the moves list found in the if-else block for your desired category.
Move names are case sensitive.

