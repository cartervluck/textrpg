# [class, element, damage type]
# Common, uncommon, rare, mythical, legendary

import math
import random

#
#
#    CCCCCCC      LLLL             AAAAAAAAAA       SSSSSSSSSSSS    SSSSSSSSSSSS    EEEEEEEEEEEEEEEE    SSSSSSSSSSSS
#   CCCCCCCCC     LLLL            AAAAAAAAAAAA      SSSSSSSSSSSS    SSSSSSSSSSSS    EEEEEEEEEEEEEEEE    SSSSSSSSSSSS
#  CCCCCCCCCCC    LLLL           AAAAAAAAAAAAAA     SSSSSSSSSSSS    SSSSSSSSSSSS    EEEEEEEEEEEEEEEE    SSSSSSSSSSSS
# CCCCC   CCCC    LLLL           AAAA      AAAA     SSSS            SSSS            EEEE                SSSS        
# CCCC            LLLL          AAAA        AAAA    SSSS            SSSS            EEEE                SSSS        
#CCCC             LLLL          AAAA        AAAA    SSSS            SSSS            EEEE                SSSS        
#CCCC             LLLL          AAAAAAAAAAAAAAAA    SSSSSSSSSSSS    SSSSSSSSSSSS    EEEEEEEEEEEE        SSSSSSSSSSSS
#CCCC             LLLL          AAAAAAAAAAAAAAAA    SSSSSSSSSSSS    SSSSSSSSSSSS    EEEEEEEEEEEE        SSSSSSSSSSSS
#CCCC             LLLL          AAAA        AAAA    SSSSSSSSSSSS    SSSSSSSSSSSS    EEEE                SSSSSSSSSSSS
#CCCC             LLLL          AAAA        AAAA            SSSS            SSSS    EEEE                        SSSS
#CCCC             LLLL          AAAA        AAAA            SSSS            SSSS    EEEE                        SSSS
# CCCC            LLLL          AAAA        AAAA            SSSS            SSSS    EEEE                        SSSS
# CCCCC   CCCC    LLLL          AAAA        AAAA            SSSS            SSSS    EEEE                        SSSS
#  CCCCCCCCCCC    LLLLLLLLLL    AAAA        AAAA    SSSSSSSSSSSS    SSSSSSSSSSSS    EEEEEEEEEEEEEEEE    SSSSSSSSSSSS
#   CCCCCCCCC     LLLLLLLLLL    AAAA        AAAA    SSSSSSSSSSSS    SSSSSSSSSSSS    EEEEEEEEEEEEEEEE    SSSSSSSSSSSS
#    CCCCCCC      LLLLLLLLLL    AAAA        AAAA    SSSSSSSSSSSS    SSSSSSSSSSSS    EEEEEEEEEEEEEEEE    SSSSSSSSSSSS
#
#
#
#






#misc
def floatToPercent(floatNum):
	return str(math.floor(floatNum*100)) + "%"

#Map init
map = {
	'Obelisk': [],
	"CastleRoomMain": ["CastleCourtyard","CastleCorridor"],"CastleCorridor": ["CastleRoomMain"],"CastleCourtyard":["CastleRoomMain","CastleGate"],"CastleGate": ["CastleCourtyard","Village"],'CastleGate2': ['Village','CastleCourtyard'],
	"Village": ["CastleGate2","VillageHouse","VillageHeal","Cave1","Route1","Obelisk"],"VillageHouse":["Village"],'Cave1':['Village'],'VillageHeal':['Village'],
	'Route1': ['BabyBush','Village','Brush1'],'BabyBush': ['Route1'], 'Brush1': ['Route1','Town1'],
	'Town1': ['Brush1','Town1Shop','Town1Heal','Obelisk','Route2','Route3'],'Town1Heal': ['Town1'],
	'Route2': ['MaplebellForest','Town1'],
	'MaplebellForest': ['Route2','MaplebellAlcove','MB1'], 'MaplebellAlcove': ['MaplebellForest'], 'MB1': ['MaplebellForest','MB2','MB3'], 'MB2': ['MB1','MB4','MB5','MB6'], 'MB4': ['MB2'], 'MB5': ['MB2','MB7'], 'MB6': ['MB2','MB8','MB9'], 'MB8': ['MB6'], 'MB7': ['MB5'], 'MB9': ['MB6','MBOutlet'], 'MB3': ['MB1','MB10','MB11'], 'MB11': ['MB3'], 'MB10': ['MB3','MB12','MB13','MB14'], 'MB12': ['MB10'], 'MB13': ['MB10','MB15'], 'MB14': ['MB10','MB15','MB16'], 'MB16': ['MB14'], 'MB15': ['MB14','MB13'],
	'MBOutlet': ['MB9',''],

	'Hell': ['HellGate1']
}

