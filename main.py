#This is a text only RPG, made as my final project for my class, Computer Science Principles. Any suggestions are welcome, and should be sent to 27ollyf@seasidek12.org

import random
import shutil
import sys
import textwrap
import time

characterClassChecker = False
nameChecker = True
playerStatChecker = False
playerStatChecker2 = False
playerStatChecker3 = False
playerStatChecker4 = False
playerStatChecker5 = False
playerStatChecker6 = False
playerName = ""
playersClass = ""
playerLevel = 1
playerStrengthScore = 0
playerStrengthModifier = 0
playerDexterityScore = 0
playerDexterityModifier = 0
playerConstitutionScore = 0
playerConstitutionModifier = 0
playerIntelligenceScore = 0
playerIntelligenceModifier = 0
playerWisdomScore = 0
playerWisdomModifier = 0
playerCharismaScore = 0
playerCharismaModifier = 0
playerDamageTaken = 0
playerHealthMax = 0 + playerConstitutionModifier
playerHealth = playerHealthMax - playerDamageTaken
playersInventory = []
playersCurrentWornArmorName = ""
playersCurrentWornArmorDefense = 0
playersCurrentWornArmorCheckPenalty = 0
playersArmorClass = 10 + playersCurrentWornArmorDefense + playerDexterityModifier
damagePlayerAboutToDeal = 0
enemyAC = 0
statChoosingIterator = -1
maximumArmorDexBonus = 0
playerGold = 0
playersCurrentWornShieldDefense = 0
playersCurrentWornShieldCheckPenalty = 0
fastMovement = False
inRage = False
equippedWeapon = ""
sorcererSpellChooser = False
playerChoosenSpells = []
playerSpellSlots = 0
druidSpellChooser = False
gameLoop = 0
choiceChoosen = ""
rolledNumber = 0
playerGender = ""

def rollDiceD6():
  return random.randint(1, 6)
def rollDiceD4():
  return random.randint(1, 4)
def rollDiceD8():
  return random.randint(1, 8)
def rollDiceD10():
  return random.randint(1, 10)
def rollDiceD12():
  return random.randint(1, 12)
def rollDiceD20():
  return random.randint(1, 20)
def rollDiceD100():
  return random.randint(1, 100)
def characterInfo():
  print(playerName, " - Player Name")
  print(playerIntelligenceScore, " - Intelligence Score")
  print(playerIntelligenceModifier, " - Intelligence Modifier")
  print(playerWisdomScore, " - Wisdom Score")
  print(playerWisdomModifier, " - Wisdom Modfier")
  print(playerStrengthScore, " - Strength Score")
  print(playerStrengthModifier, " - Strength Modifier")
  print(playerDexterityScore, " - Dexterity Score")
  print(playerDexterityModifier, " - Dexterity Modifier")
  print(playerConstitutionScore, " - Constitution Score")
  print(playerConstitutionModifier, " - Constitution Modifier" )
  print(playerCharismaScore, " - Charisma Score")
  print(playerCharismaModifier, " - Charisma Modifier")
  print(playerHealthMax, " - Maximum Health")
  print(playerHealth, " - Current Health")
  print(playersInventory, " - Current Inventory")
  print(playersArmorClass, " - Armor Class")



def printMessage():
  global message
  print(textwrap.fill(message, width=shutil.get_terminal_size().columns))

def calculate_modifier(score):
    if score in [18, 19]:
        return 4
    elif score in [17, 16]:
        return 3
    elif score in [15, 14]:
        return 2
    elif score in [13, 12]:
        return 1
    elif score in [11, 10]:
        return 0
    elif score in [9, 8]:
        return -1
    elif score in [7, 6]:
        return -2
    elif score in [5, 4]:
        return -3
    elif score in [3, 2]:
        return -4
    elif score == 1:
        return -5

def delayPrint(t):
  #Im not exactly sure why this is working. It sets the variable message as itself with added formatting to not cut off words. 
  global message
  message = textwrap.fill(message, width=shutil.get_terminal_size().columns)
  #Then for each Character (c) in the newly set message, it runs the loop below.
  for c in message:
    #It writes the character
    sys.stdout.write(c)
    sys.stdout.flush()
    #Then waits for the time put.
    time.sleep(t)




message = ("Welcome adventurer! Before we begin, may I get your name?" )
delayPrint(0.04)
#Once finished choosing name, switch to False
while nameChecker is True:

  #\n creates a new line
  playerName = input( "\nMy name is... ")

  if playerName == "":
    print("Please enter a name.")
  elif len(playerName) < 3:
    print("Name must be at least 3 letters long.")
  elif len(playerName) > 16:
    print("Name is to long; please try again.")
  else:
    print("Welcome, " + playerName + "! Let's pick your stats, shall we?")
    nameChecker = False
    playerStatChecker = True

