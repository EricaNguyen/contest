import contestMove
import random
import math

#dictionary of flavor text for Spectacular Talent moves
SpecMoves = {
    "cool": {
        "Normal": "Incredible Shining Road",
        "Fire": "Splendid Inferno",
        "Water": "Amazing Blessed Rain",
        "Electric": "Striking Chronicles",
        "Grass": "Fresh Flower Garden",
        "Ice": "Sublime Iceberg",
        "Fighting": "Grand Advance",
        "Poison": "Toxiquad CL",
        "Ground": "Planet Burst",
        "Flying": "Glorious Skies",
        "Psychic": "Techno",
        "Bug": "Cool Chrysalis",
        "Rock": "Rising Above",
        "Ghost": "Accursed House",
        "Dragon": "Doom Incarnate",
        "Dark": "Moonlit Pledge",
        "Steel": "Clarior E Tenebris",
        "Fairy": "Awesome * Adventure"
    },
    "tough": {
        "Normal": "Strong Shining Road",
        "Fire": "Devouring Inferno",
        "Water": "Soaking Blessed Rain",
        "Electric": "Thunderbolt Aftershock",
        "Grass": "Impressive Flower Garden",
        "Ice": "Powerful Blizzard",
        "Fighting": "Ballistic Bullet",
        "Poison": "Blighted Force TG",
        "Ground": "Supershear Quake",
        "Flying": "Intrepid Skies",
        "Psychic": "Anthem",
        "Bug": "Bold Transformation",
        "Rock": "These Stone Walls",
        "Ghost": "Agony Theater",
        "Dragon": "Agent of Divinity",
        "Dark": "Moonshadow Sorrow",
        "Steel": "Audaces Fortuna Iuvat",
        "Fairy": "Heroic * Journey"
    },
    "beauty": {
        "Normal": "Graceful Shining Road",
        "Fire": "Exquisite Inferno",
        "Water": "Serene Blessed Rain",
        "Electric": "Lightning Dazzle",
        "Grass": "Cultured Flower Garden",
        "Ice": "Glistening Icicles",
        "Fighting": "Uplifting Dawn",
        "Poison": "Venin Quartet BT",
        "Ground": "Global Shuddering",
        "Flying": "Celestial Skies",
        "Psychic": "Serenade",
        "Bug": "Radiant Emergence",
        "Rock": "Roaring Fantasia",
        "Ghost": "Nightmare Dawn",
        "Dragon": "Regal Courtesy",
        "Dark": "Moonscape Reflection",
        "Steel": "Luceat Lux Vestra",
        "Fairy": "Elegant * Outing"
    },
    "clever": {
        "Normal": "Bright Shining Road",
        "Fire": "Philosophical Inferno",
        "Water": "Clear Blessed Rain",
        "Electric": "Electrodynamic Archives",
        "Grass": "Blooming Flower Garden",
        "Ice": "Acute Frost",
        "Fighting": "Tactical Approach",
        "Poison": "Vitrolic Division CV",
        "Ground": "Tectonic Shift",
        "Flying": "Keen Skies",
        "Psychic": "Madrigal",
        "Bug": "Intellectual Awakening",
        "Rock": "Ambient World",
        "Ghost": "Evil Rituals",
        "Dragon": "Proven Sagacity",
        "Dark": "Moonbright Vision",
        "Steel": "Scientia Potentia Est",
        "Fairy": "Intelligent * Expedition"
    },
    "cute": {
        "Normal": "Pretty Shining Road",
        "Fire": "Scintillating Inferno",
        "Water": "Pattering Blessed Rain",
        "Electric": "Glittering Rhapsody",
        "Grass": "Enchanting Flower Garden",
        "Ice": "Twinkling Diamonds",
        "Fighting": "Charming Onslaught",
        "Poison": "Poison Orbit CN",
        "Ground": "Shaky Ground",
        "Flying": "Pleasant Skies",
        "Psychic": "Lullaby",
        "Bug": "Sweet Unfurling",
        "Rock": "Echo Ridge",
        "Ghost": "Midnight Revels",
        "Dragon": "Passionate Archetype",
        "Dark": "Moonrise Beckoning",
        "Steel": "Amor Vincit Omnia",
        "Fairy": "Delightful * Wandering"
    }
}