locToReadableLoc = {'CastleRoomMain': 'CASTLE THRONE ROOM','CastleCourtyard': 'COURTYARD','CastleCorridor': 'CORRIDOR','CastleGate': 'GATE','Village': 'VILLAGE','CastleGate2': 'GATE', 'VillageHouse': 'RANDOM HOUSE', 'Cave1': 'INNOCENT-LOOKING CAVE', 'Route1': 'ROUTE 1','VillageHeal': 'THE DOCTOR\'S HOUSE','Obelisk': 'OBELISK','BabyBush': 'BUSHY GROVE','Brush1': 'FIELD','Town1': 'FERMI', 'Town1Shop': 'MERCHANT', 'Town1Heal': 'DOCTOR\'S HOUSE', 'Route2': 'ROUTE 2', 'Route3': 'ROUTE 3', 'Hell': 'HELL', 'HellGate1': 'HELL GATES','MaplebellForest': 'MAPLEBELL FOREST', 'MaplebellAlcove': 'ALCOVE', 'MB1': 'FOREST PATH', 'MB2': 'FOREST PATH', 'MB3': 'FOREST PATH', 'MB4': 'FOREST PATH', 'MB5': 'FOREST PATH', 'MB6': 'FOREST PATH', 'MB7': 'FOREST PATH', 'MB8': 'FOREST PATH', 'MB9': 'FOREST PATH', 'MB10': 'FOREST PATH', 'MB11': 'FOREST PATH', 'MB12': 'FOREST PATH', 'MB13': 'FOREST PATH', 'MB14': 'FOREST PATH', 'MB15': 'FOREST PATH', 'MB16': 'FOREST PATH', 'MBOutlet': 'FOREST ENTRANCE'}

locToDialog = {'Obelisk': '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n*This OBELISK has a mysterious presence*','CastleRoomMain': '*You should go out to the courtyard*\n*To perform an action, type the number that corrosponds with it, and hit enter.*','CastleCorridor': '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nThere\'s nothing here', 'CastleCourtyard': '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n*You see a very short man, attempting to sheath his sword.*\n*You walk up to him.*','CastleGate': '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n*You make out a figure guarding the gate as you approach.*\n*He notices you, and stands up a little straighter.*', 'Village': '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n*There are many houses in this village.*\n*There are also a few paths that you can take.*\n*That cave over there looks promising. It shouldn\'t be too hard to explore.*\n*There\'s also a mysterious obelisk*','CastleGate2': '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n*You make out a figure guarding the gate as you approach.*\n*He notices you, and stands up a little straighter.*','Route1': '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n*The path splits into two paths: a bushy grove, or a field of tall grass*','Brush1': '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n*You can hardly see over the brush...*','Town1': '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n*FERMI is a small town.*\n*You can buy some essentials here.*','Route2': '','Hell': '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n*YOU ARE LITERALLY IN HELL.*','Route2': '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n*You smile as you walk down the path.*','MaplebellForest':'\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n*This is a peaceful place*','MBOutlet': '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n*This is one entry point to the forest.*'}
def move(loc,char):
	inputLoc = "Not good if this"
	possLocs = range(0,len(map[loc]))
	for i in range(0,len(possLocs)):
		possLocs[i] = str(possLocs[i] + 1)
	while (not inputLoc in possLocs) and (inputLoc != "0"):
		for i in range(0,len(map[loc])):
			print str(i + 1) + ". " + locToReadableLoc[map[loc][i]]
		inputLoc = raw_input("Which location do you want to go to?\nLocation ")
		if inputLoc != "0":
			if not inputLoc in possLocs:
				print "That's not a valid location."
			elif map[char.loc][int(inputLoc)-1] == 'Obelisk':
				if not char.loc in map['Obelisk']:
					map['Obelisk'].append(char.loc)
			if inputLoc in possLocs:
				char.loc = map[loc][int(inputLoc) - 1]
		else:
			char.oldLoc = char.loc
			char.loc = "Inventory"