#Attribute[0Strength, 1Dexterity, 2Constitution, 3Intelligence, 4Wisdom, 5Charisma]]


statTotals = []
#Run this loop 6 times for the six seperate times
for _ in range(6):
  stats = []
  #For each run of the loop, roll 4 D6s
  for _ in range(4):
    stats.append(rollDiceD6())

  #Figure out the lowest number rolled, before removing it from the list "stats"
  min_number = min(stats)
  stats.remove(min_number)

  #adds the total of the 4 dice rolls, after removing the lowest rolled number, to stat totals. This happens six times for each of the six stats.
  total = sum(stats)
  statTotals.append(total)
print(statTotals)

message = ("\n\nThe numbers above are your stats, which determine how good your character is at doing a specific task. You have six stats in total: Strength, your muscles, Dexterity, your intricacy and movement, Constitution, your health and immune system, Intelligence, your ability to think rationally, Wisdom, your knowledge of common sense and decision making, as well as your way to use spells if your a Druid, and finally Charisma, your way of talking to others. Now that you know all this, let's choose your stats.\n\n")

#Checks the size of the console window, and makes sure lines arent cut off.
printMessage()

stats_mapping = {
  "Strength": 0,
  "Dexterity": 0,
  "Constitution": 0,
  "Intelligence": 0,
  "Wisdom": 0,
  "Charisma": 0
}

for stat_name in stats_mapping:
  while True:
    try:
      #Asks the player to input a stat in statTotals
      playerStatInput = int(input(f"{stat_name}: "))
      if playerStatInput in statTotals:
        stats_mapping[stat_name] = playerStatInput
        statTotals.remove(playerStatInput)
        print(statTotals)
        #Increase statChoosingIterator by 1 for each time the loop runs. This lets us differentiate which stat we are updating. The variable initially starts at -1.
        statChoosingIterator = statChoosingIterator + 1
        if statChoosingIterator == 0:
          playerStrengthScore = playerStatInput
        elif statChoosingIterator == 1:
          playerDexterityScore = playerStatInput
        elif statChoosingIterator == 2:
          playerConstitutionScore = playerStatInput
        elif statChoosingIterator == 3:
          playerIntelligenceScore = playerStatInput
        elif statChoosingIterator == 4:
          playerWisdomScore = playerStatInput
        elif statChoosingIterator == 5:
          playerCharismaScore = playerStatInput
        break
      else:
        print("That stat does not match any listed. Please try again.")
    except ValueError:
      print("Invalid input. Please enter an whole number.")


playerStrengthModifier = calculate_modifier(playerStrengthScore)
playerDexterityModifier = calculate_modifier(playerDexterityScore)
playerConstitutionModifier = calculate_modifier(playerConstitutionScore)
playerIntelligenceModifier = calculate_modifier(playerIntelligenceScore)
playerWisdomModifier = calculate_modifier(playerWisdomScore)
playerCharismaModifier = calculate_modifier(playerCharismaScore)

characterClassChecker = True

