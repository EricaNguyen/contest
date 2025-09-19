#this file contains data on all moves

#given an id nuber, this dictionary keeps track of a move's effect
#format: [description, appeal, jam, jam target]
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
        #additional effects of the move go here
    
    def __str__(self):
        return self.name + " (" + self.category.upper() + ", Appeal: " + str(int(self.appeal/10)) + ", Jam: " + str(int(self.jam/10)) + ")" + ", " + effectDict[self.effectIndex][0]


#this dictionary keeps track of the data for all moves
#cool combo starters done
moveList = {
    #== Quite an appealing move (0) == DONE
    #cool (done)
    "Air Cutter": Move("Air Cutter", "cool", 0),
    "Brick Break": Move("Brick Break", "cool", 0),
    "Cut": Move("Cut", "cool", 0),
    "Dark Pulse": Move("Dark Pulse", "cool", 0),
    "Dragon Claw": Move("Dragon Claw", "cool", 0),
    "Fire Fang": Move("Fire Fang", "cool", 0),
    "Focus Blast": Move("Focus Blast", "cool", 0),
    "Force Palm": Move("Force Palm", "cool", 0, True, ["Hex", "Smelling Salts"]),
    "Horn Attack": Move("Horn Attack", "cool", 0),
    "Ice Fang": Move("Ice Fang", "cool", 0),
    "Iron Tail": Move("Iron Tail", "cool", 0),
    "Metal Claw": Move("Metal Claw", "cool", 0),
    "Peck": Move("Peck", "cool", 0),
    "Psycho Cut": Move("Psycho Cut", "cool", 0),
    "Razor Leaf": Move("Razor Leaf", "cool", 0),
    "Rolling Kick": Move("Rolling Kick", "cool", 0),
    "Shadow Claw": Move("Shadow Claw", "cool", 0),
    "Slash": Move("Slash", "cool", 0),
    "Spark": Move("Spark", "cool", 0),
    "Thunder Fang": Move("Thunder Fang", "cool", 0),
    "Thunder Punch": Move("Thunder Punch", "cool", 0),
    "Thunder Shock": Move("Thunder Shock", "cool", 0),
    "Thunderbolt": Move("Thunderbolt", "cool", 0),
    "Twister": Move("Twister", "cool", 0),
    "Vine Whip": Move("Vine Whip", "cool", 0),
    "Wing Attack": Move("Wing Attack", "cool", 0),
    #tough (done)
    "Fire Punch": Move("Fire Punch", "tough", 0),
    "Headbutt": Move("Headbutt", "tough", 0),
    "Iron Head": Move("Iron Head", "tough", 0),
    "Karate Chop": Move("Karate Chop", "tough", 0),
    "Mud Shot": Move("Mud Shot", "tough", 0),
    "Poison Jab": Move("Poison Jab", "tough", 0),
    "Pound": Move("Pound", "tough", 0),
    "Rock Smash": Move("Rock Smash", "tough", 0),
    "Rock Throw": Move("Rock Throw", "tough", 0),
    "Scratch": Move("Scratch", "tough", 0),
    "Seed Bomb": Move("Seed Bomb", "tough", 0),
    "Slam": Move("Slam", "tough", 0),
    "Smog": Move("Smog", "tough", 0),
    "Stomp": Move("Stomp", "tough", 0),
    "Strength": Move("Strength", "tough", 0),
    "Tackle": Move("Tackle", "tough", 0),
    "Vice Grip": Move("Vice Grip", "tough", 0),
    "Waterfall": Move("Waterfall", "tough", 0),
    #beauty (done)
    "Aqua Tail": Move("Aqua Tail", "beauty", 0),
    "Dazzling Gleam": Move("Dazzling Gleam", "beauty", 0),
    "Dragon Pulse": Move("Dragon Pulse", "beauty", 0),
    "Earth Power": Move("Earth Power", "beauty", 0),
    "Energy Ball": Move("Energy Ball", "beauty", 0),
    "Fairy Wind": Move("Fairy Wind", "beauty", 0),
    "Flamethrower": Move("Flamethrower", "beauty", 0),
    "Flash Cannon": Move("Flash Cannon", "beauty", 0),
    "Ice Punch": Move("Ice Punch", "beauty", 0),
    "Powder Snow": Move("Powder Snow", "beauty", 0),
    "Power Gem": Move("Power Gem", "beauty", 0),
    #clever (done)
    "Absorb": Move("Absorb", "clever", 0),
    "Confusion": Move("Confusion", "clever", 0),
    "Gear Grind": Move("Gear Grind", "clever", 0),
    "Helping Hand": Move("Helping Hand", "clever", 0),
    "Needle Arm": Move("Needle Arm", "clever", 0),
    "Poison Fang": Move("Poison Fang", "clever", 0),
    "Psychic": Move("Psychic", "clever", 0),
    "Shadow Ball": Move("Shadow Ball", "clever", 0),
    "Zen Headbutt": Move("Zen Headbutt", "clever", 0),
    #cute (done)
    "Bubble": Move("Bubble", "cute", 0),
    "Egg Bomb": Move("Egg Bomb", "cute", 0),
    "Ember": Move("Ember", "cute", 0),
    "Return": Move("Return", "cute", 0),
    "Water Gun": Move("Water Gun", "cute", 0),
    
    #== Causes the user to move earlier on the next turn (1) == DONE
    #cool (done)
    "Agility": Move("Agility", "cool", 1, True, ["Baton Pass", "Electro Ball"]),
    "Aqua Jet": Move("Aqua Jet", "cool", 1),
    "Extreme Speed": Move("Extreme Speed", "cool", 1),
    "Mach Punch": Move("Mach Punch", "cool", 1),
    "Quick Attack": Move("Quick Attack", "cool", 1),
    "Tailwind": Move("Tailwind", "cool", 1),
    "Vacuum Wave": Move("Vacuum Wave", "cool", 1),
    "Water Shuriken": Move("Water Shuriken", "cool", 1),
    #tough (done)
    "Bullet Punch": Move("Bullet Punch", "tough", 1),
    "Rock Polish": Move("Rock Polish", "tough", 1, True, ["Baton Pass", "Electro Ball"]),
    #beauty (done)
    "Ice Shard": Move("Ice Shard", "beauty", 1),
    #clever (done)
    "Feint": Move("Feint", "clever", 1),
    "Lock-On": Move("Lock-On", "clever", 1, True, ["Fissure", "Guillotine", "Horn Drill", "Sheer Cold"]),
    "Me First": Move("Me First", "clever", 1),
    "Mind Reader": Move("Mind Reader", "clever", 1, True, ["Fissure", "Guillotine", "Horn Drill", "Sheer Cold"]),
    "Quash": Move("Quash", "clever", 1),
    "Shadow Sneak": Move("Shadow Sneak", "clever", 1),
    #cute (done)
    "Baby-Doll Eyes": Move("Baby-Doll Eyes", "cute", 1),
    
    #== Causes the user to move later on the next turn (2) == DONE
    #cool move (done)
    "Circle Throw": Move("Circle Throw", "cool", 2),
    "Roar": Move("Roar", "cool", 2),
    #tough (done)
    "Bide": Move("Bide", "tough", 2),
    "Curse": Move("Curse", "tough", 2),
    "Dragon Tail": Move("Dragon Tail", "tough", 2),
    "Endure": Move("Endure", "tough", 2, True, ["Endeavor", "Flail", "Reversal", "Pain Split"]),
    #beauty (N/A)
    #clever (done)
    "Whirlwind": Move("Whirlwind", "clever", 2),
    #cute (done)
    "After You": Move("After You", "cute", 2),
    
    #== Prevents the user from being startled one time this turn (3) == DONE
    #cool (N/A)
    #tough (done)
    "Dig": Move("Dig", "tough", 3),
    "Harden": Move("Harden", "tough", 3),
    "Swallow": Move("Swallow", "tough", 3),
    #beauty (done)
    "Dive": Move("Dive", "beauty", 3),
    "Light Screen": Move("Light Screen", "beauty", 3),
    "Safeguard": Move("Safeguard", "beauty", 3),
    #clever (done)
    "Fly": Move("Fly", "clever", 3),
    "Reflect": Move("Reflect", "clever", 3),
    "Defend Order": Move("Defend Order", "clever", 3),
    "Grass Whistle": Move("Grass Whistle", "clever", 3, True, ["Dream Eater", "Hex", "Nightmare", "Wake-Up Slap"]),
    "Odor Sleuth": Move("Odor Sleuth", "clever", 3),
    #cute (done)
    "Defense Curl": Move("Defense Curl", "cute", 3, True, ["Rollout", "Ice Ball"]),
    "Protect": Move("Protect", "cute", 3),
    "Refresh": Move("Refresh", "cute", 3),
    "Substitute": Move("Substitute", "cute", 3),
    "Sweet Scent": Move("Sweet Scent", "cute", 3),
    "Withdraw": Move("Withdraw", "cute", 3),
    
    #== Prevents the user from being startled until the turn ends (4) == DONE
    #cool (done)
    "Barrier": Move("Barrier", "cool", 4),
    "Detect": Move("Detect", "cool", 4),
    "King's Shield": Move("King's Shield", "cool", 4),
    "Phantom Force": Move("Phantom Force", "cool", 4),
    "Shadow Force": Move("Shadow Force", "cool", 4),
    "Teleport": Move("Teleport", "cool", 4),
    #tough (done)
    "Acid Armor": Move("Acid Armor", "tough", 4),
    "Iron Defense": Move("Iron Defense", "tough", 4),
    "Spiky Shield": Move("Spiky Shield", "tough", 4),
    "Wide Guard": Move("Wide Guard", "tough", 4),
    #beauty (done)
    "Flower Shield": Move("Flower Shield", "beauty", 4),
    "Heal Bell": Move("Heal Bell", "beauty", 4),
    "Mist": Move("Mist", "beauty", 4),
    #clever (done)
    "Aromatherapy": Move("Aromatherapy", "clever", 4),
    #cute (done)
    "Amnesia": Move("Amnesia", "cute", 4, True, ["Baton Pass", "Stored Power"]),
    "Bounce": Move("Bounce", "cute", 4),
    "Cotton Guard": Move("Cotton Guard", "cute", 4, True, ["Baton Pass", "Stored Power"]),
    "Hold Hands": Move("Hold Hands", "cute", 4, True, ["Circle Throw", "Seismic Toss", "Sky Drop", "Smack Down", "Storm Throw", "Vital Throw"]),
    "Minimize": Move("Minimize", "cute", 4),
    "Rest": Move("Rest", "cute", 4, True, ["Snore", "Sleep Talk"]),
    
    #== Gets the Pokemon pumped up. Helps prevent nervousness, too (5) == DONE
    #cool (done)
    "Bulk Up": Move("Bulk Up", "cool", 5),
    "Double Team": Move("Double Team", "cool", 5),
    "Dragon Dance": Move("Dragon Dance", "cool", 5),
    "Focus Energy": Move("Focus Energy", "cool", 5, True, ["Aeroblast", "Attack Order", "Blaze Kick", "Cross Poison", "Drill Run", "Karate Chop", "Leaf Blade", "Night Slash", "Poison Tail", "Psycho Cut", "Shadow Claw", "Spacial Rend", "Stone Edge"]),
    #tough (done)
    "Ancient Power": Move("Ancient Power", "tough", 5),
    "Coil": Move("Coil", "tough", 5),
    "Rototiller": Move("Rototiller", "tough", 5, True, ["Bullet Seed", "Leech Seed", "Seed Bomb", "Worry Seed"]),
    "Stockpile": Move("Stockpile", "tough", 5, True, ["Spit Up", "Swallow"]),
    #beauty (done)
    "Aqua Ring": Move("Aqua Ring", "beauty", 5),
    "Aromatic Mist": Move("Aromatic Mist", "beauty", 5),
    "Autotomize": Move("Autotomize", "beauty", 5, True, ["Baton Pass", "Electro Ball"]),
    "Cosmic Power": Move("Cosmic Power", "beauty", 5),
    "Geomancy": Move("Geomancy", "beauty", 5),
    "Growth": Move("Growth", "beauty", 5),
    "Meditate": Move("Meditate", "beauty", 5),
    "Ominous Wind": Move("Ominous Wind", "beauty", 5),
    "Quiver Dance": Move("Quiver Dance", "beauty", 5),
    "Silver Wind": Move("Silver Wind", "beauty", 5),
    "Swords Dance": Move("Swords Dance", "beauty", 5),
    "Tail Glow": Move("Tail Glow", "beauty", 5),
    #clever (done)
    "Calm Mind": Move("Calm Mind", "clever", 5, True, ["Baton Pass", "Stored Power"]),
    "Charge": Move("Charge", "clever", 5, True, ["Bolt Strike", "Charge Beam", "Discharge", "Electro Ball", "Fusion Bolt", "Nuzzle", "Parabolic Charge", "Shock Wave", "Spark", "Thunder", "Thunder Fang", "Thunder Punch", "Thunder Shock", "Thunderbolt", "Volt Switch", "Volt Tackle"]),
    "Ingrain": Move("Ingrain", "clever", 5),
    "Leech Seed": Move("Leech Seed", "clever", 5),
    "Magnetic Flux": Move("Magnetic Flux", "clever", 5),
    "Nasty Plot": Move("Nasty Plot", "clever", 5, True, ["Baton Pass", "Stored Power"]),
    "Shift Gear": Move("Shift Gear", "clever", 5, True, ["Gear Grind"]),
    #cute (done)
    "Hone Claws": Move("Hone Claws", "cute", 5, True, ["Baton Pass", "Stored Power"]),
    "Lucky Chant": Move("Lucky Chant", "cute", 5),
    "Sharpen": Move("Sharpen", "cute", 5),
    
    #== Works well if the user is pumped up (6) == DONE
    #cool (done)
    "Acrobatics": Move("Acrobatics", "cool", 6),
    "Flame Charge": Move("Flame Charge", "cool", 6),
    "Techno Blast": Move("Techno Blast", "cool", 6),
    #tough (done)
    "Belch": Move("Belch", "tough", 6),
    "Power-Up Punch": Move("Power-Up Punch", "tough", 6),
    "Spit Up": Move("Spit Up", "tough", 6),
    #beauty (done)
    "Charge Beam": Move("Charge Beam", "beauty", 6),
    "Fiery Dance": Move("Fiery Dance", "beauty", 6),
    #clever (done)
    "Beat Up": Move("Beat Up", "clever", 6),
    "Secret Power": Move("Secret Power", "clever", 6),
    "Stored Power": Move("Stored Power", "clever", 6),
    #cute (done)
    "Baton Pass": Move("Baton Pass", "cute", 6),
    "Last Resort": Move("Last Resort", "cute", 6),
    
    #== Works great if the user goes first this turn (7) == DONE
    #cool (done)
    "Aerial Ace": Move("Aerial Ace", "cool", 7),
    "Defog": Move("Defog", "cool", 7),
    "Magnet Bomb": Move("Magnet Bomb", "cool", 7),
    "Quick Guard": Move("Quick Guard", "cool", 7),
    "Shock Wave": Move("Shock Wave", "cool", 7),
    "Swift": Move("Swift", "cool", 7),
    #tough (done)
    "Noble Roar": Move("Noble Roar", "tough", 7),
    #beauty (done)
    "Aura Sphere": Move("Aura Sphere", "beauty", 7),
    "Clear Smog": Move("Clear Smog", "beauty", 7),
    "Magical Leaf": Move("Magical Leaf", "beauty", 7),
    #clever (done)
    "Feint Attack": Move("Feint Attack", "clever", 7),
    "Miracle Eye": Move("Miracle Eye", "clever", 7, True, ["Fissure", "Guillotine", "Horn Drill", "Sheer Cold"]),
    "Shadow Punch": Move("Shadow Punch", "clever", 7),
    #cute (done)
    "Disarming Voice": Move("Disarming Voice", "cute", 7),
    "Milk Drink": Move("Milk Drink", "cute", 7),
    "Soft-Boiled": Move("Soft-Boiled", "cute", 7, True, ["Egg Bomb"]),
    
    #== Works great if the user goes last this turn (8) == DONE
    #cool (done)
    "Howl": Move("Howl", "cool", 8),
    "Metal Burst": Move("Metal Burst", "cool", 8),
    "Vital Throw": Move("Vital Throw", "cool", 8),
    #tough (done)
    "Counter": Move("Counter", "tough", 8),
    "Endeavor": Move("Endeavor", "tough", 8),
    "Focus Punch": Move("Focus Punch", "tough", 8),
    "Payback": Move("Payback", "tough", 8),
    "Revenge": Move("Revenge", "tough", 8),
    #beauty (done)
    "Feather Dance": Move("Feather Dance", "beauty", 8),
    "Magic Coat": Move("Magic Coat", "beauty", 8),
    "Mirror Coat": Move("Mirror Coat", "beauty", 8),
    #clever (done)
    "Psycho Shift": Move("Psycho Shift", "clever", 8),
    #cute (done)
    "Facade": Move("Facade", "cute", 8),
    "Growl": Move("Growl", "cute", 8),
    "Struggle Bug": Move("Struggle Bug", "cute", 8),
    "Tail Whip": Move("Tail Whip", "cute", 8),
    
    #== Works better the later it is used in a turn (9) == DONE
    #cool (done)
    "Fusion Bolt": Move("Fusion Bolt", "cool", 9),
    "Gyro Ball": Move("Gyro Ball", "cool", 9),
    "Reversal": Move("Reversal", "cool", 9),
    "Trump Card": Move("Trump Card", "cool", 9),
    #tough (done)
    "Low Kick": Move("Low Kick", "tough", 9),
    #beauty (done)
    "Fusion Flare": Move("Fusion Flare", "beauty", 9),
    #clever (done)
    "Assurance": Move("Assurance", "clever", 9),
    #cute (done)
    "Flail": Move("Flail", "cute", 9),
    "Grass Knot": Move("Grass Knot", "cute", 9),
    
    #== Effectiveness varies depending on when it is used (10) == DONE
    #cool (done)
    "Bullet Seed": Move("Bullet Seed", "cool", 10),
    "Fury Attack": Move("Fury Attack", "cool", 10),
    "Pin Missile": Move("Pin Missile", "cool", 10),
    "Spike Cannon": Move("Spike Cannon", "cool", 10),
    #tough (done)
    "Acupressure": Move("Acupressure", "tough", 10),
    "Arm Thrust": Move("Arm Thrust", "tough", 10),
    "Bone Rush": Move("Bone Rush", "tough", 10),
    "Comet Punch": Move("Comet Punch", "tough", 10),
    "Fury Swipes": Move("Fury Swipes", "tough", 10),
    "Rock Blast": Move("Rock Blast", "tough", 10),
    #beauty (done)
    "Icicle Spear": Move("Icicle Spear", "beauty", 10),
    "Moonlight": Move("Moonlight", "beauty", 10),
    "Morning Sun": Move("Morning Sun", "beauty", 10),
    "Tri Attack": Move("Tri Attack", "beauty", 10),
    #clever (done)
    "Psywave": Move("Psywave", "clever", 10),
    "Synthesis": Move("Synthesis", "clever", 10),
    #cute (done)
    "Assist": Move("Assist", "cute", 10),
    "Barrage": Move("Barrage", "cute", 10),
    "Double Slap": Move("Double Slap", "cute", 10),
    "Metronome": Move("Metronome", "cute", 10),
    "Sleep Talk": Move("Sleep Talk", "cute", 10),
    "Tail Slap": Move("Tail Slap", "cute", 10),
    
    #== A very appealing move, but after using this move, the user is more easily startled (11) == DONE
    #cool (done)
    "Brave Bird": Move("Brave Bird", "cool", 11),
    "Flare Blitz": Move("Flare Blitz", "cool", 11),
    "High Jump Kick": Move("High Jump Kick", "cool", 11),
    "Jump Kick": Move("Jump Kick", "cool", 11),
    "Outrage": Move("Outrage", "cool", 11),
    "Submission": Move("Submission", "cool", 11),
    "V-create": Move("V-create", "cool", 11),
    "Volt Tackle": Move("Volt Tackle", "cool", 11),
    #tough (done)
    "Close Combat": Move("Close Combat", "tough", 11),
    "Double-Edge": Move("Double-Edge", "tough", 11),
    "Hammer Arm": Move("Hammer Arm", "tough", 11),
    "Head Charge": Move("Head Charge", "tough", 11),
    "Head Smash": Move("Head Smash", "tough", 11),
    "Superpower": Move("Superpower", "tough", 11),
    "Take Down": Move("Take Down", "tough", 11),
    "Thrash": Move("Thrash", "tough", 11),
    "Wild Charge": Move("Wild Charge", "tough", 11),
    "Wood Hammer": Move("Wood Hammer", "tough", 11),
    #beauty (done)
    "Draco Meteor": Move("Draco Meteor", "beauty", 11),
    "Dragon Ascent": Move("Dragon Ascent", "beauty", 11),
    "Eruption": Move("Eruption", "beauty", 11),
    "Leaf Storm": Move("Leaf Storm", "beauty", 11),
    "Light of Ruin": Move("Light of Ruin", "beauty", 11),
    "Overheat": Move("Overheat", "beauty", 11),
    "Petal Dance": Move("Petal Dance", "beauty", 11),
    "Seed Flare": Move("Seed Flare", "beauty", 11),
    "Spacial Rend": Move("Spacial Rend", "beauty", 11),
    "Water Spout": Move("Water Spout", "beauty", 11),
    #clever (done)
    "Psycho Boost": Move("Psycho Boost", "clever", 11),
    #cute (done)
    "Belly Drum": Move("Belly Drum", "cute", 11),
    
    #== User cannot act in the next turn (12) == DONE
    #cool (done)
    "Hyper Beam": Move("Hyper Beam", "cool", 12),
    "Frenzy Plant": Move("Frenzy Plant", "cool", 12),
    #tough (done)
    "Boomburst": Move("Boomburst", "tough", 12),
    "Giga Impact": Move("Giga Impact", "tough", 12),
    "Grudge": Move("Grudge", "tough", 12),
    "Rock Wrecker": Move("Rock Wrecker", "tough", 12),
    #beauty (done)
    "Blast Burn": Move("Blast Burn", "beauty", 12),
    "Hydro Cannon": Move("Hydro Cannon", "beauty", 12),
    "Roar of Time": Move("Roar of Time", "beauty", 12),
    #clever (N/A)
    #cute (done)
    "Teeter Dance": Move("Teeter Dance", "cute", 12),
    
    #== A move of huge appeal, but using it prevents the user from taking further contest moves (13) == DONE
    #cool (N/A)
    #tough (done)
    "Final Gambit": Move("Final Gambit", "tough", 13),
    "Memento": Move("Memento", "tough", 13),
    #beauty (done)
    "Explosion": Move("Explosion", "beauty", 13),
    "Healing Wish": Move("Healing Wish", "beauty", 13),
    "Lunar Dance": Move("Lunar Dance", "beauty", 13),
    "Self-Destruct": Move("Self-Destruct", "beauty", 13),
    #clever (done)
    "Destiny Bond": Move("Destiny Bond", "clever", 13),
    #cute (N/A)
    
    #== Makes the remaining Pokemon nervous (14) == DONE
    #cool (done)
    "Stealth Rock": Move("Stealth Rock", "cool", 14, True, ["Circle Throw", "Dragon Tail", "Whirlwind", "Roar"]),
    #tough (done)
    "Scald": Move("Scald", "tough", 14),
    "Torment": Move("Torment", "tough", 14, True, ["Counter", "Destiny Bond", "Grudge", "King's Shield", "Metal Burst", "Mirror Coat", "Spite"]),
    #beauty (done)
    "Mean Look": Move("Mean Look", "beauty", 14, True, ["Explosion", "Memento", "Perish Song", "Self-Destruct"]),
    "Relic Song": Move("Relic Song", "beauty", 14),
    #clever (done)
    "Dark Void": Move("Dark Void", "clever", 14, True, ["Dream Eater", "Hex", "Nightmare", "Wake-Up Slap"]),
    "Disable": Move("Disable", "clever", 14),
    "Flatter": Move("Flatter", "clever", 14),
    "Gravity": Move("Gravity", "clever", 14),
    "Magnet Rise": Move("Magnet Rise", "clever", 14),
    "Spider Web": Move("Spider Web", "clever", 14, True, ["Explosion", "Memento", "Perish Song", "Self-Destruct"]),
    "Spikes": Move("Spikes", "clever", 14, True, ["Circle Throw", "Dragon Tail", "Roar", "Whirlwind"]),
    "Telekinesis": Move("Telekinesis", "clever", 14),
    "Toxic Spikes": Move("Toxic Spikes", "clever", 14, True, ["Hex", "Venom Drench", "Venoshock", "Circle Throw", "Dragon Tail", "Roar", "Whirlwind"]),
    "Worry Seed": Move("Worry Seed", "clever", 14),
    #cute (done)
    "Attract": Move("Attract", "cute", 14),
    "Block": Move("Block", "cute", 14, True, ["Explosion", "Memento", "Perish Song", "Self-Destruct"]),
    "Encore": Move("Encore", "cute", 14, True, ["Counter", "Destiny Bond", "Grudge", "King's Shield", "Metal Burst", "Mirror Coat", "Spite"]),
    "Sing": Move("Sing", "cute", 14, True, ["Dream Eater", "Hex", "Nightmare", "Wake-Up Slap"]),
    "Sweet Kiss": Move("Sweet Kiss", "cute", 14),
    "Yawn": Move("Yawn", "cute", 14, True, ["Dream Eater", "Hex", "Nightmare", "Wake-Up Slap"]),
    
    #== Excites the audience a lot if used first (15) == DONE
    #cool (done)
    "Electro Ball": Move("Electro Ball", "cool", 15),
    #tough (done)
    "Hyperspace Fury": Move("Hyperspace Fury", "tough", 15),
    "Work Up": Move("Work Up", "tough", 15),
    #beauty (done)
    "Grassy Terrain": Move("Grassy Terrain", "beauty", 15),
    "Misty Terrain": Move("Misty Terrain", "beauty", 15),
    "Origin Pulse": Move("Origin Pulse", "beauty", 15),
    #clever (done)
    "Crafty Shield": Move("Crafty Shield", "clever", 15),
    "Electric Terrain": Move("Electric Terrain", "clever", 15),
    "Hyperspace Hole": Move("Hyperspace Hole", "clever", 15),
    "Sucker Punch": Move("Sucker Punch", "clever", 15),
    #cute (N/A)
    
    #== Excites the audience a lot if used last (16) == DONE
    #cool (done)
    "Aeroblast": Move("Aeroblast", "cool", 16),
    "Parting Shot": Move("Parting Shot", "cool", 16),
    "Precipice Blades": Move("Precipice Blades", "cool", 16),
    #tough (done)
    "Heat Crash": Move("Heat Crash", "tough", 16),
    "Heavy Slam": Move("Heavy Slam", "tough", 16),
    "Shell Smash": Move("Shell Smash", "tough", 16, True, ["Baton Pass", "Electro Ball"]),
    #beauty (done)
    "Diamond Storm": Move("Diamond Storm", "beauty", 16),
    "Doom Desire": Move("Doom Desire", "beauty", 16),
    "Icicle Crash": Move("Icicle Crash", "beauty", 16),
    "Sacred Fire": Move("Sacred Fire", "beauty", 16),
    "Steam Eruption": Move("Steam Eruption", "beauty", 16),
    #clever (N/A)
    #cute (done)
    "Wish": Move("Wish", "cute", 16, True, ["Bestow", "Fling", "Present"]),
    
    #== Excites the audience in any kind of contest (17) == DONE
    #cool (done)
    "Sacred Sword": Move("Sacred Sword", "cool", 17),
    "Storm Throw": Move("Storm Throw", "cool", 17),
    #tough (done)
    "Chip Away": Move("Chip Away", "tough", 17),
    "Flying Press": Move("Flying Press", "tough", 17),
    #beauty (done)
    "Fire Pledge": Move("Fire Pledge", "beauty", 17),
    "Grass Pledge": Move("Grass Pledge", "beauty", 17),
    "Heal Pulse": Move("Heal Pulse", "beauty", 17),
    "Water Pledge": Move("Water Pledge", "beauty", 17),
    #clever (done)
    "Pay Day": Move("Pay Day", "clever", 17),
    #cute (done)
    "Celebrate": Move("Celebrate", "cute", 17, True, ["Bestow", "Fling", "Present"]),
    "Happy Hour": Move("Happy Hour", "cute", 17, True, ["Bestow", "Fling", "Present"]),
    "Mud Sport": Move("Mud Sport", "cute", 17),
    "Water Sport": Move("Water Sport", "cute", 17),
    
    #== Works better the more the crowd is excited (18) == DONE
    #cool (done)
    "Fell Stinger": Move("Fell Stinger", "cool", 18),
    "Mega Kick": Move("Mega Kick", "cool", 18),
    "Rapid Spin": Move("Rapid Spin", "cool", 18),
    "Thunder": Move("Thunder", "cool", 18),
    #tough (done)
    "Magnitude": Move("Magnitude", "tough", 18),
    "Power Whip": Move("Power Whip", "tough", 18),
    #beauty (done)
    "Fire Blast": Move("Fire Blast", "beauty", 18),
    "Hydro Pump": Move("Hydro Pump", "beauty", 18),
    "Nature Power": Move("Nature Power", "beauty", 18),
    "Rain Dance": Move("Rain Dance", "beauty", 18, True, ["Hurricane", "Soak", "Thunder", "Water Sport", "Weather Ball"]),
    "Sunny Day": Move("Sunny Day", "beauty", 18, True, ["Growth", "Moonlight", "Morning Sun", "Solar Beam", "Synthesis", "Weather Ball"]),
    #clever (done)
    "Natural Gift": Move("Natural Gift", "clever", 18),
    #cute (done)
    "Bestow": Move("Bestow", "cute", 18),
    "Play Nice": Move("Play Nice", "cute", 18, True, ["Circle Throw", "Seismic Toss", "Sky Drop", "Smack Down", "Storm Throw", "Vital Throw", "Wake-Up Slap"]),
    
    #== An appealing move that can be used repeatedly without boring the audience (19) == DONE
    #cool (done)
    "Blaze Kick": Move("Blaze Kick", "cool", 19),
    "Dragon Rage": Move("Dragon Rage", "cool", 19),
    "Fury Cutter": Move("Fury Cutter", "cool", 19),
    "Hyper Fang": Move("Hyper Fang", "cool", 19),
    "Leaf Blade": Move("Leaf Blade", "cool", 19),
    "Leaf Tornado": Move("Leaf Tornado", "cool", 19),
    "Megahorn": Move("Megahorn", "cool", 19),
    "Meteor Mash": Move("Meteor Mash", "cool", 19),
    "Night Daze": Move("Night Daze", "cool", 19),
    "Psystrike": Move("Psystrike", "cool", 19),
    "Razor Shell": Move("Razor Shell", "cool", 19),
    "Searing Shot": Move("Searing Shot", "cool", 19),
    "Sonic Boom": Move("Sonic Boom", "cool", 19),
    "Triple Kick": Move("Triple Kick", "cool", 19),
    #tough (done)
    "Bone Club": Move("Bone Club", "tough", 19),
    "Crabhammer": Move("Crabhammer", "tough", 19),
    "Crush Grip": Move("Crush Grip", "tough", 19),
    "Mega Punch": Move("Mega Punch", "tough", 19),
    "Octazooka": Move("Octazooka", "tough", 19),
    "Seismic Toss": Move("Seismic Toss", "tough", 19),
    "Steamroller": Move("Steamroller", "tough", 19),
    #beauty (done)
    "Blue Flare": Move("Blue Flare", "beauty", 19),
    "Bolt Strike": Move("Bolt Strike", "beauty", 19),
    "Echoed Voice": Move("Echoed Voice", "beauty", 19),
    "Freeze-Dry": Move("Freeze-Dry", "beauty", 19),
    "Judgement": Move("Judgement", "beauty", 19),
    "Mystical Fire": Move("Mystical Fire", "beauty", 19),
    "Secret Sword": Move("Secret Sword", "beauty", 19),
    "Weather Ball": Move("Weather Ball", "beauty", 19),
    #clever (done)
    "Attack Order": Move("Attack Order", "clever", 19),
    "Hidden Power": Move("Hidden Power", "clever", 19),
    "Kinesis": Move("Kinesis", "clever", 19),
    "Night Shade": Move("Night Shade", "clever", 19),
    "Transform": Move("Transform", "clever", 19),
    #cute (done)
    "Rollout": Move("Rollout", "cute", 19),
    "Present": Move("Present", "cute", 19),
    "Heart Stamp": Move("Heart Stamp", "cute", 19),
    
    #== Startles the last Pokemon to act before the user (20) == DONE
    #cool (done)
    "Dragon Breath": Move("Dragon Breath", "cool", 20),
    #tough (done)
    "Bite": Move("Bite", "tough", 20),
    "Sludge": Move("Sludge", "tough", 20),
    #beauty (done)
    "Aurora Beam": Move("Aurora Beam", "beauty", 20),
    "Bubble Beam": Move("Bubble Beam", "beauty", 20),
    "Mirror Shot": Move("Mirror Shot", "beauty", 20),
    #clever (done)
    "Gust": Move("Gust", "clever", 20),
    "Knock Off": Move("Knock Off", "clever", 20),
    "Low Sweep": Move("Low Sweep", "clever", 20),
    "Mega Drain": Move("Mega Drain", "clever", 20),
    "Poison Sting": Move("Poison Sting", "clever", 20),
    "Smokescreen": Move("Smokescreen", "clever", 20),
    "String Shot": Move("String Shot", "clever", 20, True, ["Electroweb", "Spider Web", "Sticky Web"]),
    #cute (done)
    "Astonish": Move("Astonish", "cute", 20),
    "Fake Out": Move("Fake Out", "cute", 20),
    "Frustration": Move("Frustration", "cute", 20),
    "Lick": Move("Lick", "cute", 20),
    "Mud Bomb": Move("Mud Bomb", "cute", 20),
    
    #== Badly startles the last Pokemon to act before the user (21) == DONE
    #cool (done)
    "Air Slash": Move("Air Slash", "cool", 21),
    "Crush Claw": Move("Crush Claw", "cool", 21),
    #tough (done)
    "Body Slam": Move("Body Slam", "tough", 21),
    "Crunch": Move("Crunch", "tough", 21),
    #beauty (done)
    "Bug Buzz": Move("Bug Buzz", "beauty", 21),
    "Ice Beam": Move("Ice Beam", "beauty", 21),
    "Inferno": Move("Inferno", "beauty", 21, True, ["Hex"]),
    "Moonblast": Move("Moonblast", "beauty", 21),
    "Psyshock": Move("Psyshock", "beauty", 21),
    #clever (done)
    "Giga Drain": Move("Giga Drain", "clever", 21),
    #cute (N/A)
    
    #== Startles the all of the Pokemon to act before the user (22) == DONE
    #cool (done)
    "Hyper Voice": Move("Hyper Voice", "cool", 22),
    #tough (done)
    "Bulldoze": Move("Bulldoze", "tough", 22),
    "Lava Plume": Move("Lava Plume", "tough", 22),
    "Muddy Water": Move("Muddy Water", "tough", 22),
    "Rock Slide": Move("Rock Slide", "tough", 22),
    #beauty (done)
    "Discharge": Move("Discharge", "beauty", 22),
    "Heat Wave": Move("Heat Wave", "beauty", 22),
    "Land's Wrath": Move("Land's Wrath", "beauty", 22),
    "Petal Blizzard": Move("Petal Blizzard", "beauty", 22),
    "Surf": Move("Surf", "beauty", 22),
    #clever (N/A)
    #cute (N/A)
    
    #== Badly startles all of the Pokemon to act before the user (23) == DONE
    #cool (done)
    "Thunder Wave": Move("Thunder Wave", "cool", 23, True, ["Hex", "Smelling Salts"]),
    "Mat Block": Move("Mat Block", "cool", 23),
    #tough (done)
    "Glare": Move("Glare", "tough", 23, True, ["Hex", "Smelling Salts"]),
    "Rage": Move("Rage", "tough", 23),
    #beauty (done)
    "Blizzard": Move("Blizzard", "beauty", 23),
    "Spore": Move("Spore", "beauty", 23, True, ["Dream Eater", "Hex", "Nightmare", "Wake-Up Slap"]),
    #clever (done)
    "Eerie Impulse": Move("Eerie Impulse", "clever", 23),
    "Hypnosis": Move("Hypnosis", "clever", 23, True, ["Dream Eater", "Hex", "Nightmare", "Wake-Up Slap"]),
    "Metal Sound": Move("Metal Sound", "clever", 23),
    "Nightmare": Move("Nightmare", "clever", 23),
    "Sleep Powder": Move("Sleep Powder", "clever", 23, True, ["Dream Eater", "Hex", "Nightmare", "Wake-Up Slap"]),
    #cute (N/A)
    
    #== Affected by how well the previous Pokemon's move went (24) == DONE
    #cool (done)
    "Cross Chop": Move("Cross Chop", "cool", 24),
    "Drill Peck": Move("Drill Peck", "cool", 24),
    "Night Slash": Move("Night Slash", "cool", 24),
    "Razor Wind": Move("Razor Wind", "cool", 24),
    "Retaliate": Move("Retaliate", "cool", 24),
    "Sky Attack": Move("Sky Attack", "cool", 24),
    "Solar Beam": Move("Solar Beam", "cool", 24),
    "Steel Wing": Move("Steel Wing", "cool", 24),
    #tough (done)
    "Brine": Move("Brine", "tough", 24),
    "Dragon Rush": Move("Dragon Rush", "tough", 24),
    "Drill Run": Move("Drill Run", "tough", 24),
    "Skull Bash": Move("Skull Bash", "tough", 24),
    "Smelling Salts": Move("Smelling Salts", "tough", 24),
    "Stone Edge": Move("Stone Edge", "tough", 24),
    "Wake-Up Slap": Move("Wake-Up Slap", "tough", 24),
    #beauty (done)
    "Avalanche": Move("Avalanche", "beauty", 24),
    "Flame Wheel": Move("Flame Wheel", "beauty", 24),
    "Freeze Shock": Move("Freeze Shock", "beauty", 24),
    "Ice Burn": Move("Ice Burn", "beauty", 24),
    #clever (N/A)
    #cute (N/A)
    
    #== Badly startles all Pokemon that successfully showed their appeal (25) == DONE
    #cool (done)
    "Guillotine": Move("Guillotine", "cool", 25),
    "Horn Drill": Move("Horn Drill", "cool", 25),
    "Zap Cannon": Move("Zap Cannon", "cool", 25, True, ["Hex", "Smelling Salts"]),
    #tough (done)
    "Earthquake": Move("Earthquake", "tough", 25),
    "Fissure": Move("Fissure", "tough", 25),
    "Gunk Shot": Move("Gunk Shot", "tough", 25),
    "Hurricane": Move("Hurricane", "tough", 25),
    "Sandstorm": Move("Sandstorm", "tough", 25, True, ["Sand Attack", "Sand Tomb", "Weather Ball"]),
    "Spite": Move("Spite", "tough", 25),
    "Super Fang": Move("Super Fang", "tough", 25),
    #beauty (done)
    "Hail": Move("Hail", "beauty", 25, True, ["Blizzard", "Glaciate", "Icicile Crash", "Icy Wind", "Powder Snow", "Weather Ball"]),
    "Sheer Cold": Move("Sheer Cold", "beauty", 25),
    #clever (done)
    "Forest's Curse": Move("Forest's Curse", "clever", 25),
    "Mist Ball": Move("Mist Ball", "clever", 25),
    "Stun Spore": Move("Stun Spore", "clever", 25, True, ["Hex", "Smelling Salts"]),
    #cute (N/A)
    
    #== Badly startles Pokemon that the audience has high expectations of (26) == DONE
    #cool (done)
    "Dynamic Punch": Move("Dynamic Punch", "cool", 26),
    "Leer": Move("Leer", "cool", 26),
    "Punishment": Move("Punishment", "cool", 26),
    #tough (done)
    "Sludge Bomb": Move("Sludge Bomb", "tough", 26),
    "Smack Down": Move("Smack Down", "tough", 26),
    "Sticky Web": Move("Sticky Web", "tough", 26),
    "Wring Out": Move("Wring Out", "tough", 26),
    #beauty (done)
    "Cotton Spore": Move("Cotton Spore", "beauty", 26),
    "Electroweb": Move("Electroweb", "beauty", 26),
    #clever (done)
    "Confuse Ray": Move("Confuse Ray", "clever", 26),
    "Taunt": Move("Taunt", "clever", 26, True, ["Counter", "Destiny Bond", "Grudge", "King's Shield", "Metal Burst", "Mirror Coat", "Spite"]),
    #cute (done)
    "Charm": Move("Charm", "cute", 26),
    "Soak": Move("Soak", "cute", 26),
    "Uproar": Move("Uproar", "cute", 26),
    
    #== Badly startles Pokemon that used a move of the same type (27) == DONE
    #cool (done)
    "Cross Poison": Move("Cross Poison", "cool", 27),
    "Double Hit": Move("Double Hit", "cool", 27),
    "Double Kick": Move("Double Kick", "cool", 27),
    "Extrasensory": Move("Extrasensory", "cool", 27),
    "Sky Uppercut": Move("Sky Uppercut", "cool", 27),
    "Twineedle": Move("Twineedle", "cool", 27),
    "X-Scissor": Move("X-Scissor", "cool", 27),
    #tough (done)
    "Bonemerang": Move("Bonemerang", "tough", 27),
    "Dual Chop": Move("Dual Chop", "tough", 27),
    #beauty (done)
    "Acid Spray": Move("Acid Spray", "beauty", 27),
    "Thousand Arrows": Move("Thousand Arrows", "beauty", 27),
    #clever (done)
    "Electrify": Move("Electrify", "clever", 27),
    "Foresight": Move("Foresight", "clever", 27),
    "Heal Order": Move("Heal Order", "clever", 27),
    "Hex": Move("Hex", "clever", 27),
    "Luster Purge": Move("Luster Purge", "clever", 27),
    "Pursuit": Move("Pursuit", "clever", 27),
    "Switcheroo": Move("Switcheroo", "clever", 27),
    "Trick": Move("Trick", "clever", 27),
    #cute (done)
    "Entrainment": Move("Entrainment", "cute", 27, True, ["Circle Throw", "Seismic Toss", "Sky Drop", "Smack Down", "Storm Throw", "Vital Throw"]),
    "Nuzzle": Move("Nuzzle", "cute", 27, True, ["Hex", "Smelling Salts"]),
    "Trick-or-Treat": Move("Trick-or-Treat", "cute", 27),
    
    #== Shows off the Pokemon's appeal about as well as all the moves before it this turn (28) == DONE
    #cool (done)
    "Oblivion Wing": Move("Oblivion Wing", "cool", 28),
    #tough (N/A)
    #beauty (N/A)
    #clever (done)
    "Camouflage": Move("Camouflage", "clever", 28),
    "Guard Split": Move("Guard Split", "clever", 28),
    "Guard Swap": Move("Guard Swap", "clever", 28),
    "Heart Swap": Move("Heart Swap", "clever", 28),
    "Pain Split": Move("Pain Split", "clever", 28),
    "Parabolic Charge": Move("Parabolic Charge", "clever", 28, True, ["Electrify"]),
    "Power Split": Move("Power Split", "clever", 28),
    "Power Swap": Move("Power Swap", "clever", 28),
    #cute (done)
    "Draining Kiss": Move("Draining Kiss", "cute", 28),
    
    #== Makes the audience quickly grow bored when an appeal move has little effect (29) == DONE
    #cool (done)
    "False Swipe": Move("False Swipe", "cool", 29),
    "Hold Back": Move("Hold Back", "cool", 29),
    "Volt Switch": Move("Volt Switch", "cool", 29),
    #tough (done)
    "Snarl": Move("Snarl", "tough", 29),
    #beauty (done)
    "Frost Breath": Move("Frost Breath", "beauty", 29),
    "Icy Wind": Move("Icy Wind", "beauty", 29),
    "Lovely Kiss": Move("Lovely Kiss", "beauty", 29, True, ["Dream Eater", "Hex", "Nightmare", "Wake-Up Slap"]),
    "Perish Song": Move("Perish Song", "beauty", 29),
    #clever (done)
    "Powder": Move("Powder", "clever", 29),
    "Roost": Move("Roost", "clever", 29),
    #cute (done)
    "Captivate": Move("Captivate", "cute", 29),
    "Fake Tears": Move("Fake Tears", "cute", 29),
    "Slack Off": Move("Slack Off", "cute", 29),
    "Snore": Move("Snore", "cute", 29),
    "Splash": Move("Splash", "cute", 29),
    "U-turn": Move("U-turn", "cute", 29),
    
    #== Works well if it is the same type as the move used by the last Pokemon (30) == DONE
    #cool (N/A)
    #tough (N/A)
    #beauty (done)
    "Conversion": Move("Conversion", "beauty", 30),
    "Conversion 2": Move("Conversion 2", "beauty", 30),
    "Round": Move("Round", "beauty", 30),
    "Venoshock": Move("Venoshock", "beauty", 30),
    #clever (done)
    "Dream Eater": Move("Dream Eater", "clever", 30),
    "Future Sight": Move("Future Sight", "clever", 30),
    "Power Trick": Move("Power Trick", "clever", 30),
    "Psych Up": Move("Psych Up", "clever", 30),
    "Recover": Move("Recover", "clever", 30),
    "Reflect Type": Move("Reflect Type", "clever", 30, True, ["Synchronoise"]),
    "Synchronoise": Move("Synchronoise", "clever", 30),
    #cute (N/A)
    
    #== Brings down the energy of any Pokemon that have already used a move this turn (31) == DONE
    #cool (N/A)
    #tough (done)
    "Constrict": Move("Constrict", "tough", 31),
    "Gastro Acid": Move("Gastro Acid", "tough", 31),
    "Scary Face": Move("Scary Face", "tough", 31),
    "Sludge Wave": Move("Sludge Wave", "tough", 31),
    "Thousand Waves": Move("Thousand Waves", "tough", 31),
    #beauty (done)
    "Haze": Move("Haze", "beauty", 31),
    #clever (done)
    "Acid": Move("Acid", "clever", 31),
    "Embargo": Move("Embargo", "clever", 31),
    "Poison Powder": Move("Poison Powder", "clever", 31, True, ["Hex", "Venom Drench", "Venoshock"]),
    "Poison Tail": Move("Poison Tail", "clever", 31),
    "Toxic": Move("Toxic", "clever", 31, True, ["Hex", "Venom Drench", "Venoshock"]),
    "Venom Drench": Move("Venom Drench", "clever", 31),
    #cute (done)
    "Bug Bite": Move("Bug Bite", "cute", 31),
    "Chatter": Move("Chatter", "cute", 31),
    "Confide": Move("Confide", "cute", 31),
    "Fling": Move("Fling", "cute", 31),
    "Mud-Slap": Move("Mud-Slap", "cute", 31),
    "Play Rough": Move("Play Rough", "cute", 31),
    "Pluck": Move("Pluck", "cute", 31),
    "Simple Beam": Move("Simple Beam", "cute", 31),
    "Swagger": Move("Swagger", "cute", 31),
    "Tickle": Move("Tickle", "cute", 31),
    
    #== Makes audience expect little of other contestants (32) == DONE
    #cool (N/A)
    #tough (done)
    "Incinerate": Move("Incinerate", "tough", 32),
    "Rock Climb": Move("Rock Climb", "tough", 32),
    #beauty (done)
    "Flame Burst": Move("Flame Burst", "beauty", 32),
    "Flash": Move("Flash", "beauty", 32),
    "Psybeam": Move("Psybeam", "beauty", 32),
    "Signal Beam": Move("Signal Beam", "beauty", 32),
    "Water Pulse": Move("Water Pulse", "beauty", 32),
    "Will-O-Wisp": Move("Will-O-Wisp", "beauty", 32, True, ["Hex"]),
    #clever (done)
    "Poison Gas": Move("Poison Gas", "clever", 32, True, ["Hex", "Venom Drench", "Venoshock"]),
    "Rock Tomb": Move("Rock Tomb", "clever", 32),
    "Screech": Move("Screech", "clever", 32),
    "Supersonic": Move("Supersonic", "clever", 32),
    #cute (done)
    "Dizzy Punch": Move("Dizzy Punch", "cute", 32),
    "Sand Attack": Move("Sand Attack", "cute", 32),
    
    #== Temporarily stops the crowd from growing excited (33) == DONE
    #cool (N/A)
    #tough (done)
    "Bind": Move("Bind", "tough", 33),
    "Clamp": Move("Clamp", "tough", 33),
    "Magma Storm": Move("Magma Storm", "tough", 33),
    "Sky Drop": Move("Sky Drop", "tough", 33),
    "Wrap": Move("Wrap", "tough", 33),
    #beauty (done)
    "Fire Spin": Move("Fire Spin", "beauty", 33),
    "Glaciate": Move("Glaciate", "beauty", 33),
    "Ice Ball": Move("Ice Ball", "beauty", 33),
    "Ion Deluge": Move("Ion Deluge", "beauty", 33),
    "Whirlpool": Move("Whirlpool", "beauty", 33),
    #clever (done)
    "Fairy Lock": Move("Fairy Lock", "clever", 33),
    "Heal Block": Move("Heal Block", "clever", 33),
    "Imprison": Move("Imprison", "clever", 33),
    "Magic Room": Move("Magic Room", "clever", 33),
    "Rage Powder": Move("Rage Powder", "clever", 33),
    "Sand Tomb": Move("Sand Tomb", "clever", 33),
    #cute (done)
    "Follow Me": Move("Follow Me", "cute", 33),
    "Infestation": Move("Infestation", "cute", 33),
    
    #== Shows off the Pokemon's appeal about as well as the move used just before it (34) == DONE
    #cool (N/A)
    #tough (done)
    "Drain Punch": Move("Drain Punch", "tough", 34),
    "Horn Leech": Move("Horn Leech", "tough", 34),
    "Thief": Move("Thief", "tough", 34),
    #beauty (N/A)
    #clever (done)
    "Foul Play": Move("Foul Play", "clever", 34),
    "Leech Life": Move("Leech Life", "clever", 34),
    "Mirror Move": Move("Mirror Move", "clever", 34),
    "Recycle": Move("Recycle", "clever", 34),
    "Sketch": Move("Sketch", "clever", 34),
    "Skill Swap": Move("Skill Swap", "clever", 34),
    "Snatch": Move("Snatch", "clever", 34),
    #cute (done)
    "Copycat": Move("Copycat", "cute", 34),
    "Covet": Move("Covet", "cute", 34, True, ["Bestow", "Fling", "Present"]),
    "Mimic": Move("Mimic", "cute", 34),
    "Role Play": Move("Role Play", "cute", 34),
    
    #== Scrambles the order in which Pokemon will move on the next turn (35) == DONE
    #cool (N/A)
    #tough (N/A)
    #beauty (N/A)
    #clever (done)
    "Ally Switch": Move("Ally Switch", "clever", 35),
    "Topsy-Turvy": Move("Topsy-Turvy", "clever", 35),
    "Trick Room": Move("Trick Room", "clever", 35),
    "Wonder Room": Move("Wonder Room", "clever", 35),
    #cute (N/A)
    
    #placeholder move
    "Struggle": Move("Struggle", "tough", 0)
}


#this dictionary keeps track of which categories are secondary to a given category
categorySecondaryType = {
    "cool": ["tough", "beauty"],
    "tough": ["clever", "cool"],
    "beauty": ["cool", "cute"],
    "clever": ["cute", "tough"],
    "cute": ["beauty", "clever"]
}