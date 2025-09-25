import csv
#this file contains data on all moves

#given an effectIndex id number as a key, this dictionary keeps track of a move's effect
#format is effectIndex: [description, appeal, jam, jam target]
effectDict = {
    #basic attack (definition done, game mechs done, move list done)
    0: ["Quite an appealing move.", 40, 0, 'no jam'],
    #affects priority of the move's user (definition done, game mechs done, move list done)
    1: ["Causes the user to move earlier on the next turn.", 30, 0, 'no jam'],
    2: ["Causes the user to move later on the next turn.", 30, 0, 'no jam'],
    #affects calmness (definition done, game mechs done, move list done)
    3: ["Prevents the user from being startled one time this turn.", 20, 0, 'no jam'],
    4: ["Prevents the user from being startled until the turn ends.", 10, 0, 'no jam'],
    #related to the user's pumpedUp value (definition done, game mechs done, move list done)
    5: ["Gets the Pokemon pumped up. Helps prevent nervousness, too.", 10, 0, 'no jam'],
    6: ["Works well if the user is pumped up.", 10, 0, 'no jam'],
    #affected by the user's turn order (definition done, game mechs done, move list done)
    7: ["Works great if the user goes first this turn.", 20, 0, 'no jam'],
    8: ["Works great if the user goes last this turn.", 20, 0, 'no jam'],
    9: ["Works better the later it is used in a turn.", 10, 0, 'no jam'],
    #randomly picks 1,2,4,6, or 8 hearts (definition done, game mechs done, move list done)
    10: ["Effectiveness varies depending on when it is used.", 10, 0, 'no jam'],
    #negative effects on the user (definition done, game mechs done, move list done)
    11: ["A very appealing move, but after using this move, the user is more easily startled.", 60, 0, 'no jam'],
    12: ["User cannot act in the next turn.", 40, -40, 'all'],
    13: ["A move of huge appeal, but using it prevents the user from taking further contest moves.", 80, 0, 'no jam'],
    #make other pokemon nervous (definition done, game mechs done, move list done)
    14: ["Makes the remaining Pokemon nervous.", 20, 0, 'no jam'],
    #related to audience excitement level (definition done, game mechs done, move list done)
    15: ["Excites the audience a lot if used first", 30, 0, 'no jam'],
    16: ["Excites the audience a lot if used last", 30, 0, 'no jam'],
    17: ["Excites the audience in any kind of contest", 20, 0, 'no jam'],
    18: ["Works better the more the crowd is excited", 10, 0, 'no jam'],
    #can be repeated without boring the audience (definition done, game mechs done, move list done)
    19: ["An appealing move that can be used repeatedly without boring the audience.", 30, 0, 'no jam'],
    #jamming moves with no extra conditions or effects (definition done, game mechs done, move list done)
    20: ["Startles the last Pokemon to act before the user.", 20, -30, 'front'],
    21: ["Badly startles the last Pokemon to act before the user.", 10, -40, 'front'],
    22: ["Startles all of the Pokemon to act before the user.", 20, -20, 'all'],
    23: ["Badly startles all of the Pokemon to act before the user.", 10, -30, 'all'],
    #effect depends on the state of other pokemon (definition done, game mechs done, move list done)
    24: ["Affected by how well the previous Pokemon's move went.", 30, 0, 'no jam'],
    25: ["Badly startles all Pokemon that successfully showed their appeal.", 20, -10, 'successful'],
    26: ["Badly startles Pokemon that the audience has high expectations of.", 20, -10, 'high expectation'],
    27: ["Badly startles Pokemon that used a move of the same type.", 20, -10, 'same type'],
    28: ["Shows off the Pokemon's appeal about as well as all the moves before it this turn.", 10, 0, 'no jam'],
    29: ["Makes the audience quickly grow bored when an appeal move has little effect.", 40, 0, 'no jam'],
    30: ["Works well if it is the same type as the move used by the last Pokemon.", 20, 0, 'no jam'],
    #negatively affects other pokemon without causing them to lose hearts (definition done, game mechs done, move list done)
    31: ["Brings down the energy of any Pokemon that have already used a move this turn.", 30, 0, 'energy only'],
    32: ["Makes audience expect little of other contestants.", 30, 0, 'high expectation'],
    #misc (definition done, game mechs done, move list done)
    33: ["Temporarily stops the crowd from growing excited.", 30, 0, 'no jam'],
    34: ["Shows off the Pokemon's appeal about as well as the move used just before it.", 10, 0, 'no jam'],
    35: ["Scrambles the order in which Pokemon will move on the next turn.", 30, 0, 'no jam'],
    
    #other (temporarily use this for effects not implemented yet)
    -1: ["Description not implemented yet.", 0, 0, 'no jam']
}


#struct containing move data
class Move:
    def __init__(self, name, category, effectIndex=-1, startsCombo=False, combosWith=[]):
        self.name = name
        self.category = category
        self.effectIndex = effectIndex #0-35, see effectDict above
        self.appeal = effectDict[effectIndex][1]
        self.jam = effectDict[effectIndex][2]
        self.jamTarget = effectDict[effectIndex][3] #options: no jam, front, all, same type, high expectation, successful, energy only
        self.startsCombo = startsCombo #True if this move can be the start of a combo
        self.combosWith = combosWith #list the names of the moves that this move starts a combo with
    
    def __str__(self):
        return self.name + " (" + self.category.upper() + ", Appeal: " + str(int(self.appeal/10)) + ", Jam: " + str(int(self.jam/10)) + ")" + ", " + effectDict[self.effectIndex][0]


#this dictionary keeps track of the data for all moves
moveList = {}

#this dictionary keeps track of which categories are secondary to a given category
categorySecondaryType = {
    "cool": ["tough", "beauty"],
    "tough": ["clever", "cool"],
    "beauty": ["cool", "cute"],
    "clever": ["cute", "tough"],
    "cute": ["beauty", "clever"]
}

#read csv file containing data for all moves
def readMoveData(filename):
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            #name, category, effectIndex, startsCombo, combosWith
            if row['startsCombo'].strip().upper() == "FALSE":
                moveList[row['name']] = Move(row['name'], row['category'], int(row['effectIndex']))
            else:
                mylist = row['combosWith'].split('|')
                moveList[row['name']] = Move(row['name'], row['category'], int(row['effectIndex']), True, mylist)