#Once finished with choosing a character class, switch to False
while characterClassChecker is True:
  message = ("Now that you have picked your stats, lets pick your class. If you are confused as to what any of the classes do, type the classes name, followed by 'help'")

  #Checks the size of the console window, and makes sure lines arent cut off.
  printMessage()
  print("1. Barbarian")
  print("2. Sorcerer")
  print("3. Rogue")
  print("4. Paladin")
  print("5. Druid")
  playersClass = input("\nMy class is: ")
  if playersClass == "":
    print("Please select your class.")
  elif playersClass == "1" or playersClass == "Barbarian" or playersClass == "barbarian" or playersClass == "1.":
    print("You have chosen the Barbarian class.")
    playersClass = "Barbarian"
    playerHitDie = "D12"
    if playerConstitutionModifier is not None:
      playerHealthMax = 12 + playerConstitutionModifier
    characterClassChecker = False
  elif playersClass == "2" or playersClass == "Sorcerer" or playersClass == "sorcerer" or playersClass == "2.":
    print("You have chosen the Sorcerer class.")
    playersClass = "Sorcerer"
    playerHitDie = "D4"
    if playerConstitutionModifier is not None:
      playerHealthMax = 4 + playerConstitutionModifier
    characterClassChecker = False
  elif playersClass == "3" or playersClass == "Rogue" or playersClass == "rogue" or playersClass == "3.":
    print("You have chosen the Rogue class.")
    playersClass = "Rogue"
    playerHitDie = "D6"
    if playerConstitutionModifier is not None:
      playerHealthMax = 6 + playerConstitutionModifier
    characterClassChecker = False
  elif playersClass == "4" or playersClass == "Paladin" or playersClass == "paladin" or playersClass == "4.":
    print("You have chosen the Paladin class.")
    playersClass = "Paladin"
    playerHitDie = "D10"
    if playerConstitutionModifier is not None:
      playerHealthMax = 10 + playerConstitutionModifier
    characterClassChecker = False
  elif playersClass == "5" or playersClass == "Druid" or playersClass == "druid" or playersClass == "5.":
    print("You have chosen the Druid class.")
    playersClass = "Druid"
    playerHitDie = "D8"
    if playerConstitutionModifier is not None:
      playerHealthMax = 8 + playerConstitutionModifier
    characterClassChecker = False

  elif playersClass == "Barbarian help" or playersClass == "barbarian help" or playersClass == "1. help" or playersClass == "1 help":
    message = ("Barbarians are warriors, who use there brute strength and health to fight off enemies. Barbarians have the ability to 'rage', letting them deal more damage, but in return take more. Barbarians usually have a high strength score, followed by constitution ")
    printMessage()

  elif playersClass == "Sorcerer help" or playersClass == "sorcerer help" or playersClass == "2. help" or playersClass == "2 help":
    message = ("Sorcerers are spelllcasters who rely on their innately magical bloodline to cast spells. Sorcerers are generally weak, usually serving as long range defense or utility. They add their charisma modifier to their spell's rolls. ")
    printMessage()

  elif playersClass == "Rogue help" or playersClass == "rogue help" or playersClass == "3. help" or playersClass == "3 help":
    message = ("Rogues are tricksters, usually thieves or criminals. They excel in the art of sneaking or stealing. Their best stat is usually Dexterity, followed by Constitution.")
    printMessage()

  elif playersClass == "Paladin help" or playersClass == "paladin help" or playersClass == "4. help" or playersClass == "4 help":
    message = ("Paladins are holy warriors, who fight to protect a code of honor. Paladins act in service of a deity, helping their god rid the world of evil. Their highest ability score is usually Strength, followed by Constitution.")
    printMessage()

  elif playersClass == "Druid help" or playersClass == "druid help" or playersClass == "5. help" or playersClass == "5 help":
    message = ("Druids are protectors of the earth and nature. They are able to cast spells, usually related to the ground, the earth, or other animals, and use their Wisdom Modifier to add onto their attacks. Their highest stat is usually Wisdom, followed by Constitution.")
    printMessage()
  else:
    print("Invalid Syntax. Please try again.")


print("Now that you have chosen your class, I'll give you your starting equipment.")

if playersClass == "Barbarian":
  time.sleep(2)
  playersInventory.append("Studded Leather Armor")
  playersInventory.append("Greataxe")
  playersInventory.append("Torches x10")
  playersInventory.append("Rations x3")

  startingGold = 0
  startingGoldBeforeMultiplication = []
  #Run this loop 4 times
  for _ in range(4):
    startingGoldBeforeMultiplication.append(rollDiceD4())

  total = sum(startingGoldBeforeMultiplication * 10)
  startingGold = startingGold + total
  playerGold = playerGold + startingGold
  print(playerGold, "Gold")
  time.sleep(0.5)
  print("4 Items added to your inventory.")
  #Sets players armor stats
  if "Studded Leather Armor" in playersInventory:
    playersCurrentWornArmorName = "Studded Leather Armor"
    playersCurrentWornArmorDefense = 3
    playersCurrentWornArmorCheckPenalty = -1
    maximumArmorDexBonus = 5

  #Sets players Armor Class
  if playerDexterityModifier is not None and maximumArmorDexBonus is not None:
    if playerDexterityModifier <= maximumArmorDexBonus:
      playersArmorClass = 10 + playersCurrentWornArmorDefense +   playerDexterityModifier + playersCurrentWornShieldDefense
  else:
    playersArmorClass = 10 + playersCurrentWornArmorDefense + maximumArmorDexBonus + playersCurrentWornShieldDefense

  playerHealth = playerHealthMax - playerDamageTaken