#DON'T USE THIS FUNCTION YET... NOT READY
def questLoc(questName,loc,char):
	if (not questName in char.activeQs) and (not questName in char.completedQs):
		#asfhajkfakj
		print 'You suck'

#Specific map stuff
villageHouses = ['Villager: "What are you doing in here?"','Villager: "How can I help you?"','Villager: "Please don\'t disturb me. I\'m trying to sleep."','Villager: "Do you know what privacy looks like?"','Villager: "I wasn\'t expecting you until 7!"','Villager: "Did you know you can access your inventory by pressing 0 while being prompeted to move?"']

#BATTLE STUFF

#restistantToChart: {"Water": ["Lava, Fire"]} #EXTEND

class Enemy:
	health = 0
	name = ""
	damage = 0
	level = 0
	maxHealth = 0
	def __init__(self,health,name,damage,level):
		self.health = health
		self.name = name
		self.damage = damage
		self.level = level
		self.maxHealth = health

def genEn(name,lv):
	hp = math.floor(random.randint(lv * 5,lv * 10))
	dmg = random.randint(lv,lv * 5)
	return Enemy(hp,name,dmg,lv)

def battle(char,enem):
	print "You plunge into combat with a level " + str(enem.level) + " " + enem.name + "."
	raw_input("Press Enter to continue. ")
	playerTurn = True
	while char.health > 0 and enem.health > 0:
		print "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n" + enem.name + ":\nHealth: " + str(enem.health) + "/" + str(enem.maxHealth) + "\n\nYou:\nHealth: " + str(char.health) + "/" + str(char.maxHealth)
		if playerTurn:
			if len(player1.inventory) > 0:
				for i in range(0,len(char.inventory)):
					print str(i + 1) + ". " + char.inventory[i].name
				inp = raw_input("What are you going to do?\nUse: ")
				if random.random() < char.inventory[int(inp)-1].critChance:
					print "Critical hit!"
					enem.health -= int(math.floor(char.inventory[int(inp)-1].damage * 1.5))
				else:
					enem.health -= char.inventory[int(inp)-1].damage
				char.health -= char.inventory[int(inp)-1].selfDamage
				if char.health > char.maxHealth:
					char.health = char.maxHealth
				char.inventory[int(inp)-1].uses -= 1
				if char.inventory[int(inp)-1].checkIfBroke():
					del char.inventory[int(inp)-1]
					del char.inventoryNames[int(inp)-1]
					#REMOVE ITEMS
			else:
				print "You have no items!\n1. FISTS"
				response = "-1"
				while response != "1":
					response = raw_input("What are you going to do?\nUse: ")
				enem.health -=1
		else:
			print "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n*The " + enem.name + " attacked!*\n" + enem.name + ":\nHealth: " + str(enem.health) + "\n\nYou:\nHealth: " + str(char.health)
			char.health -= enem.damage
			raw_input("Press Enter to continue. ")
			print "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n*The " + enem.name + " attacked!*\n" + enem.name + ":\nHealth: " + str(enem.health) + "\n\nYou:\nHealth: " + str(char.health)
			raw_input("Press Enter to continue. ")
		playerTurn = not playerTurn
	if char.health > 0:
		print "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nYou beat the " + enem.name + "!"
		expGained = enem.level * random.randint(1,15)
		print "You gained " + str(expGained) + " Experience."
		char.exp += expGained
		char.checkLvUp()
		goldGained = enem.level * random.randint(1,15)
		print "You gained " + str(goldGained) + " Gold."
		char.gold += goldGained
		return True
	else:
		player1.loc = 'CastleRoomMain'
		print "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n*You wake up, not realizing how you got here.*\n*You are fully healed*"
		player1.health = player1.maxHealth
		return False

encounterLocs = ['Brush1']

#Character init stuff... lists of classes, etc
allClasses = ['Knight','Mage','Archer']

#Weapon init stuff... names, class weapons, etc. Vars, lists, dicts
classWeapons = {'Knight' : ["Sword","Lance","Spear"],'Mage': ['Wand','Staff'],'Archer': ['Shortbow','Longbow','Crossbow']}#EXTEND
prefixes = ['Short','Long','Big','Small','Intense','Fierce','Meek','Huge','Miniscule','Annoying','Disruptive'] #EXTEND
elements = ['Fire','Water','Ice','Electricity','Plasma','Lava'] #EXTEND
numToRarity = {0: 'Common', 1: 'Uncommon', 2: 'Rare', 3: 'Mythical', 4: 'Legendary'}

