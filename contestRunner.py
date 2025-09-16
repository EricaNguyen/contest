#this is the main script that runs the application
#py contestRunner.py

import pokemon
from pokemon import Pokemon
import stage
from stage import Stage
import contestMove
import random

"""
#cool contest contestants
moves1 = ["Thunder Wave", "Electro Ball", "Meteor Mash", "Agility"]
mon1 = Pokemon("Chuchu", "Pikachu", 275, 255, 255, 255, 255, moves1, False, ["Electric"])
moves2 = ["Swift", "Thunderbolt", "Psychic", "Quick Attack"]
mon2 = Pokemon("Raili", "Raichu", 275, 255, 255, 255, 255, moves2, False, ["Electric", "Psychic"])
moves3 = ["Detect", "Quick Attack", "Focus Energy", "Blaze Kick"]
mon3 = Pokemon("Bob", "Blaziken", 255, 255, 255, 255, 255, moves3, True, ["Fire", "Fighting"])
moves4 = ["Hyper Beam", "Roar", "Crunch", "Stealth Rock"]
mon4 = Pokemon("Cynthia", "Garchomp", 255, 255, 255, 255, 255, moves4, True, ["Ground", "Dragon"])
"""


#tough contest contestants
moves1 = ["Iron Head", "Giga Impact", "Ancient Power", "Power-Up Punch"]
mon1 = Pokemon("Tanabata", "Jirachi", 255, 275, 255, 255, 255, moves1, False, ["Steel", "Psychic"])
moves2 = ["Dig", "Muddy Water", "Aqua Tail", "Bide"]
mon2 = Pokemon("Swampy", "Swampert", 255, 255, 255, 255, 255, moves2, True, ["Water", "Ground"])
moves3 = ["Endure", "Endeavor", "Iron Defense", "Sandstorm"]
mon3 = Pokemon("Aaron", "Aron", 255, 275, 255, 255, 255, moves3, False, ["Steel", "Rock"])
moves4 = ["Stockpile", "Spit Up", "Swallow", "Gunk Shot"]
mon4 = Pokemon("Yamamoto", "Swalot", 255, 275, 255, 255, 255, moves4, False, ["Poison"])


"""
#beauty contest contestants
moves1 = ["Fire Spin", "Sunny Day", "Weather Ball", "Safeguard"]
mon1 = Pokemon("Kitsune", "Ninetales", 255, 255, 275, 255, 255, moves1, False, ["Fire"])
moves2 = ["Ice Beam", "Dragon Dance", "Aqua Tail", "Surf"]
mon2 = Pokemon("Melody", "Milotic", 255, 255, 275, 255, 255, moves2, False, ["Water"])
moves3 = ["Morning Sun", "Acrobatics", "Silver Wind", "Sunny Day"]
mon3 = Pokemon("Ageha", "Beautifly", 255, 255, 275, 255, 255, moves3, False, ["Bug", "Flying"])
moves4 = ["Ice Shard", "Protect", "Blizzard", "Explosion"]
mon4 = Pokemon("Snowball", "Glalie", 255, 255, 255, 255, 255, moves4, True, ["Ice"])
"""

"""
#clever contest contestants
moves1 = ["Calm Mind", "Stored Power", "Hypnosis", "Reflect"]
mon1 = Pokemon("Lily", "Gardevoir", 255, 255, 255, 255, 255, moves1, True, ["Psychic", "Fairy"])
moves2 = ["Stun Spore", "Absorb", "Giga Drain", "Petal Blizzard"]
mon2 = Pokemon("Hana", "Bellossom", 255, 255, 255, 275, 255, moves2, False, ["Grass"])
moves3 = ["Dark Void", "Nightmare", "Shadow Ball", "Protect"]
mon3 = Pokemon("Shadower", "Darkrai", 255, 255, 255, 275, 255, moves3, False, ["Dark"])
moves4 = ["Shadow Sneak", "Destiny Bond", "Taunt", "Curse"]
mon4 = Pokemon("Teru", "Banette", 255, 255, 255, 255, 255, moves4, True, ["Ghost"])
"""

"""
#cute contest contestants
moves1 = ["Attract", "Baby-Doll Eyes", "Sing", "Disarming Voice"]
mon1 = Pokemon("Pinky", "Skitty", 255, 255, 255, 255, 275, moves1, False, ["Normal"])
moves2 = ["Belly Drum", "Rollout", "Defense Curl", "Bubble Beam"]
mon2 = Pokemon("Bubbles", "Azumarill", 255, 255, 255, 255, 275, moves2, False, ["Water", "Fairy"])
moves3 = ["Cotton Guard", "Return", "Hone Claws", "Draco Meteor"]
mon3 = Pokemon("Fluffy", "Altaria", 255, 255, 255, 255, 255, moves3, True, ["Dragon", "Fairy"])
moves4 = ["Assist", "Fake Out", "Charm", "Encore"]
mon4 = Pokemon("Purrple", "Purrloin", 255, 255, 255, 255, 275, moves4, False, ["Dark"])
"""


#initialize the contestants
contestants = [mon1, mon2, mon3, mon4]

#init the contest stage
myStage = Stage("tough", contestants)


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
        myStage.getMonsInTurnOrder()[i].doMove(random.randint(0,3), i) #perform move
        myStage.updateExcitementLevel(myStage.getMonsInTurnOrder()[i], i) #update excitement level
        myStage.doJam(myStage.getMonsInTurnOrder()[i], i) #jam other pokemon
        myStage.makeNervous(myStage.getMonsInTurnOrder()[i], i) #make other pokemon nervous
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
    print("SELECT A MOVE:")
    for j in range (0, 4):
        #print an asterisk in front of moves that complete a combo this turn
        seperatorMark = " - "
        if mon1.isExpectingCombo == True and mon1.prevMove != None and moves1[j] in mon1.prevMove.combosWith:
            seperatorMark = " * "
        print(str(j) + seperatorMark + str(contestMove.moveList[moves1[j]]))
    choice = input()
    while choice.isdigit() == False or int(choice) > 3:
        print("Invalid choice, please type a number to select the corresponding move.")
        print()
        print("SELECT A MOVE:")
        for j in range (0, 4):
            seperatorMark = " - "
            if mon1.isExpectingCombo == True and mon1.prevMove != None and moves1[j] in mon1.prevMove.combosWith:
                seperatorMark = " * "
            print(str(j) + seperatorMark + str(contestMove.moveList[moves1[j]]))
        choice = input()
        
    #each pokemon performs a move in the order decided for this round
    for i in range(0, 4):
        if myStage.getMonsInTurnOrder()[i] is mon1:
            myStage.getMonsInTurnOrder()[i].doMove(int(choice), i) #player performs a move
        else:
            myStage.getMonsInTurnOrder()[i].doMove(random.randint(0,3), i) #NPC perform move
        myStage.updateExcitementLevel(myStage.getMonsInTurnOrder()[i], i) #update excitement level
        myStage.doJam(myStage.getMonsInTurnOrder()[i], i) #jam other pokemon
        myStage.makeNervous(myStage.getMonsInTurnOrder()[i], i) #make other pokemon nervous
        print()
    
    #move on to the next round
    myStage.nextRound()
    input("Press Enter to continue...")