if playersClass == "Sorcerer":
  time.sleep(1)
  playersInventory.append("Leather Armor")
  playersInventory.append("Shortsword")
  playersInventory.append("Torches x10")
  playersInventory.append("Rations x3")
  playersInventory.append("Potion of Healing x3")

  startingGold = 0
  startingGoldBeforeMultiplication = []
  #Run this loop 3 times
  for _ in range(3):
    startingGoldBeforeMultiplication.append(rollDiceD4())

  #adds together all the rolled dice, and times that total by 10
  total = sum(startingGoldBeforeMultiplication * 10)
  startingGold = startingGold + total
  playerGold = playerGold + startingGold
  time.sleep(1)
  print(playerGold, "Gold")
  time.sleep(0.5)
  print("7 items were added to your inventory.")
  time.sleep(0.5)

  if "Leather Armor" in playersInventory:
    playersCurrentWornArmorName = "Leather Armor"
    playersCurrentWornArmorDefense = 2
    playersCurrentWornArmorCheckPenalty = 0
    maximumArmorDexBonus = 6
  if playerDexterityModifier is not None and maximumArmorDexBonus is not None:
    if playerDexterityModifier <= maximumArmorDexBonus:
      playersArmorClass = 10 + playersCurrentWornArmorDefense +   playerDexterityModifier + playersCurrentWornShieldDefense
  else:
    playersArmorClass = 10 + playersCurrentWornArmorDefense + maximumArmorDexBonus + playersCurrentWornShieldDefense

  playerHealth = playerHealthMax - playerDamageTaken



if playersClass == "Rogue":
  time.sleep(2)
  playersInventory.append("Leather Armor")
  playersInventory.append("Shortsword")
  playersInventory.append("Torches x10")
  playersInventory.append("Rations x3")
  playersInventory.append("Thieve's Kit")
  playersInventory.append("Trap Disarm Toolkit")


  startingGold = 0
  startingGoldBeforeMultiplication = []
    #Run this loop 5 times
  for _ in range(5):
    startingGoldBeforeMultiplication.append(rollDiceD4())

  total = sum(startingGoldBeforeMultiplication * 10)
  startingGold = startingGold + total
  playerGold = playerGold + startingGold
  print(playerGold, "Gold")
  time.sleep(0.5)
  print("6 Items were added to your inventory.")

  if "Leather Armor" in playersInventory:
    playersCurrentWornArmorName = "Leather Armor"
    playersCurrentWornArmorDefense = 2
    playersCurrentWornArmorCheckPenalty = 0
    maximumArmorDexBonus = 6

  if playerDexterityModifier is not None and maximumArmorDexBonus is not None:
    if playerDexterityModifier <= maximumArmorDexBonus:
      playersArmorClass = 10 + playersCurrentWornArmorDefense +   playerDexterityModifier + playersCurrentWornShieldDefense
  else:
    playersArmorClass = 10 + playersCurrentWornArmorDefense + maximumArmorDexBonus + playersCurrentWornShieldDefense

  playerHealth = playerHealthMax - playerDamageTaken

if playersClass == "Paladin":
  time.sleep(2)
  playersInventory.append("Scale Mail")
  playersInventory.append("Heavy Wooden Shield")
  playersInventory.append("Torches x10")
  playersInventory.append("Rations x3")
  playersInventory.append("Longsword")
  startingGold = 0
  startingGoldBeforeMultiplication = []
    #Run this loop 6 times
  for _ in range(6):
    startingGoldBeforeMultiplication.append(rollDiceD4())

  total = sum(startingGoldBeforeMultiplication * 10)
  startingGold = startingGold + total
  playerGold = playerGold + startingGold
  print(playerGold, "Gold")
  time.sleep(0.5)
  print("5 Items were added to your inventory.")

  if "Scale Mail" in playersInventory:
    playersCurrentWornArmorName = "Scale Mail"
    playersCurrentWornArmorDefense = 4
    playersCurrentWornArmorCheckPenalty = -4
    maximumArmorDexBonus = 3

  if "Heavy Wooden Shield" in playersInventory:
    playersCurrentWornShieldDefense = 2
    playersCurrentWornShieldCheckPenalty = -2

  if playerDexterityModifier is not None and maximumArmorDexBonus is not None:
    if playerDexterityModifier <= maximumArmorDexBonus:
      playersArmorClass = 10 + playersCurrentWornArmorDefense +   playerDexterityModifier + playersCurrentWornShieldDefense
  else:
    playersArmorClass = 10 + playersCurrentWornArmorDefense + maximumArmorDexBonus + playersCurrentWornShieldDefense

  playerHealth = playerHealthMax - playerDamageTaken