#Weapon init stuff... functions, classes for init, finding weapons, describing weapons

def removeFromInv(char,item):
	for i in range(0,len(player1.inventoryNames)):
		if player1.inventoryNames[i] == item:
			delItemIndex = i
	del player1.inventory[delItemIndex]
	del player1.inventoryNames[delItemIndex]

def findWeapon(character):
	print "*You found a new weapon!*"
	newWeapon = initWeapon(character.level, character.classType)
	printWeapon(newWeapon)
	return newWeapon

def printWeapon(weapon):
	print weapon.name
	print "Rarity: " + numToRarity[weapon.rarity]
	print str(weapon.damage) + " " + weapon.element + " damage"
	print floatToPercent(weapon.critChance) + " Critical Hit Chance"

#level is character level for balancing and progression. classType is player's class so the weapon matches the class
def initWeapon(level, classType):
	rarity = random.randint(0,4)
	damage = int(float(level) * (math.ceil(random.random() * 10))) * (rarity + 1)
	weaponType = classWeapons[classType][int(math.floor(random.random()*len(classWeapons[classType])))]
	name = " ".join([prefixes[random.randint(0,len(prefixes)-1)], weaponType])
	element = elements[int(math.floor(random.random()*(len(elements)-1)))]
	crits = random.random()
	newWeapon = Weapon(name, weaponType, rarity, damage, element, crits)
	newWeapon.uses = -1
	player1.inventoryNames.append(name)
	return newWeapon

def initItem(name,damage,selfDamage,uses):
	player1.inventoryNames.append(name)
	return (Item(name,damage,selfDamage,uses))

class Item:
	damage = 0
	selfDamage = 0
	name = ""
	uses = 1
	itemType = "Item"
	critChance = 0.0

	def __init__ (self, name, damage, selfDamage, uses):
		self.name = name
		self.damage = damage
		self.selfDamage = selfDamage
		self.uses = uses

	def checkIfBroke(self):
		if self.uses == 0:
			return True
		else:
			return False

class Weapon(Item):
	rarity = 0
	element = ""
	weaponType = ""
	critChance = 0.0

	def __init__ (self, name, weaponType, rarity, damage, element, critChance):
		self.name = name
		self.weaponType = weaponType
		self.rarity = rarity
		self.damage = damage
		self.element = element
		self.critChance = critChance
		self.itemType = "Weapon"

#Character classes
class Character:
	oldLoc = ""
	maxHealth = 0
	exp = 0
	gold = 0
	health = 0
	level = 1
	classType = ""
	inventory = []
	inventoryNames = []
	loc = "CastleRoomMain"
	activeQs = []
	completedQs = []

	def checkLvUp(self):
		if self.exp >= (10*(2**(self.level-2))):
			self.exp -= (10*(2**(self.level-2)))
			self.level += 1
			print "*You leveled up!*\n*You are now level " + str(self.level) + "!*"
			print "*Your max health has gone up from " + str(self.maxHealth) + " to " + str(int(math.floor(self.maxHealth*1.1)))
			self.maxHealth = int(math.floor(self.maxHealth * 1.1))
			self.checkLvUp()

class Knight(Character):
	
	def __init__(self, health):
		self.health = health
		self.classType = "Knight"
		self.maxHealth = health

class Mage(Character):
	
	def __init__(self, health):
		self.health = health
		self.classType = "Mage"
		self.maxHealth = health

class Archer(Character):
	
	def __init__(self, health):
		self.health = health
		self.classType = "Archer"
		self.maxHealth = health

#PLAY
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nWelcome, adventurer, to the world of Wohndar.\nI am the godly voice inside everyone's head. You may refer to me as The Narrator.\nIn this world, people from many dimensions meet to explore, adventure, and trade.")
inputClass = ""
while not inputClass in allClasses:
	print("What class are you?\nYour options are:")
	for i in allClasses:
		print i
	inputClass = raw_input("Choose a class: ")
	if not inputClass in allClasses:
		print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nThat was not one of the options.")

#INIT CHARACTER
if inputClass == 'Knight':
	player1 = Knight(20)
elif inputClass == 'Mage':
	player1 = Mage(15)
elif inputClass == 'Archer':
	player1 = Archer(15)
#elif inputClass == '':...