#this class represents a pokemon contestant
class Pokemon:
    def __init__(self, name, species, coolStat, toughStat, beautyStat, cleverStat, cuteStat, moves, canMega, types=["Normal"]):
        #init from params
        self.name = name
        self.species = species
        self.coolStat = coolStat
        self.toughStat = toughStat
        self.beautyStat = beautyStat
        self.cleverStat = cleverStat
        self.cuteStat = cuteStat
        self.moves = moves
        self.canMega = canMega
        self.types = types
        
        #calc condition score for initial turn order
        self.condition = 0
        self.gameStart = False
        
        #init without params
        self.currScore = 0
        self.tempScore = 0
        self.totalScore = 0
        self.prevMove = None
        self.currMove = None
        self.isNervous = False
        self.isCalm = False
        self.isVeryCalm = False
        self.pumpedUp = 0 #max 3
        self.priority = 0
        self.isKOd = False
        self.isMega = False
        self.isExpectingCombo = False
        self.easyStartle = False
    
    #used for determining turn order. If two pokemon would be tied for their turn order, randomly pick which one of the two will go earlier
    def __gt__(self, other):
        #for the first round, compare condition
        if self.gameStart == False:
            if self.condition != other.condition:
                return self.condition > other.condition
            else:
                return random.randint(0, 1) == 1
        
        #for other rounds
        if(self.priority != other.priority):
            return self.priority > other.priority
        else:
            if self.tempScore == other.tempScore:
                return random.randint(0, 1) == 1
            else:
                return self.tempScore > other.tempScore
        
    #perform a move
    def doMove(self, moveIndex, currTurnOrder, contestantsList):
        #if the pokemon is knocked out, skip its turn
        if self.isKOd == True:
            print(self.name + " the " + self.species + " is knocked out and can no longer move.")
            self.isExpectingCombo = False
        #if the pokemon used a move the previous turn that requires it to recharge this turn, skip its turn
        elif self.prevMove is not None and self.prevMove.effectIndex == 12:
            print("All " + self.name + " the " + self.species + " can do is watch the others.")
            self.isExpectingCombo = False
        #if the pokemon is nervous, skip its turn
        elif self.isNervous == True:
            print(self.name + " the " + self.species + " was too nervous to move!")
            self.isExpectingCombo = False
        #otherwise, carry out its move
        else:
            self.currMove = contestMove.moveList[self.moves[moveIndex]]
            print(self.name + " the " + self.species + " tried to show its appeal with " + self.currMove.name + "!")
            
            
            # === BASE APPEAL POINTS ===
            #calculate initial base appeal. Bonuses based on the audience excitement level are handled in stage.py
            temp = self.currMove.appeal
            flavorText = ""
            #extra points for moves that work great if the user goes first
            if self.currMove.effectIndex == 7 and currTurnOrder == 0:
                flavorText = "The standout leader, " + self.name + ", really tried to show off its appeal!"
                temp += 40
            #extra points for moves that work great if the user goes last
            elif self.currMove.effectIndex == 8 and currTurnOrder == 3:
                flavorText = self.name + " hadn't been standing out much, but really gave its all this time!"
                temp += 40
            #contestant earns 0,1,3,5 extra hearts moves that work better the later it is used in a turn
            elif self.currMove.effectIndex == 9:
                if currTurnOrder == 0:
                    pass
                elif currTurnOrder == 1:
                    flavorText = self.name + "'s " + self.currMove.name + " received extra points for its timing."
                    temp += 10
                elif currTurnOrder == 2:
                    flavorText = self.name + "'s " + self.currMove.name + " received extra points for its timing."
                    temp += 30
                else:
                    flavorText = self.name + "'s " + self.currMove.name + " showed off its appeal fantastically well!"
                    temp += 50
            #extra random hearts for moves that "vary depending on when it is used" (yes, it's a misleading description from the OG games...)
            elif self.currMove.effectIndex == 10:
                bonus = 2 * random.randint(0, 4) - 1
                if bonus <= 0:
                    flavorText = "The timing of " + self.name + "'s " + self.currMove.name + " didn't go over that well with the audience..."
                elif bonus >= 7:
                    flavorText = "The timing of " + self.name + "'s " + self.currMove.name + " went over great with the audience!"
                    temp += bonus * 10
                else:
                    flavorText = "The timing of " + self.name + "'s " + self.currMove.name + " went over fairly well with the audience."
                    temp += bonus * 10
            #if the move is 'Affected by how well the previous Pokemon's move went', give 0 hearts if the pokemon in front has more than 3 hearts, 6 if less, and 3 otherwise
            elif self.currMove.effectIndex == 24:
                if currTurnOrder == 0 or contestantsList[currTurnOrder-1].tempScore == 30:
                    pass
                elif contestantsList[currTurnOrder-1].tempScore > 30:
                    flavorText = "But " + self.name + " failed to stand out compared to the Pokemon that went before it..."
                    temp = 0
                else:
                    flavorText = "It totally outshone the last Pokemon! What appeal!"
                    temp = 60
            #if 'Shows off the Pokemon's appeal about as well as all the moves before it this turn', add hearts equal to sum of all previous contestants divided by 2, rounded down
            elif self.currMove.effectIndex == 28:
                if currTurnOrder > 0:
                    tempSum = 0
                    for i in range(0, currTurnOrder):
                        tempSum += contestantsList[i].tempScore
                    tempSum = int(tempSum/10)
                    tempSum = int(tempSum/2)
                    tempSum = max(0, tempSum)
                    tempSum *= 10
                    temp += tempSum
            #if 'Works well if it is the same type as the move used by the last Pokemon', add 4 bonus hearts
            elif self.currMove.effectIndex == 30:
                if currTurnOrder > 0 and contestantsList[currTurnOrder-1].currMove != None and contestantsList[currTurnOrder-1].currMove.category == self.currMove.category:
                    temp += 40
                    flavorText = "It was a huge hit with the audience because it was the same type as the move used by the last Pokemon!"
            #if 'Shows off the Pokemon's appeal about as well as the move used just before it', add number of hearts equal to the previous pokemon
            elif self.currMove.effectIndex == 34:
                if currTurnOrder > 0:
                    temp += max(0, contestantsList[currTurnOrder-1].tempScore)
                    flavorText = self.name + " did about as well as the Pokemon that went before it."
            
            #bonus hearts for being pumped up, 3x bonus if the move works well when pumped up
            if self.currMove.effectIndex == 6:
                temp += self.pumpedUp*30
            else:
                temp += self.pumpedUp*10
                
            #add initial appeal score to this round's score
            self.changeScore(temp)
            
            #print flavor text
            if flavorText != "":
                print(flavorText)
            
            
            # === SECONDARY EFFECTS ===
            #additional effects that apply only to the user. Effects that affect other pokemon are handled in stage.py's method doJam
            #sets priority
            if self.currMove.effectIndex == 1:
                print(self.name + " will move first in the next round.")
                self.priority = 1 * (1+currTurnOrder)
            elif self.currMove.effectIndex == 2:
                print(self.name + " will move last in the next round.")
                self.priority = -1 * (1+currTurnOrder)
            #set calmness
            elif self.currMove.effectIndex == 3:
                print(self.name + " is feeling pretty calm and collected now.")
                self.isCalm = True
            elif self.currMove.effectIndex == 4:
                print(self.name + " is completely oblivious to other Pokemon's moves.")
                self.isVeryCalm = True
            #pumps up
            elif self.currMove.effectIndex == 5:
                self.changePumpedUp(1)
            #easily startled
            elif self.currMove.effectIndex == 11:
                print(self.name + " will startle more easily this round.")
                self.easyStartle = True
            #self KO
            elif self.currMove.effectIndex == 13:
                print(self.name + " will not be able to make any more appeals for the rest of the contest.")
                self.isKOd = True
            #scrambles turn order
            elif self.currMove.effectIndex == 35:
                print(self.name + " scrambled the order of appeals for the next round!")
                for i in range(0, 4):
                    contestantsList[i].priority = random.random()
            
            #if this move completes a combo, earn 3 extra hearts
            if self.isExpectingCombo == True and self.prevMove is not None and self.prevMove.startsCombo == True and self.currMove.name in self.prevMove.combosWith:
                print(self.name + "'s move combination went over well with the audience!")
                self.changeScore(30)
            
            #check if this move can start a combo
            if self.currMove.startsCombo == True:
                self.isExpectingCombo = True
                print("Anticipation is swelling for a combo on the next turn!")
            else:
                self.isExpectingCombo = False
                
    
    #add/subtract hearts for the current round    
    def changeScore(self, scoreChange):
        if scoreChange < 0:
            print(self.name + " lost " + str(int(scoreChange/10)) + " heart(s)...")
        else:
            print(self.name + " gained +" + str(int(scoreChange/10)) + " heart(s)!")
        self.tempScore += scoreChange
        
    #change pumpedUp value
    def changePumpedUp(self, pumpedUpChange):
        if pumpedUpChange < 0:
            if self.pumpedUp > 0:
                self.pumpedUp = max(0, self.pumpedUp - 1)
                print(self.name + "'s energy was brought down!\n" + self.name + " lost -1 energy.")
        else:
            if self.pumpedUp <= 2:
                self.pumpedUp = min(self.pumpedUp + 1, 3)
                print(self.name + " got even more pumped up than usual!\n" + self.name + " gained +1 energy.")
    
    def getTempScore(self):
        return self.tempScore
        
    def getCurrScore(self):
        return self.currScore
    
    #setup for next round
    def nextRound(self):
        #update with values from the round that we just completed
        self.currScore = max(0, self.currScore + self.tempScore)
        self.prevMove = self.currMove
        
        #reset values in preperation for the next round
        self.tempScore = 0
        self.isNervous = False
        self.isCalm = False
        self.isVeryCalm = False
        self.priority = 0
        self.currMove = None
        self.easyStartle = False
    
    #calculate the condition score based on the pokemon's contest stats
    def calcCondition(self, category):
        if category == "cool":
            self.condition = self.coolStat + 0.5 * self.toughStat + 0.5 * self.beautyStat
        elif category == "tough":
            self.condition = self.toughStat + 0.5 * self.cleverStat + 0.5 * self.coolStat
        elif category == "beauty":
            self.condition = self.beautyStat + 0.5 * self.coolStat + 0.5 * self.cuteStat
        elif category == "clever":
            self.condition = self.cleverStat + 0.5 * self.cuteStat + 0.5 * self.toughStat
        else:
            self.condition = self.cuteStat + 0.5 * self.beautyStat + 0.5 * self.cleverStat
    
    def startGame(self):
        self.gameStart = True
       
    #totalScore = condition + 2*appeal
    def calcTotalScore(self):
        self.totalScore = self.condition + 2 * self.currScore
        
    #implement bonus points, mega evolution, and flavor text when this pokemon performs a Spectacular Talent (called by stage.py when this pokemon maxes out the audience meter)
    def doSpectacular(self, category):
        #make the element type of the spectacular talent the same as the pokemon. If the pokemon is dual-typed, choose randomly between the two types with the primary type weighted
        spectacularType = self.types[0]
        if len(self.types) > 1:
            spectacularType = random.choices(population=self.types, weights=[0.75, 0.25], k=1)[0]
            
        #give 5 bonus hearts (8 bonus hearts if the pokemon mega evolves this turn)
        if self.canMega == True and self.isMega == False:
            self.isMega = True
            self.species = "Mega " + self.species
            print(self.name + " mega evolved into " + self.species + "!")
            print("This is it! Time for a Spectacular Talent! " + SpecMoves[category][spectacularType].upper() + "!!")
            self.changeScore(80)
        else:
            print("This is it! Time for a Spectacular Talent! " + SpecMoves[category][spectacularType].upper() + "!!")
            self.changeScore(50)
        