import contestMove
from contestMove import Move
#py exportMoveChart.py

#this script helps export the list of moves in html format, to use in the README file
    
#specify game mode to read data for ("ORAS" or "NatDex")
gameMode = "NatDex"

#load move data
contestMove.readMoveData("data/" +gameMode+ "/" + gameMode + "_movelist.csv")

#dictionary, key: effectIndex+category as string (ex: 3cool), val: list of move names
fullMoveList = {}

#init dictionary
for i in range(0, 36):
    fullMoveList[str(i)+"cool"] = []
    fullMoveList[str(i)+"tough"] = []
    fullMoveList[str(i)+"beauty"] = []
    fullMoveList[str(i)+"clever"] = []
    fullMoveList[str(i)+"cute"] = []

#fill out dictionary
for move in contestMove.moveList:
    if contestMove.moveList[move].category == "cool":
        fullMoveList[str(contestMove.moveList[move].effectIndex)+"cool"].append(contestMove.moveList[move].name)
    elif contestMove.moveList[move].category == "tough":
        fullMoveList[str(contestMove.moveList[move].effectIndex)+"tough"].append(contestMove.moveList[move].name)
    elif contestMove.moveList[move].category == "beauty":
        fullMoveList[str(contestMove.moveList[move].effectIndex)+"beauty"].append(contestMove.moveList[move].name)
    elif contestMove.moveList[move].category == "clever":
        fullMoveList[str(contestMove.moveList[move].effectIndex)+"clever"].append(contestMove.moveList[move].name)
    else:
        fullMoveList[str(contestMove.moveList[move].effectIndex)+"cute"].append(contestMove.moveList[move].name)
        
#dictionary to keep track of descriptions. key: effectIndex, val: description
descriptions = {
    0: "| 0 | Quite an appealing move. | No additional effect. | 4 | 0 |",
    1: "| 1 | Causes the user to move earlier on the next turn. | Makes the user go first in the next round. <br/>If more than one contestant in a round uses a move with this effect, the contestant who used their move later this round will be prioritzed in going first in the next round. | 3 | 0 |",
    2: "| 2 | Causes the user to move later on the next turn. | Makes the user go last in the next round. <br/>If more than one contestant in a round uses a move with this effect, the contestant who used their move later this round will be prioritzed in going last in the next round. | 3 | 0 |",
    3: "| 3 | Prevents the user from being startled one time this turn. | The user will be prevented from being jammed one time this round. | 2 | 0 |",
    4: "| 4 | Prevents the user from being startled until the turn ends. | The user will be prevented from being jammed for the rest of the current round. | 1 | 0 |",
    5: "| 5 | Gets the Pokemon pumped up. Helps prevent nervousness, too. | The user gains 1 energy (up to 3 energy max). <br/>For subsequent rounds, the user will gain 1 extra heart per energy. <br/>Each energy also cuts the chance of becoming nervous in half. | 1 | 0 |",
    6: "| 6 | Works well if the user is pumped up. | The user gains 3 extra hearts per energy instead of just 1 extra heart per energy for this move. | 1 | 0 |",
    7: "| 7 | Works great if the user goes first this turn. | The user gains 6 hearts insted of 2 if they moved first this round. | 2 | 0 |",
    8: "| 8 | Works great if the user goes last this turn. | The user gains 6 hearts insted of 2 if they moved last this round. | 2 | 0 |",
    9: "| 9 | Works better the later it is used in a turn. | The user earns 1 heart if going 1st, 2 hearts if going 2nd, 4 hearts if going 3rd, and 6 hearts if going last. | 1 | 0 |",
    10: "| 10 | Effectiveness varies depending on when it is used. | Randomly earn 1, 2, 4, 6, or 8 hearts | 1 | 0 |",
    11: "| 11 | A very appealing move, but after using this move, the user is more easily startled. | For the rest of the current round, the user will lose double the amount of hearts if they get jammed. | 6 | 0 |",
    12: "| 12 | User cannot act in the next turn. | Jams all the contestants who went before the user, but then the user cannot move in the next round. | 4 | -4 |",
    13: "| 13 | A move of huge appeal, but using it prevents the user from taking further contest moves. | The user cannot move for the rest of the contest. | 8 | 0 |",
    14: "| 14 | Makes the remaining Pokemon nervous. | Each contestant going after you this round has a chance of becoming nervous and being unable to make their move. | 2 | 0 |",
    15: "| 15 | Excites the audience a lot if used first. | If the move category matches the contest category and the user goes first, the audience excitement meter goes up by 2 levels instead of 1. <br/>The user also earns 2 extra hearts from the audience's excitement instead of 1 as a result. | 3 | 0 |",
    16: "| 16 | Excites the audience a lot if used last. | If the move category matches the contest category and the user goes last, the audience excitement meter goes up by 2 levels instead of 1. <br/>The user also earns 2 extra hearts from the audience's excitement instead of 1 as a result. | 3 | 0 |",
    17: "| 17 | Excites the audience in any kind of contest. | The audience excitement meter goes up by 1, regardless of the contest category. | 2 | 0 |",
    18: "| 18 | Works better the more the crowd is excited. | The user earns 1 heart if the audience excitement meter is at 0-1, 3 hearts if the meter is at 2, 4 hearts if the meter is at 3, and 6 hearts if the meter is at 4. | 1 | 0 |",
    19: "| 19 | An appealing move that can be used repeatedly without boring the audience. | The user will not receive a penalty in hearts for repeating this move in the next round. | 3 | 0 |",
    20: "| 20 | Startles the last Pokemon to act before the user. | Jams the contestant who went right before the user in this round. | 2 | -3 |",
    21: "| 21 | Badly startles the last Pokemon to act before the user. | Jams the contestant who went right before the user in this round. | 1 | -4 |",
    22: "| 22 | Startles all of the Pokemon to act before the user. | Jams all the contestant who went before the user in this round. | 2 | -2 |",
    23: "| 23 | Badly startles all of the Pokemon to act before the user. | Jams all the contestant who went before the user in this round. | 1 | -3 |",
    24: "| 24 | Affected by how well the previous Pokemon's move went. | If the contestant who went right before the user earned less than 3 hearts this round, then the user earns 6 hearts. <br/>If the contestant who went right before the user earned more than 3 hearts this round, then the user does not earn any hearts. <br/>If the user is going first or if the contestant who went right before the user earned exactly 3 hearts, then the user earns 3 hearts. | 3 | 0 |",
    25: "| 25 | Badly startles all Pokemon that successfully showed their appeal. | Jams each contestant who went before the user this round for an amount equal to half of the hearts that contestant earned this round, rounded down. <br/>Minimum jam amount is 1 heart. | 2 | -1 |",
    26: "| 26 | Badly startles Pokemon that the audience has high expectations of. | All contestants who went before the user this round who are starting a move combo will be jammed for 5 hearts instead of 1. | 2 | -1 |",
    27: "| 27 | Badly startles Pokemon that used a move of the same type. | All contestants who went before the user this round who used a move of the same contest category as this move will be jammed for 4 hearts instead of 1. | 2 | -1 |",
    28: "| 28 | Shows off the Pokemon's appeal about as well as all the moves before it this turn. | Earns an amount of hearts equal to half the total amount of hearts earned this round by the contestants that went before the user, rounded down, plus 1. <br/>Minimum amount of hearts earned is 1. | 1 | 0 |",
    29: "| 29 | Makes the audience quickly grow bored when an appeal move has little effect. | If this move does not match the contest category nor the complementary contest categories, the audience excitement meter goes down by 2 instead of 1. | 4 | 0 |",
    30: "| 30 | Works well if it is the same type as the move used by the last Pokemon. | If the contestant who went right before the user this round used a move of the same contest category as this move, the user earns 6 hearts instead of 2. | 2 | 0 |",
    31: "| 31 | Brings down the energy of any Pokemon that have already used a move this turn. | All contestants who went before the user this round lose 1 energy. <br/>This move cannot cause a contestant to go below 0 energy. | 3 | 0 |",
    32: "| 32 | Makes audience expect little of other contestants. | Makes the audience no longer expect a move combo in the next round from any contestants who went before the user in this round. | 3 | 0 |",
    33: "| 33 | Temporarily stops the crowd from growing excited. | For this round, contestants who go after the user cannot increase the audience excitement meter. | 3 | 0 |",
    34: "| 34 | Shows off the Pokemon's appeal about as well as the move used just before it. | Earns the same amount of hearts as the contestant who went right before the user, plus 1 heart. <br/>Minimum amount of hearts earned is 1. | 1 | 0 |",
    35: "| 35 | Scrambles the order in which Pokemon will move on the next turn. | The turn order for all contestants is random in the next round. | 3 | 0 |"
}