print "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nAh, so you are a", inputClass + "!\nThat's perfect, because I found this weapon outside for you.\nIt should suit your needs, for now."
player1.inventory.append(findWeapon(player1))
print '*You can check your character at any time by typing 0.*'
print "Now, go on out to the courtyard. I think there's someone there that wants to talk to you."

#START GAME LOOP
while True:
	#MISC LOCS
	if player1.loc == "Inventory":
		j = "-1"
		possInps = []
		possItems = []
		for i in range(0,len(player1.inventoryNames)+1):
			possInps.append(str(i + 1))
			if i != len(player1.inventoryNames) + 1:
				possItems.append(str(i))
		while not j in possInps:
			print "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nLevel " + str(player1.level) + " " + player1.classType + "\nXP: " + str(player1.exp) + "/" + str(int(10*(2**(player1.level-2)))) + "\nGold: " + str(player1.gold)
			for i in range(0,len(player1.inventoryNames)):
				print str(i + 1) + ". " + player1.inventoryNames[i]
			print str(len(player1.inventoryNames) + 1) + ". LEAVE INVENTORY"
			inp = raw_input("")
			if not inp in possInps:
				print "Not a valid response."
			elif inp in possItems:
				if player1.inventory[int(inp)-1].itemType == "Weapon":
					print player1.inventory[int(inp)-1].name + "\nRarity: " + numToRarity[player1.inventory[int(inp)-1].rarity] + "\nDamage: " + str(player1.inventory[int(inp)-1].damage) + "\nCrit Chance: " + floatToPercent(player1.inventory[int(inp)-1].critChance) + "\nSelf Healing: " + str(-player1.inventory[int(inp)-1].selfDamage)
				else:
					print player1.inventory[int(inp)-1].name + "\nDamage: " + str(player1.inventory[int(inp)-1].damage) + "\nSelf Healing: " + str(-player1.inventory[int(inp)-1].selfDamage)
				response = "-1"
				while not response in ["1","2"]:
					response = raw_input("1. Return to INVENTORY\n2. Drop item\n")
				if response == "2":
					newResponse = "-1"
					while not newResponse in ["1","2"]:
						newResponse = raw_input("Are you sure you want to drop " + str(player1.inventory[int(inp)-1].name) + "? (THIS ACTION CANNOT BE UNDONE)\n1. Yes\n2. No\n")
					if newResponse == "1":
						del player1.inventory[int(inp)-1]
						del player1.inventoryNames[int(inp)-1]
			else:
				player1.loc = player1.oldLoc
			j = inp
	#CASTLE OF WOHNDAR
	elif player1.loc == 'CastleCourtyard':
		if not "FindChild" in player1.completedQs and not "FindChild" in player1.activeQs:
			print locToDialog[player1.loc]
			print 'Dwarf: "Oh, hello, there! Yes, I am in need of some help."\nDwarf: "You see, I\'ve been hired to protect a child while his parents are away."\nDwarf: "Unfortunately, I must have dozed off, because when I woke up, the baby was gone!"\nDwarf: "Could you help me find him? Please?"'
			response = raw_input('1. I\'ll help you.\n2. Maybe later.\n')
			if response == "1":
				player1.activeQs.append("FindChild")
				print 'Dwarf: "Oh, thank you so much! You can go out the gate to get out of the castle."\n*Quests updated*'
			else:
				print 'Dwarf: "I understand, you\'re busy..."'
			move(player1.loc,player1)
		elif "FindChild" not in player1.completedQs:
			print '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nDwarf: "Have you brought the baby?"'
			if not 'Baby' in player1.inventoryNames:
				print 'Dwarf: "Oh, you haven\'t? Okay..."\nDwarf:"..."\nDwarf: "The password? Oh, it\'s \'p@ssw0rd123\'."'
			else:
				print 'Dwarf: "Oh, you found him! Thank you so much!"\n*The dwarf walks away with the baby*\n*QUEST COMPLETE*'
				for i in range(0,len(player1.activeQs)):
					if player1.activeQs[i] == 'FindChild':
						del player1.activeQs[i]
				player1.completedQs.append('FindChild')
				babyIndex = 0
				for i in range(0,len(player1.inventoryNames)):
					if player1.inventoryNames[i] == 'Baby':
						babyIndex = i
				del player1.inventory[babyIndex]
				del player1.inventoryNames[babyIndex]
				player1.exp += 50
				print '*Added 50 XP*'
				player1.checkLvUp()
				print '*The dwarf comes back, a bloodied mess, without the baby.*\n*He stares off into the distance, not acknowledging your existence.*'
				villageHouses.append('*Many hooded figures are sitting in a circle, chanting.*\n*They don\'t notice you; you should probably leave.*')
			move(player1.loc,player1)
		else:
			babyInventoryNames = ['Baby','Baby','Baby','Baby','Baby','Baby','Baby','Baby']
			if player1.inventoryNames == babyInventoryNames:
				print '*The Dwarf has returned*\nDwarf: "Are you ready to face my master?"\n1. Yes\n2. No'
				inp = "-1"
				while not inp in ["1","2"]:
					inp = raw_input("Respond: ")
					if not inp in ["1","2"]:
						print "Invalid input."
				if inp == "1":
					print "*The dwarf nods, taking the babies.*\n*He stabs them one by one.*\n*A demonic rift opens.*\n*You jump in.*"
					player1.loc = "Hell"
					player1.inventory = []
					player1.inventoryNames = []
				else:
					print '*The dwarf walks away.*'
					move(player1.loc,player1)
			else:
				print '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n*The emptiness of the courtyard is haunting.*'
				move(player1.loc,player1)
	elif player1.loc == 'CastleGate':
		print locToDialog[player1.loc]
		passwordInp = raw_input("Guard: \"Halt! What's the password?\"\nPassword: ")
		if passwordInp == "p@ssw0rd123":
			print 'Guard: "Okay, you can go."'
			move(player1.loc, player1)
		else:
			print 'Guard: "Sorry, that\'s wrong. I\'ll escort you back to the CASTLE THRONE ROOM."'
			player1.loc = "CastleRoomMain"
	elif player1.loc == 'CastleGate2':
		print locToDialog[player1.loc]
		passwordInp = raw_input("Guard: \"Halt! What's the password?\"\nPassword: ")
		if passwordInp == "p@ssw0rd123":
			print 'Guard: "Okay, you can go."'
			move(player1.loc, player1)
		else:
			print 'Guard: "Sorry, that\'s wrong. I\'ll escort you back to the VILLAGE."'
			player1.loc = "Village"
	#WOHNDAR VILLAGE
	elif player1.loc == "VillageHouse":
		print "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
		print villageHouses[random.randint(0,len(villageHouses)-1)]
		move(player1.loc, player1)
	elif player1.loc == "Cave1":
		print "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n*Your initial suspicions seemed to be correct*\n*There's not much here...*\n*But wait... what's that?!*"
		battle(player1, Enemy(10, "Slime", 10, 1))
		move(player1.loc, player1)
	elif player1.loc == "VillageHeal" or player1.loc == "Town1Heal":
		print '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n*An old man is hunched over the table*\nDoctor: "Hello! Would you like me to heal you?"\n1. Yes\n2. No'
		response = '7afagda'
		response = raw_input("Respond: ")
		if not response in ["1","2"]:
			print '*Invalid Response. Try again*'
		if response == "1":
			print 'Doctor: "Alright."\n*You have been healed*'
			player1.health = player1.maxHealth
		else:
			print 'Doctor: "Suit yourself."'
		move(player1.loc, player1)
	elif player1.loc == 'BabyBush':
		print len(player1.inventory)
		print "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n*You see a rustling in the bush.*\n*A baby jumps out at you!*\n*Using your enhanced reflexes, you catch it and put it in your inventory.*"
		if len(player1.inventory) < 8:
			print "*Added BABY to inventory*"
			player1.inventory.append(initItem("Baby",-9001,0,-1))
		else:
			print "Inventory full"
		move(player1.loc, player1)
	elif player1.loc == 'Brush1':
		print locToDialog[player1.loc]
		battle(player1,genEn("GREMLIN",5))
		move(player1.loc,player1)
	elif player1.loc == "Town1Shop":
		inp = "afsaf"
		canPerform = False
		print '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nShopkeeper: "Welcome to my shop!"\n1. Random Weapon - 200 Gold\n2. Health Potion - 50 Gold\n3. Leave Shop'
		while not canPerform:
			inp = "afsaf"
			while not inp in ["1","2","3"]:
				inp = raw_input("")
				if not inp in ["1","2","3"]:
					print "Invalid input."
			if inp == "1":
				if player1.gold >= 200:
					player1.inventory.append(findWeapon(player1))
					player1.gold -= 200
					canPerform = True
				else:
					print "You can't afford that!"
			elif inp == "2":
				if player1.gold >= 50:
					player1.inventory.append(initItem("Potion of Lesser Healing", 0, -20, 3))
					player1.gold -= 50
					canPerform = True
				else:
					print "You can't afford that!"
			else:
				player1.loc = 'Town1'
				canPerform = True
	elif player1.loc == "MaplebellAlcove":
		if (not 'MaplebellNymph' in player1.activeQs) and (not 'MaplebellNymph' in player1.completedQs):
			print '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n*A nymph is sitting, facing away from you.*\nNymph: "I\'ve been waiting for you."\n*She turns to look at you.*\nNymph: "My name is Scarlet, and I\'m the protector of this forest."\nScarlet: "I need your help with something."\nScarlet: "You see, Maplebell forest is somewhat of a maze."\nScarlet: "But recently, there have been GREMLINS invading!"\nScarlet: "Find these 3 GREMLINS and bring to me their scalps, and I will reward you."\n*QUESTS UPDATED*'
			player1.activeQs.append('MaplebellNymph')
		elif 'MaplebellNymph' in player1.activeQs:
			if 'MBGremlinScalp1' in player1.inventoryNames and 'MBGremlinScalp2' in player1.inventoryNames and 'MBGremlinScalp3' in player1.inventoryNames:
				print 'Scarlet: "Thank you for clearing the forest of these creatures. You will be rewarded."\n*QUEST COMPLETE*'
				player1.exp += 100
				print '*Added 100 XP*'
				player1.checkLvUp()
				removeFromInv(player1, 'MBGremlinScalp1')
				removeFromInv(player1, 'MBGremlinScalp2')
				removeFromInv(player1, 'MBGremlinScalp3')
				for i in range(0,len(player1.activeQs)):
					if player1.activeQs[i] == 'MaplebellNymph':
						del player1.activeQs[i]
				player1.completedQs.append('MaplebellNymph')
		else:
			print 'Scarlet: "Come back later... Maybe I\'ll have something for you then."'
		move(player1.loc, player1)
	elif player1.loc == 'MB1' or player1.loc == 'MB2' or player1.loc == 'MB3' or player1.loc == 'MB5' or player1.loc == 'MB6' or player1.loc == 'MB7' or player1.loc == 'MB9' or player1.loc == 'MB10' or player1.loc == 'MB11' or player1.loc == 'MB13' or player1.loc == 'MB14' or player1.loc == 'MB15' or player1.loc == 'MB16':
		mbMazeDialogs = ['*You\'re beginning to feel a little lost...*', '*Have I been here before?*','*That tree looks familiar...*','*These places all look the same.*']
		print '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n'
		print mbMazeDialogs[random.randint(0,len(mbMazeDialogs)-1)]
		move(player1.loc,player1)
	elif player1.loc == 'MB4':
		if battle(player1,genEn('GREMLIN',10)):
			if len(player1.inventory) <= 8:
				player1.inventory.append(Item('GREMLIN SCALP',0,0,-1))
				player1.inventoryNames.append('MBGremlinScalp1')
				print '*Added GREMLIN SCALP to Inventory*'
			else:
				print '*Inventory Full!*'
		move(player1.loc,player1)
	elif player1.loc == 'MB8':
		if battle(player1,genEn('GREMLIN',10)):
			if len(player1.inventory) <= 8:
				player1.inventory.append(Item('GREMLIN SCALP',0,0,-1))
				player1.inventoryNames.append('MBGremlinScalp2')
				print '*Added GREMLIN SCALP to Inventory*'
			else:
				print '*Inventory Full!*'
		move(player1.loc,player1)
	elif player1.loc == 'MB12':
		if battle(player1,genEn('GREMLIN',10)):
			if len(player1.inventory) <= 8:
				player1.inventory.append(Item('GREMLIN SCALP',0,0,-1))
				player1.inventoryNames.append('MBGremlinScalp3')
				print '*Added GREMLIN SCALP to Inventory*'
			else:
				print '*Inventory Full!*'
		move(player1.loc,player1)
	#HELL
	elif player1.loc == "Hell":
		print locToDialog[player1.loc]
		move(player1.loc, player1)
	elif player1.loc == "HellGate1":
		print '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n*A Demon is guarding the path.*\nDemon: What are you looking at?'
		battle(player1,genEn("Demon",100))
	else:
		print "You are at: " + locToReadableLoc[player1.loc]
		print locToDialog[player1.loc]
		move(player1.loc, player1)


