if playersClass == "Druid":
  playersInventory.append("Studded Leather Armor")
  playersInventory.append("Scimitar")
  playersInventory.append("Light Wooden Shield")
  playersInventory.append("Torches x10")
  playersInventory.append("Rations x3")
  startingGold = 0
  startingGoldBeforeMultiplication = []
    #Run this loop 2 times
  for _ in range(2):
    startingGoldBeforeMultiplication.append(rollDiceD4())

  total = sum(startingGoldBeforeMultiplication * 10)
  startingGold = startingGold + total
  playerGold = playerGold + startingGold
  time.sleep(0.5)
  print(playerGold, "Gold")
  time.sleep(0.5)
  print("5 Items were added to your inventory.")

  if "Studded Leather Armor" in playersInventory:
    playersCurrentWornArmorName = "Studded Leather Armor"
    playersCurrentWornArmorDefense = 3
    playersCurrentWornArmorCheckPenalty = -1
    maximumArmorDexBonus = 5

  if "Light Wooden Shield" in playersInventory:
    playersCurrentWornShieldDefense = 1
    playersCurrentWornShieldCheckPenalty = -1
  if playerDexterityModifier is not None and maximumArmorDexBonus is not None:
    if playerDexterityModifier <= maximumArmorDexBonus:
      playersArmorClass = 10 + playersCurrentWornArmorDefense + playerDexterityModifier + playersCurrentWornShieldDefense
  else:
    playersArmorClass = 10 + playersCurrentWornArmorDefense + maximumArmorDexBonus + playersCurrentWornShieldDefense

  if "Scimitar" in playersInventory:
    equippedWeapon = "Scimitar"
  playerHealth = playerHealthMax - playerDamageTaken


def swingGreataxe():
  global playerStrengthModifier
  global enemyAC
  if playerStrengthModifier is None:
    playerStrengthModifier = 0

  rolledAttack = rollDiceD20() + playerStrengthModifier

  if rolledAttack == 20:
    damage = rollDiceD6() * 2 + playerStrengthModifier
    return damage
  if rolledAttack >= enemyAC:
      damage = rollDiceD6() + playerStrengthModifier
      return damage

def swingShortsword():
  global playerStrengthModifier
  global playerDexterityModifier
  global enemyAC
  if playerStrengthModifier is None:
    playerStrengthModifier = 0

  if playerDexterityModifier is None:
    playerDexterityModifier = 0

  rolledAttack = rollDiceD20() + playerStrengthModifier

  #If it rolls a 20 it serves as a critical hit, and the dice roll landed is doubled
  if rolledAttack == 20:
    if playerStrengthModifier > playerDexterityModifier:
      damage = rollDiceD6() * 2 + playerStrengthModifier
      return damage

    if playerStrengthModifier <= playerDexterityModifier:
      damage = rollDiceD6() * 2 + playerDexterityModifier
      return damage

  if rolledAttack >= enemyAC:
    if playerStrengthModifier > playerDexterityModifier:
      damage = rollDiceD6() + playerStrengthModifier
      return damage

    if playerStrengthModifier <= playerDexterityModifier:
      damage = rollDiceD6() + playerDexterityModifier
      return damage

def swingScimitar():
  global playerStrengthModifier
  global playerDexterityModifier
  global enemyAC
  if playerStrengthModifier is None:
    playerStrengthModifier = 0

  if playerDexterityModifier is None:
    playerDexterityModifier = 0

  rolledAttack = rollDiceD20() + playerStrengthModifier

  #If it rolls a 20 it serves as a critical hit, and the dice roll landed is doubled
  if rolledAttack == 20:
    if playerStrengthModifier > playerDexterityModifier:
      damage = rollDiceD6() * 2 + playerStrengthModifier
      return damage

    if playerStrengthModifier <= playerDexterityModifier:
      damage = rollDiceD6() * 2 + playerDexterityModifier
      return damage

  if rolledAttack >= enemyAC:
    if playerStrengthModifier > playerDexterityModifier:
      damage = rollDiceD6() + playerStrengthModifier
      return damage

    if playerStrengthModifier <= playerDexterityModifier:
      damage = rollDiceD6() + playerDexterityModifier
      return damage


#Sorcerers have 5 level 0 spells (Cantrips) and 3 level 1 spells when their character is at level 1. They also get a familar.

#Druids have 3 level 0 spells and 1 level 1 spell when their character is at levvel 1. They also get an animal companion, nature sense, and wild empathy.

