#this is the main script that runs the application
#py contestRunner.py

import pokemon
from pokemon import Pokemon
import stage
from stage import Stage
import contestMove
import random
import csv

#define the player's pokemon, with a preset for each contest category read from a csv file
def initPlayerMon(gameMode, category):  
    player = None
    
    filename = "data/" + gameMode + "/player_data.csv"

    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['category'] == category:
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
                    
                #make pokemon object
                player = Pokemon(row['name'], row['species'], int(row['coolStat']), int(row['toughStat']), int(row['beautyStat']), int(row['cleverStat']), int(row['cuteStat']), tempMovepool, tempCanMega, tempType)
                break
                
    if player == None:
        print("Error reading player_data.csv. Make sure the csv file is formatted correctly.")
        
    return player

#create NPC opponents by reading data from a csv file, with presets for each category
def initCPUMons(gameMode, category): 
    possibleRoster = []
    
    #pick which csv file to read from based on the contest category
    filename = "data/" + gameMode + "/" + category + "_contestants.csv"
        
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


#initialize the game mode and contest category based on the contents of init.txt
gameMode = None #ORAS or NatDex
myCategory = None
with open('init.txt', 'r') as txtfile:
    gameMode = txtfile.readline().strip() #1st line is the game mode
    myCategory = txtfile.readline().strip() #2nd line is the contest category

#read the data for all the moves available for the given game mode
contestMove.readMoveData("data/" +gameMode+ "/" + gameMode + "_movelist.csv")

#initialize the contestants
#player
mon1 = initPlayerMon(gameMode, myCategory)
#NPC
CPUContestants = initCPUMons(gameMode, myCategory)
mon2 = CPUContestants[0]
mon3 = CPUContestants[1]
mon4 = CPUContestants[2]

contestants = [mon1, mon2, mon3, mon4]

#init the contest stage
myStage = Stage(myCategory, contestants)


#RUN THE GAME
print("WELCOME TO THE " + gameMode.upper() + " " + stage.categoryNouns[myStage.category].upper() + " CONTEST!!!")
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
        myStage.getMonsInTurnOrder()[i].doAppeal(random.randint(0,3), i, myStage.getMonsInTurnOrder(), myStage.excitementLevel) #perform move
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
    print("Turn order:")
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
            myStage.getMonsInTurnOrder()[i].doAppeal(int(choice), i, myStage.getMonsInTurnOrder(), myStage.excitementLevel) #player performs a move
        else:
            myStage.getMonsInTurnOrder()[i].doAppeal(random.randint(0,3), i, myStage.getMonsInTurnOrder(), myStage.excitementLevel) #NPC performs a random move
        myStage.getMonsInTurnOrder()[i].doJam(i, myStage.getMonsInTurnOrder()) #jam other pokemon
        myStage.getMonsInTurnOrder()[i].makeOthersNervous(i, myStage.getMonsInTurnOrder()) #make other pokemon nervous
        myStage.updateExcitementLevel(myStage.getMonsInTurnOrder()[i], i) #update audience excitement level
        
        print()
    
    #move on to the next round
    myStage.nextRound()
    input("Press Enter to continue...")
