import contestMove
from contestMove import Move
#py exportCombos.py

#this script helps export a list of move combos, to use in the README file

#specify game mode to read data for ("ORAS" or "NatDex")
gameMode = "NatDex"

#load move data
contestMove.readMoveData("data/" +gameMode+ "/" + gameMode + "_movelist.csv")

comboStarts = []

#get list of moves that start combos, then sort the list alphabetically
for movename in contestMove.moveList.keys():
    if contestMove.moveList[movename].startsCombo == True:
        comboStarts.append(movename)
comboStarts.sort()
        
#write combo finishers to output file
with open("combo_output.txt", "w") as txtfile:
    txtfile.write("| Combo starter | Combo finisher |\n| --- | --- |")
    for movename in comboStarts:
        txtfile.write("\n| " + movename + " | ")
        tempFinisher = contestMove.moveList[movename].combosWith
        
        for i in range(0, len(tempFinisher)):
            txtfile.write(tempFinisher[i])
            if i < len(tempFinisher)-1:
                txtfile.write(", ")
        
        txtfile.write(" |")
        