if playersClass == "Sorcerer":
  sorcererSpellChooser = True
  if sorcererSpellChooser is True:
    message = ("Because you have choosen the sorcerer class you can now pick your spells. Unlike other classes who use their weapons, your class primarily uses spells to excel in combat. However, your spells are limited. You can use your spells that are 'level 0', also known as Cantrips as many times as you want per day. However, you can only use your level 1 spells three times per day at your current level. With that now said, lets choose your spells.")
    printMessage()
    print("\n")
    message = ("Heres your choice of level 0 spells:")
    printMessage()

    message = ("Detect Poison: Detects poison in one creature or object")
    printMessage()
    message = ("Detect Magic: Detects spells and magic items within 60 ft.")
    printMessage()
    message = ("Read Magic: Read scrolls and spellbooks.")
    printMessage()
    message = ("Tasha's Hideous Laughter: Subject loses actions for 1 roound/level")
    printMessage()
    message = ("Light: Creates torches or other lights")
    printMessage()
    message = ("Ray of Frost: Ray deals 1d6 cold damage")
    printMessage()
    print("\n")
    message = ("Type in a spell's name to choose it. (Capitalization and spelling matters) You have 5 choices in total")
    printMessage()
    choosingLevelZeroSpells = True
    amountOfChoosenLevelZeroSpells = 0
    while choosingLevelZeroSpells is True:
      if amountOfChoosenLevelZeroSpells == 5:
        choosingLevelZeroSpells = False
        break
      choosenSpell = input("")
      #Needs to check and not let the player choose the same spell multiple times.
      if choosenSpell == "Detect Poison" or choosenSpell == "Detect Magic" or choosenSpell == "Read Magic" or choosenSpell == "Tasha's Hideous Laughter" or choosenSpell == "Light" or choosenSpell == "Ray of Frost":
        if choosenSpell in playerChoosenSpells:
          print("Spell already chosen")
        else:
          playerChoosenSpells.append(choosenSpell)
          print(choosenSpell + " chosen.")
          amountOfChoosenLevelZeroSpells = amountOfChoosenLevelZeroSpells + 1
      else: 
        print("Not a valid spell.")
    message = ("Now lets choose your level 1 spells. Remember, you only have 3 choices, so choose wisely.")
    printMessage()

    message = ("True Strike: +20 on your next attack roll.")
    printMessage()
    message = ("Magic Weapon: Weapon gets +1 bonus")
    printMessage()
    message = ("Shield: Inivisible disc gives +4 to AC, as well as blocking the spell 'magic missles'")
    printMessage()
    message = ("Magic Missle: 2d4+2 damage; +1 missle per two levels above 1st, max of 5.")
    printMessage()
    message = ("Shocking Grasp: Touch delivers 1d6/level electricity damage. Deals 2d6+1 to enemies wearing metal armor.")
    printMessage()
    message = ("Detect Thoughts: Allows 'listening' to surface thoughts")
    printMessage()

  message = ("Type in a spell's name to choose it. (Capitalization and spelling matters) You have 3 choices in total")
  printMessage()
  choosingLevelZeroSpells = True
  amountOfChoosenLevelZeroSpells = 0
  while choosingLevelZeroSpells is True:
    if amountOfChoosenLevelZeroSpells == 3:
      choosingLevelZeroSpells = False
      break
    choosenSpell = input("")
    if choosenSpell == "True Strike" or choosenSpell == "Magic Weapon" or choosenSpell == "Shield" or choosenSpell == "Magic Missle" or choosenSpell == "Shocking Grasp" or choosenSpell == "Detect Thoughts":
      if choosenSpell in playerChoosenSpells:
        print("Spell already chosen")
      else:
        playerChoosenSpells.append(choosenSpell)
        amountOfChoosenLevelZeroSpells = amountOfChoosenLevelZeroSpells + 1
    else: 
      print("Not a valid spell.")




