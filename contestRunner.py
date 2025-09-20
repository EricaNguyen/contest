#this is the main script that runs the application
#py contestRunner.py

import pokemon
from pokemon import Pokemon
import stage
from stage import Stage
import contestMove
import random
import csv

#define the player's pokemon, with a preset for each contest category
def initPlayerMon(category):  
    player = None
    
    if category == "cool":
        moves = ["Thunder Wave", "Electro Ball", "Meteor Mash", "Agility"]
        player = Pokemon("Chuchu", "Pikachu", 275, 255, 255, 255, 255, moves, False, ["Electric"])
    elif category == "tough":
        moves = ["Focus Punch", "Flying Press", "Wild Charge", "Dig"]
        player = Pokemon("Pika", "Pikachu", 255, 275, 255, 255, 255, moves, False, ["Electric"])
    elif category == "beauty":
        moves = ["Icicle Crash", "Round", "Discharge", "Flash"]
        player = Pokemon("Chuchu", "Pikachu", 255, 255, 275, 255, 255, moves, False, ["Electric"])
    elif category == "clever":
        moves = ["Electric Terrain", "Knock Off", "Feint", "Magnet Rise"]
        player = Pokemon("Pika", "Pikachu", 255, 255, 255, 275, 255, moves, False, ["Electric"])
    else:
        moves = ["Nuzzle", "Play Nice", "Draining Kiss", "Attract"]
        player = Pokemon("Chuchu", "Pikachu", 255, 255, 255, 255, 275, moves, False, ["Electric"])
    
    return player

#create NPC opponents by reading data from a csv file, with presets for each category
def initCPUMons(category): 
    possibleRoster = []
    
    #pick which csv file to read from based on the contest category
    filename = "data/" + category + "_contestants.csv"
        
    #read contestant data from csv file
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            #list of moves
            tempMovepool = [row['move1'], row['move2'], row['move3'], row['move4']]
            #list of types
            tempType = [row['type1']]
            if row['type2'] != "":
                tempType.append(row['type2'])
            #set bool for canMega
            tempCanMega = False
            if row['canMega'].upper() == "TRUE":
                tempCanMega = True
            
            #make a new Pokemon object and append it to our list of possible contestants
            possibleRoster.append( Pokemon(row['name'], row['species'], int(row['coolStat']), int(row['toughStat']), int(row['beautyStat']), int(row['cleverStat']), int(row['cuteStat']), tempMovepool, tempCanMega, tempType) )
        
    #pick 3 random mons from the possible roster
    chosenContestants = random.sample(possibleRoster, 3)
    
    return chosenContestants


#initialize the contest category
myCategory = "cool"

contestMove.readMoveData("data/ORAS_movelist.csv")

#initialize the contestants
mon1 = initPlayerMon(myCategory)
CPUContestants = initCPUMons(myCategory)
mon2 = CPUContestants[0]
mon3 = CPUContestants[1]
mon4 = CPUContestants[2]

contestants = [mon1, mon2, mon3, mon4]

#init the contest stage
myStage = Stage(myCategory, contestants)


#RUN THE GAME
print("WELCOME TO THE " + stage.categoryNouns[myStage.category].upper() + " CONTEST!!!")
myStage.startGame()

"""
#all NPCs
#each loop is a round of the game
for i in range (0, 5):
    #print info for the beginning of the current round
    print(str(myStage))
    myStage.printTurnOrderList()
    print("---")
    input("Press Enter to continue...")
        
    #each pokemon performs a move in the order decided for this round
    for i in range(0, 4):
        myStage.getMonsInTurnOrder()[i].doAppeal(random.randint(0,3), i, myStage.getMonsInTurnOrder()) #perform move
        myStage.getMonsInTurnOrder()[i].doJam(i, myStage.getMonsInTurnOrder()) #jam other pokemon
        myStage.getMonsInTurnOrder()[i].makeOthersNervous(i, myStage.getMonsInTurnOrder()) #make other pokemon nervous
        myStage.updateExcitementLevel(myStage.getMonsInTurnOrder()[i], i) #update excitement level
        print()
    
    #move on to the next round
    myStage.nextRound()
    input("Press Enter to continue...")
"""

#allow the player to play
print("(Your Pokemon is " + mon1.name + " the " + mon1.species +")")
#each loop is a round of the game
for i in range (0, 5):
    #print info for the beginning of the current round
    print(str(myStage))
    myStage.printTurnOrderList()
    print("---\n")
    
    #prompt user for move choice
    print("SELECT A MOVE by entering a number (0 - 3):")
    print("-")
    for j in range (0, 4):
        #print an asterisk in front of moves that complete a combo this turn
        seperatorMark = " - "
        if mon1.isExpectingCombo == True and mon1.prevMove != None and mon1.moves[j] in mon1.prevMove.combosWith:
            seperatorMark = " * "
        print(str(j) + seperatorMark + str(contestMove.moveList[mon1.moves[j]]))
    choice = input()
    while choice.isdigit() == False or int(choice) > 3:
        print("Invalid choice, please type a number (0 - 3) to select the corresponding move and then press Enter.")
        print()
        print("SELECT A MOVE:")
        print("-")
        for j in range (0, 4):
            seperatorMark = " - "
            if mon1.isExpectingCombo == True and mon1.prevMove != None and mon1.moves[j] in mon1.prevMove.combosWith:
                seperatorMark = " * "
            print(str(j) + seperatorMark + str(contestMove.moveList[mon1.moves[j]]))
        choice = input()
        
    #each pokemon performs a move in the order decided for this round
    for i in range(0, 4):
        if myStage.getMonsInTurnOrder()[i] is mon1:
            myStage.getMonsInTurnOrder()[i].doAppeal(int(choice), i, myStage.getMonsInTurnOrder()) #player performs a move
        else:
            myStage.getMonsInTurnOrder()[i].doAppeal(random.randint(0,3), i, myStage.getMonsInTurnOrder()) #NPC performs a random move
        myStage.getMonsInTurnOrder()[i].doJam(i, myStage.getMonsInTurnOrder()) #jam other pokemon
        myStage.getMonsInTurnOrder()[i].makeOthersNervous(i, myStage.getMonsInTurnOrder()) #make other pokemon nervous
        myStage.updateExcitementLevel(myStage.getMonsInTurnOrder()[i], i) #update audience excitement level
        
        print()
    
    #move on to the next round
    myStage.nextRound()
    input("Press Enter to continue...")
