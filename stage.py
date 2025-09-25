import pokemon
import contestMove
import random

#this dictionary keeps track of the noun forms of the contest category types, for grammatically correct flavor text
categoryNouns = {
    "cool": "Coolness",
    "tough": "Toughness",
    "beauty": "Beauty",
    "clever": "Cleverness",
    "cute": "Cuteness"
}

#this class represents the game state
class Stage:
    def __init__(self, category, contestants):
        self.category = category
        self.contestants = contestants
        
        #calculate condition of the contestants, and sort to get the turn order for the first round
        for contestant in contestants:
            contestant.calcCondition(self.category)
        self.contestants.sort(reverse=True)
            
        self.currRound = 1
        self.excitementLevel = 0
        self.isExcitementStopped = False #true if a pokemon uses a move that temporarily stops the crowd from growing more excited
        
        
    def __str__(self):
        return "\n=======\nCurrent Round #: " + str(self.currRound) + ", Audience excitement level: " + str(self.excitementLevel)
        
    def printTurnOrderList(self):
        print("Turn order:")
        listSize = len(self.contestants)
        for i in range(0, listSize):
            #print an asterisk in front of contestants that the audience is expecting a combo from
            seperatorMark = " - "
            if self.contestants[i].isExpectingCombo == True:
                seperatorMark = " * "
            print(str(i+1) + seperatorMark + self.contestants[i].name + " the " + self.contestants[i].species + " (Energy: " + str(self.contestants[i].pumpedUp) + ")")
    
    #return a list of Pokemon in the order that they will move in for the round
    def getMonsInTurnOrder(self):
        return self.contestants
    
    #set the startGame bool to True for all contestants so that the turn order for rounds 2-5 do not depend on condition stats
    def startGame(self):
        for contestant in self.contestants:
            contestant.startGame()
    
    
    #update the audience's excitement level after a given pokemon has performed their move, then add/subtract bonus hearts as needed
    def updateExcitementLevel(self, contestant, currTurnOrder):
        #check if the pokemon moved this turn
        if contestant.currMove is not None:
            #if the pokemon used the same move they used in the previous round and the move's effect does not allow it to repeat, subtract a heart
            if contestant.prevMove is not None and contestant.currMove is contestant.prevMove and contestant.currMove.effectIndex != 19:
                print("The crowd was disappointed to see " + contestant.name + " repeat the same move...")
                contestant.changeScore(-10)
            #if the move's category is not primary or secondary to this contest's category, lower excitement and subtract a heart
            elif contestant.currMove.effectIndex != 17 and contestant.currMove.category != self.category and contestant.currMove.category not in contestMove.categorySecondaryType[self.category]:
                #lower excitement by 2 instead of 1 if the move description is 'Makes the audience quickly grow bored when an appeal move has little effect' (need further research to see if this effect is correct)
                if contestant.currMove.effectIndex == 29:
                    print("But "+ contestant.name + "'s show of " + categoryNouns[contestant.currMove.category] + " went very poorly with this audience...")
                    self.excitementLevel = max(0, self.excitementLevel - 2)
                    contestant.changeScore(-10)
                else:
                    #print("contestant.currMove.category = " + contestant.currMove.category + ", stage category = " + self.category)
                    print("But "+ contestant.name + "'s show of " + categoryNouns[contestant.currMove.category] + " didn't go over very well with this audience.")
                    self.excitementLevel = max(0, self.excitementLevel - 1)
                    contestant.changeScore(-10)
            #if the excitement meter isnt frozen 
            elif(self.isExcitementStopped == False):
                #the move matched the contest category and meets the requirements for "excites the audience a lot", raise excitement by 2 instead of 1
                if (contestant.currMove.category == self.category and (contestant.currMove.effectIndex == 15 and currTurnOrder == 0 or contestant.currMove.effectIndex == 16 and currTurnOrder == 3)):
                    print(contestant.name + "'s move really, really excited the audience!")
                    self.excitementLevel = min(self.excitementLevel + 2, 5)
                    contestant.changeScore(20)
                #if the move was not a repeat and the move category matched the contest category or always raises excitement regardless of category, raise excitement and add a heart
                elif (contestant.currMove.category == self.category or contestant.currMove.effectIndex == 17):
                    print(contestant.name + "'s " + categoryNouns[contestant.currMove.category] + " really excited the audience!")
                    self.excitementLevel += 1
                    contestant.changeScore(10)
            
            #if the pokemon uses a move that stops the excitement meter from growing, apply that effect for the rest of the current round
            if (contestant.currMove.effectIndex == 33):
                self.isExcitementStopped = True
                print(contestant.name + " became the center of attention.")
                
        #after all checks above are done, see the current audience excitement level
        print("Audience excitement level: " + str(self.excitementLevel))
        
        #constestant performs a Spectacular Talent if the audience meter is maxed out
        if self.excitementLevel >= 5:
            print("The audience is completely taken with " + contestant.name + " the " + contestant.species + "'s " + categoryNouns[self.category] + "!")
            contestant.doSpectacular(self.category)
            #reset the excitement level
            self.excitementLevel = 0
            print("Audience excitement level: " + str(self.excitementLevel))
    
    
    #update the state of the game to the next round
    def nextRound(self):
        #print the total hearts each pokemon earned for this round, their priority score, and their pumpedUp value
        print("---")
        for contestant in self.contestants:
            print(contestant.name + " the " + contestant.species + " earned " + str(int(contestant.tempScore/10)) + " heart(s) this round. (Priority: " + str(contestant.priority) + ", Energy: " + str(contestant.pumpedUp) + ")")
        
        #update the turn order for the next round
        self.contestants.sort(reverse=True)
        
        #update values for the contestants to prepare for the next round
        for contestant in self.contestants:
            contestant.nextRound()
        
        #update the round counter
        self.currRound += 1
        
        #resume audience excitement meter changes for the next round
        self.isExcitementStopped = False
        
        #if 5 rounds have already been completed, end the game
        if self.currRound > 5:
            self.endGame()
            
    #end the game
    def endGame(self):
        print("\n=======\nTHE CONTEST HAS ENDED!\n=======")
        
        #make user press Enter before showing results, to build suspense
        input("Press Enter to see the contest results...")
        
        #calculate the total score for each contestant
        for contestant in self.contestants:
            contestant.calcTotalScore()
            
        #print resulting scores, in order of least to greatest
        self.contestants.sort(key=lambda contestant: contestant.totalScore)
        print("-")
        print("RESULTS:")
        for contestant in self.contestants:
            print(contestant.name + " the " + contestant.species + " - Condition: " +str(int(contestant.condition)) + ", Appeal: " + str(int(contestant.currScore * 2)) + ", Total score: " + str(int(contestant.totalScore)))
            
        #announce the winner. TODO: print multiple winners if there is a tie
        print("---")
        print("CONGRATULATIONS to " + self.contestants[-1].name + " the " + self.contestants[-1].species + " for winning!!!")