if playersClass == "Druid":
  druidSpellChooser = True
  while druidSpellChooser is True:
    message = ("Because you have chosen the Druid class, you are able to cast spells. Druids have a concept called 'spellslots', which determine how many spells they can use a day. Right now, since your level 1 you can choose 3 level 0 spells, also called 'cantrips', and 1 level 1 spell. Level 0 spells you can use always, but you can only use your level 1 spell once per day. With that all said, lets choose your spells.")
    printMessage()
    message = ("Detect Magic:  Detects spells and magic items within 60 ft. ")
    printMessage()
    message = ("Guidance: +1 on one attack roll or skill check.")
    printMessage()
    message = ("Cure Minor Wounds: Cures 1 point of damage.")
    printMessage()
    message = ("Virtue: Subject gains 1 temporary HP.")
    printMessage()
    message = ("Detect Poison: Detects poison in one creature or object.")
    printMessage()
    message = ("Flare: Dazzles one creature (-1 penalty on attack rolls or skill checks, lasting for 2 rounds.)")
    printMessage()
    print("\n")
    message = ("Type in a spell's name to choose it. (Capitalization and spelling matters) You have 3 choices in total")
    printMessage()
    choosingLevelZeroSpells = True
    amountOfChoosenLevelZeroSpells = 0
    while choosingLevelZeroSpells is True:
      if amountOfChoosenLevelZeroSpells == 3:
        choosingLevelZeroSpells = False
        break
      choosenSpell = input("")
      #Needs to check and not let the player choose the same spell multiple times.
      if choosenSpell == "Detect Poison" or choosenSpell == "Detect Magic" or choosenSpell == "Flare" or choosenSpell == "Cure Minor Wounds" or choosenSpell == "Virtue" or choosenSpell == "Guidance":
        if choosenSpell in playerChoosenSpells:
          print("Spell already chosen")
        else:
          playerChoosenSpells.append(choosenSpell)
          print(choosenSpell + " chosen.")
          amountOfChoosenLevelZeroSpells = amountOfChoosenLevelZeroSpells + 1
      else: 
        print("Not a valid spell.")

    message = ("Now lets choose your level 1 spells. Remember, you only have 1 choice, so choose wisely.")
    printMessage()
    message = ("")
    printMessage()
    message = ("Calm Animals: Calms (2d4 + level) HD of animals")
    printMessage()
    message = ("Charm Animal: Makes one animal your friend")
    printMessage()
    message = ("Cure Light Wounds: Heals 1d8 + level")
    printMessage()
    message = ("Entangle: Plants entangle everyone in a 40-ft. radius")
    printMessage()
    message = ("Faerie Fire: Outlines subjects with light, canceling blur, concealment, invisibility, and the like.")
    printMessage()
    message = ("Goodberry: 2d4 berrries, each curing 1 hp. (max 8hp/24")
    printMessage()
    message = ("Magic Fang: One natural weapon of subject creature gets +1 on attack and damage rolls.")
    printMessage()
    message = ("Magic Stone: Three stones gain +1 on attack rolls, dealing 1d6+1 damage each.")
    printMessage()
    message = ("Obscuring Mist: Fog surronds you.")
    printMessage()
    message = ("Produce Flame: 1d6+1/level damage, touch or thrown")
    printMessage()
    message = ("Speak with Animals: You can communicate with animals.")
    printMessage()

    message = ("Type in a spell's name to choose it. (Capitalization and spelling matters) You have 1 choice in total")
    printMessage()
    choosingLevelZeroSpells = True
    amountOfChoosenLevelZeroSpells = 0
    while choosingLevelZeroSpells is True:
      if amountOfChoosenLevelZeroSpells == 1:
        choosingLevelZeroSpells = False
        druidSpellChooser = False
        break
      choosenSpell = input("")
      if choosenSpell == "Calm Animals" or choosenSpell == "Charm Animal" or choosenSpell == "Cure Light Wounds" or choosenSpell == "Entangle" or choosenSpell == "Faerie Fire" or choosenSpell == "Goodberry" or choosenSpell == "Magic Fang" or choosenSpell == "Magic Stone" or choosenSpell == "Obscuring Mist" or choosenSpell == "Produce Flame" or choosenSpell == "Speak with Animals":
        if choosenSpell in playerChoosenSpells:
          print("Spell already chosen")
        else:
          playerChoosenSpells.append(choosenSpell)
          amountOfChoosenLevelZeroSpells = amountOfChoosenLevelZeroSpells + 1
      else: 
        print("Not a valid spell.")