with open("movechart_output.txt", "w") as txtfile:
    txtfile.write("| ID | In-game description | Detailed description | Appeal | Jam | Cool moves | Tough moves | Beauty moves | Clever moves | Cute Moves |\n")
    txtfile.write("| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |\n")
    for i in range(0, 36):
    
        #write description text to output file
        txtfile.write(descriptions[i])
        
        #cool section
        txtfile.write(" ")
        if len(fullMoveList[str(i)+"cool"]) > 0:
            txtfile.write("<ul>")
            for moveName in fullMoveList[str(i)+"cool"]:
                txtfile.write("<li>" + moveName + "</li>")
            txtfile.write("</ul>")
        else:
            txtfile.write("N/A")
        txtfile.write(" |")
        
        #tough section
        txtfile.write(" ")
        if len(fullMoveList[str(i)+"tough"]) > 0:
            txtfile.write("<ul>")
            for moveName in fullMoveList[str(i)+"tough"]:
                txtfile.write("<li>" + moveName + "</li>")
            txtfile.write("</ul>")
        else:
            txtfile.write("N/A")
        txtfile.write(" |")
        
        #beauty section
        txtfile.write(" ")
        if len(fullMoveList[str(i)+"beauty"]) > 0:
            txtfile.write("<ul>")
            for moveName in fullMoveList[str(i)+"beauty"]:
                txtfile.write("<li>" + moveName + "</li>")
            txtfile.write("</ul>")
        else:
            txtfile.write("N/A")
        txtfile.write(" |")
        
        #clever section
        txtfile.write(" ")
        if len(fullMoveList[str(i)+"clever"]) > 0:
            txtfile.write("<ul>")
            for moveName in fullMoveList[str(i)+"clever"]:
                txtfile.write("<li>" + moveName + "</li>")
            txtfile.write("</ul>")
        else:
            txtfile.write("N/A")
        txtfile.write(" |")
        
        #cute section
        txtfile.write(" ")
        if len(fullMoveList[str(i)+"cute"]) > 0:
            txtfile.write("<ul>")
            for moveName in fullMoveList[str(i)+"cute"]:
                txtfile.write("<li>" + moveName + "</li>")
            txtfile.write("</ul>")
        else:
            txtfile.write("N/A")
        txtfile.write(" |\n")