message = ("Now that you have made your vessel, its time for your journey to begin. A journey of heartbreak, sadness, of...")
delayPrint(0.1)
time.sleep(2)
print("\n" + "Mom: " + playerName + "!")
message = ("Its time to wake up. Wouldnt want you missing academy!")
delayPrint(0.04)
time.sleep(1)
print("\n")
message = ("You look around the room you find yourself in. Gentle sunlight streams through the curtained window as you hear kids yelling in the urban street below.")
delayPrint(0.04)
print("\n")
message = ("Your not sure where this vessel has taken you. What would you like to do?")
delayPrint(0.04)
print("\n")
message = ("A: Call back to your 'mom'.")
delayPrint(0.04)
print("\n")
message = ("B: Look around this foreign room (Wisdom, Perception). ")
delayPrint(0.04)
print("\n")
message = ("C: Start walking down stairs.")
delayPrint(0.04)
gameLoop = gameLoop + 1
while gameLoop == 1:
  choiceChoosen = str(input("\n"))
  if choiceChoosen == "A" or choiceChoosen == "a":
    time.sleep(0.3)
    message = ("Ill be there in a second mom!")
    delayPrint(0.04)
    gameLoop = gameLoop + 1
    break
  elif choiceChoosen == "B" or choiceChoosen == "b":
    time.sleep(0.3)
    if playerWisdomModifier is None:
      playerWisdomModifier = 0
    rolledNumber = rollDiceD20() + playerWisdomModifier
    if rolledNumber >= 8:
      message = ("You wipe the sleep off your eyes and look around this new space. The room is decorated nicely, with a queen bed tucked in the corner. Theres a desk with a computer on top of it, which says 'Explorers.net' in the url.")
      delayPrint(0.04)
      time.sleep(1)
      print("\n")
      message = ("You see a small lockbox tucked away neatly on your bed's nightstand. After opening it you see an ornamented pendant inside, with a ruby as its centerpiece. You pick up the necklace and wear it around your neck. ")
      delayPrint(0.04)
      time.sleep(1)
      playersInventory.append("Regenerative Pendant")
      gameLoop = gameLoop + 2

    elif rolledNumber < 8:
      message = ("You wipe the sleep off your eyes and look around this new space. The room is decorated nicely, with a queen bed tucked in the corner. Theres a desk with a computer on top of it, which says 'Explorers.net' in the url.")
      delayPrint(0.04)
      time.sleep(1)
      print("\n")
      gameLoop = gameLoop + 2
    else:
      print("Error, Line 788")
  elif choiceChoosen == "C" or choiceChoosen == "c":
    message = ("After getting up from bed and wiping your eyes, you open the wooden dresser next to your bed and put on a new set of clothes, starting to walk down the stairs.")
    delayPrint(0.04)
    gameLoop = gameLoop + 2
  else:
    print("Not a valid choice. Please pick 'A', 'B' or 'C'.")



while gameLoop == 2:
  print("\n")
  message = ("Now what would you like to do?")
  delayPrint(0.04)
  
  
  message = ("A: Look around this foreign room (Wisdom, Perception). ")
  delayPrint(0.04)
  print("\n")
  message = ("B: Start walking down stairs.")
  delayPrint(0.04)
  while gameLoop == 2:
    choiceChoosen = str(input("\n"))
    if choiceChoosen == "A" or choiceChoosen == "a":
      time.sleep(0.3)
      if playerWisdomModifier is None:
        playerWisdomModifier = 0
      rolledNumber = rollDiceD20() + playerWisdomModifier
      if rolledNumber >= 8:
        message = ("You wipe the sleep off your eyes and look around this new space. The room is decorated nicely, with a queen bed tucked in the corner. Theres a desk with a computer on top of it, which says 'Explorers.net' in the url.")
        delayPrint(0.04)
        time.sleep(1)
        print("\n")
        message = ("You see a small lockbox tucked away neatly on your bed's nightstand. After opening it you see an ornamented pendant inside, with a ruby as its centerpiece. You pick up the pendant and wear it around your neck. ")
        delayPrint(0.04)
        playersInventory.append("Regenerative Pendant")
        gameLoop = gameLoop + 1

      elif rolledNumber < 8:
        message = ("You wipe the sleep off your eyes and look around this new space. The room is decorated nicely, with a queen bed tucked in the corner. Theres a desk with a computer on top of it, which says 'Explorers.net' in the url.")
        delayPrint(0.04)
        time.sleep(1)
        print("\n")
      else:
        print("Error, Line 836")
    elif choiceChoosen == "B" or choiceChoosen == "b":
      message = ("After getting up from bed and wiping your eyes, you start walking down the stairs.")
      delayPrint(0.04)
      gameLoop = gameLoop + 1
    else:
      print("Not a valid choice. Please pick 'A' or 'B'.")


while gameLoop == 3:
  print("\n")
  message = ("You decide to start walking down the stairs, the fluorescent lights giving off a soft buzz above your head.")
  delayPrint(0.04)
  if "Regenerative Pendant" in playersInventory:
    message = ("'Good mor-' your mom glances over at you before returning to her cooking. 'I see your wearing your father's pendant. Its been a while since you pulled it out.' She says nothing more and continues  'See you at six.'")
    delayPrint(0.04)
    break
  else: 
    message = ("Good morning " + playerName + "." + " You better get going quickly— you might be late at this rate.")
    delayPrint(0.04)
    


