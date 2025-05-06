from operator import concat
import random as rand
import time
from turtle import delay
import os
import copy
import msvcrt

# --- Entity klasserna (Fiende, Allierade, Spelare) ---
class Entity:
    def __init__(self,name,description,image, max_hp,damage,speed):
        self.name = name
        self.description = description
        self.image = image
        self.max_hp = max_hp
        self.hp = max_hp
        self.damage = damage
        self.speed = speed
        self.dead = False

    def __repr__(self):
        return self.name

    def is_alive(self):
        return not self.dead
    '''
    Returns whether that target was killed.
    '''

    def print_self(self):
        print(f"{self.name}:")
        print(self.description)
        print(self.image)
        print(f"Hp: {self.hp}/{self.max_hp}")
        print(f"Damge: {self.damage}")


    def attack(self, target) -> bool:
        '''
        Attacks the target of type entity.
        Returns whether that target was killed.
        '''
        target.hp -= self.damage
        if target.hp <= 0:
            target.hp = 0
            target.dead = True
        print(f"{self.name} attacked {target.name}, dealing {self.damage} damage!")
        print(f"{target.name}'s HP is now {target.hp}/{target.max_hp}")
        
        return target.dead


class Enemy(Entity):
    def __init__ (self, name, description, image, max_hp, damage, speed):
        super().__init__(name, description, image, max_hp, damage, speed)


    def Find_target(self):
        target = ally_list[rand.randint(0,len(ally_list)-1)]
        killed = self.attack(target)
        if killed:
            ally_list.remove(target)


class Ally(Entity):
    def __init__(self, name, description, image, max_hp, damage, speed, level):
        super().__init__(name, description, image, max_hp, damage, speed)
        self.level = level
    
    def Find_target(self):
        print(f"what do you want to do using {self}\n")
        self.print_self()
        print("\nWhat will you do?")
        print("1. Attack")
        print("2. Use Item")
        print("3. Check Stats")
        action = input("Choose an action (1, 2 or 3): ")

        if action == "1":
            print("what enemy do you want to attack\n")
            i = 1
            for enemy in enemy_list:
            
                print(f"{i}: {enemy.name}: {enemy.hp}/{enemy.max_hp}")
                i+= 1
            index = int(input()) - 1
            target = enemy_list[index]

            killed = self.attack(target)
            if killed:
                enemy_list.remove(target)
        elif action == "2":
            used = self.use_items()


            if not used:
                print("\nWhat will you do?")
            print("1. Attack")
            print("2. Check Stats")
            action = input("Choose an action (1 or 2): ")

            if action == "1":
                print("What enemy do you want to attack? \n")
                i = 1
                for enemy in enemy_list:
                    print(f"{i}: {enemy.name}: {enemy.hp}/{enemy.max_hp}")
                    i+=1
                index = int(input()) - 1
                target = enemy_list[index]

                killed = self.attack(target)
                if killed:
                    enemy_list.remove(target)
        elif action == "3":
            self.player_stats
        else:
            print("Invalid action. You hesitate...")
            return


class Npc(Ally):
    def __init__(self, name, description, image, max_hp, damage, speed, level,question, quest_encounter, reward_item):
        super().__init__(name, description, image, max_hp, damage, speed, level)
        self.question = question
        self.quest_encounter = quest_encounter
        self.reward_item = reward_item

    
    #Quest for player from npc, specific enemy encounter to get the reward item 
    def quest(self):
        write(self.question)
        enemy_encounter(player, 1, self.quest_encounter)
 

# --- Item klasserna ---

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

class Usable(Item):
    def __init__(self, name, description, used):
        super().__init__(name, description)
        self.used = used

    def unused(self):
        return self.used > 0

# Boostar skada eller dmg resistance       
class Equipable(Item):
    def __init__(self, name, description, type, bonus):
        super().__init__(name, description)
        self.type = type  # vapen och rustning
        self.bonus = bonus  


# --- Declaration of items ---
class Items():
    # Weapons
    stone = Equipable("Smol stone :)", "A small, but powerfull stone (+2 damage)", "weapon", 2)
    stick = Equipable("Battle Stick", "Looks insanely cool (+5 damage)", "weapon", 5)

    # Armour
    hat = Equipable("Smol Hat, hihi", "Simple protection (+1 defense)", "armour", 1)
    Necklace = Equipable("Magical ruby necklace", "Magical armour (+3 defense)", "armour", 3)


# --- Declaration of enemies and npc ---

#In class you declare enemies, you can use them easily by enemies.X
class Enemies():

    rat = Enemy("Monster rat","A big rat", '''       ____()()
          /      @@
    `~~~~~\\_;m__m._>o ''', 30, 5,2)
    bird = Enemy("Big bird","A bird of pray", '''  `-`-.
      '( @ >
       _) (
      /    )
     /_,'  / 
       \\  / 
       m""m''', 25, 2,4)
    frog = Enemy("Posion Frog","A poisonus frog",'''              _         _
      __   ___.--'_`. 
     ( _`.'. -   'o` )
     _\\.'_'      _.-' 
    ( \\`. )    //\\`   
     \\_`-'`---'\\\\__,  
      \\`        `-\\   
       `              ''',25,3,3)
    
#In class you declare NPC, you can use them easily by npc.X
class Npcs():
    bird = Npc("Little bird","A small bird",'''   ,_
>' )
( ( \\ 
 ''|\\ ''',20,2,5,1, "Here is your quest, you need to ......",[Enemies.bird], Items.stone)



# --- Spelare klassen ---

class Player(Ally):
    def __init__(self, name):
        super().__init__(name, "The Hero", '''     _
  |\'/-..--.
 / _ _   ,  ;
`~=`Y'~_<._./
 <`-....__.'  ''', 30, 5, 3, 1)
        self.inventory = []

    def add_item(self, item):
        self.inventory.append(item)
        print(f"Obtained item: {item.name} - {item.description}")

    def equip_item(self):
        equipables = [item for item in self.inventory if isinstance(item, Equipable)]
        if not equipables:
            print("You have no equipment to equip.")
            return

        print("\nChoose equipment to equip:")
        for i, item in enumerate(equipables):
            print(f"{i+1}. {item.name} - {item.description}")

        choice = input("Enter number: ")
        if choice.isdigit():
            idx = int(choice) - 1
            if 0 <= idx < len(equipables):
                item = equipables[idx]
                if item.type == "weapon":
                    self.equipped_weapon = item
                    self.damage = 5 + item.bonus
                    print(f"You equipped {item.name}. Damage increased to {self.damage}")
                elif item.type == "armour":
                    self.equipped_armour = item
                    print(f"You equipped {item.name}. Armour bonus: {item.bonus}")

    def use_items(self):
        if not self.inventory:
            print("You have no items!")
            return False

        usable_items = [item for item in self.inventory if isinstance(item, Usable) and item.unused()]
        if not usable_items:
            print("You have no usable items left!")
            return False

        print("\nChoose an item to use:")
        for i, item in enumerate(usable_items):
            print(f"{i+1}. {item.name} - {item.description}")

        choice = input("Enter the number of the item: ")
        if choice.isdigit():
            idx = int(choice) - 1
            if 0 <= idx < len(usable_items):
                item = usable_items[idx]
                print(f"You used {item.name}!")
                if item.name == "Health Potion":
                    heal_amount = 10
                    player.hp = min(player.max_hp, player.hp + heal_amount)
                    print(f"You healed {heal_amount} HP! Current HP: {player.hp}/{player.max_hp}")
                item.used -= 1
                return True

        print("Invalid choice.")
        return False

    def player_stats(self):
        print(f"Statistics: \nDamage: {self.damage} + {Item.bonus} \nHealth: {self.hp}")


# --- Encounters ---
player = Player("cat")
ally_list = [player]
enemy_list = []
fight_order= []


def enemy_generation(amount : int, options : list[Enemy]) -> None:

    for _ in range(amount):
        choice = rand.choice(options)
        copied = copy.deepcopy(choice)
        enemy_list.append(copied)

#Fighting order of entities in fight determend by thier speed
def set_figting_order():
    global fight_order
    fight_order = concat(enemy_list,ally_list)

    fight_order.sort(key=lambda a: a.speed)
    fight_order = fight_order[::-1]

def enemy_encounter(player,amount,options):

    enemy_generation(amount, options)
    print("\nYou encounter an enemy!")
    for enemy in enemy_list:
        enemy.print_self()
    set_figting_order()
    print("figting order:")
    print(fight_order)

    while len(enemy_list) > 0 and len(ally_list) > 0:
        for entity in fight_order:
            if len(enemy_list) == 0 or len(ally_list) == 0:
                return
            entity.Find_target()

    if player.is_alive():
        print("You defeated the enemy!")
        potion = Usable("Health Potion", "Restores 10 HP", 1)
        player.add_item(potion)
    else:
        print("You have fallen in battle...")


# A npc appears, uses specific npc for information
def npc_interaction(player, npc_option):

    #quest started
    npc_option.quest()

    print(f"\nYou helped the kind {npc_option.name}!\n")
    choice = input(f"How can the {npc_option.name} help? \n1) Give you a Stone (+2dmg) \n2) Join your team")
    
    #reward item added to inventory
    if choice == "1":
        player.add_item(npc_option.reward_item)
        player.equip_item()
    else:

        #the npc becomes players ally
        ally_list.append(npc_option)
        print(f"the kind {npc_option.name} joined your team")

#A trap appears and player loses hp
def trap_event(player):
    print("\n You triggered a trap! You lose 5 HP. Hehehe, you suck")
    player.hp -= 5
    if player.hp < 0:
        player.hp = 0
    print(f"Your HP is now {player.hp}/{player.max_hp}")


#Rooms are declared
class Room():
    def __init__(self, name, desc,enemy_options, enemy_amount, npc_option):
        self.name = name
        self.desc = desc
        self.enemy_options = []
        self.enemy_amount = enemy_amount
        self.npc_option = npc_option

        #Makes copy of enemy, it is the copy that the room uses
        for enemy in enemy_options:
            copied = copy.deepcopy(enemy)
            self.enemy_options.append(copied)

    def __repr__(self):
        return self.name

    #What happens when entering room
    def enter_room(self, player):
        print(f"You have entered {self.name}. {self.desc}")

        #When entering a room there is a 1/3 chance of either enemy, npc or trap to appear
        random_encounter = rand.randint(0,1)
        if random_encounter == 0:
            enemy_encounter(player, self.enemy_amount,self.enemy_options)
        elif random_encounter == 1:
            npc_interaction(player, self.npc_option)
        else:
            trap_event(player)

#In class you declare Rooms, you can use them easily by enemies.Rooms
class Rooms():      
    street = Room("The street", "a very busy street with cars and people.",[Enemies.bird,Enemies.rat],1, Npcs.bird)
    park = Room("The park", "it has many trees and a small lake.",[Enemies.bird,Enemies.frog],2, Npcs.bird)
    market_ally = Room("The market ally", "a narrow street ally with many diffrent stands selling everything you could think of. If you are lucky you may also find useful lost items.",[Enemies.rat,Enemies.bird],2, Npcs.bird)


# --- Hur spelet fungerar (Grenar) ---
#Prints and lets the player choose where to go to next
def road_choice(player, choice_1, choice_2, choice_3 = ""):
    i = 0
    while i < 1:
        print("Where do you want to go next?")
        print(f"1. {choice_1}")
        print(f"2. {choice_2}")
        print(f"3. {choice_3}")

        #Let player choose way
        choice = int(input('''Answer with "1","2" or "3": '''))
        if choice < 1 or choice > 3:
            print("Invalid choice, please choose one of the oftional places to go to.")
            continue

        #Entering room depending on choice
        if choice == 1:
            choice_1.enter_room(player)
        elif choice == 2:
            choice_2.enter_room(player)
        else:
            choice_3.enter_room(player)
        i+=1



# --- writing system ---

#Funtion like print but writes each letter with delay
def write(string):
    # For-loop which writes each letter with delay
    for cha in string:
        print(cha,end="",flush=True)
        # Wait before repeat loop
        time.sleep(0.05)
    print("")

# --- Clear console function ---
#Clear console if player clicks on something
def clear_console():
    write("Press any button to continue...")

    #Waiting for any key on keyboard to be pressed to contine
    msvcrt.getch()

    #clearing console
    os.system('cls')

# --- funktion for att starta spelet ---

def start_up_game():

    scrole = [''' _____  _____ 
( ___ )( ___ )
 |   |  |   | 
 |   |  |   | 
 |___|  |___| 
(_____)(_____)''',''' _____         _____ 
( ___ )-------( ___ )
 |   |         |   | 
 |   |   ____  |   | 
 |   |  / ___| |   | 
 |   | | |     |   | 
 |   | | |___  |   | 
 |   |  \\____| |   | 
 |___|         |___| 
(_____)-------(_____)''',''' _____              _____ 
( ___ )------------( ___ )
 |   |              |   | 
 |   |   ____       |   | 
 |   |  / ___|__ _  |   | 
 |   | | |   / _` | |   | 
 |   | | |__| (_| | |   | 
 |   |  \\____\\__,_| |   | 
 |___|              |___| 
(_____)------------(_____)''',''' _____                  _____ 
( ___ )----------------( ___ )
 |   |                  |   | 
 |   |   ____      _    |   | 
 |   |  / ___|__ _| |_  |   | 
 |   | | |   / _` | __| |   | 
 |   | | |__| (_| | |_  |   | 
 |   |  \\____\\__,_|\\__| |   | 
 |___|                  |___| 
(_____)----------------(_____)''',''' _____                   _____ 
( ___ )-----------------( ___ )
 |   |                   |   | 
 |   |   ____      _     |   | 
 |   |  / ___|__ _| |_   |   | 
 |   | | |   / _` | __|  |   | 
 |   | | |__| (_| | |_   |   | 
 |   |  \\____\\__,_|\\__|  |   | 
 |___|                   |___| 
(_____)-----------------(_____)''',''' _____                            _____ 
( ___ )--------------------------( ___ )
 |   |                            |   | 
 |   |   ____      _        _     |   | 
 |   |  / ___|__ _| |_     / \\    |   | 
 |   | | |   / _` | __|   / _ \\   |   | 
 |   | | |__| (_| | |_   / ___ \\  |   | 
 |   |  \\____\\__,_|\\__| /_/   \\_\\ |   | 
 |___|                            |___| 
(_____)--------------------------(_____)''',''' _____                                 _____ 
( ___ )-------------------------------( ___ )
 |   |                                 |   | 
 |   |   ____      _        _          |   | 
 |   |  / ___|__ _| |_     / \\   _ __  |   | 
 |   | | |   / _` | __|   / _ \\ | '__| |   | 
 |   | | |__| (_| | |_   / ___ \\| |    |   | 
 |   |  \\____\\__,_|\\__| /_/   \\_\\_|    |   | 
 |___|                                 |___| 
(_____)-------------------------------(_____)''',''' _____                                     _____ 
( ___ )-----------------------------------( ___ )
 |   |                                     |   | 
 |   |   ____      _        _         _    |   | 
 |   |  / ___|__ _| |_     / \\   _ __| |_  |   | 
 |   | | |   / _` | __|   / _ \\ | '__| __| |   | 
 |   | | |__| (_| | |_   / ___ \\| |  | |_  |   | 
 |   |  \\____\\__,_|\\__| /_/   \\_\\_|   \\__| |   | 
 |___|                                     |___| 
(_____)-----------------------------------(_____)''',''' _____                                      _____ 
( ___ )------------------------------------( ___ )
 |   |                                      |   | 
 |   |   ____      _        _         _     |   | 
 |   |  / ___|__ _| |_     / \\   _ __| |_   |   | 
 |   | | |   / _` | __|   / _ \\ | '__| __|  |   | 
 |   | | |__| (_| | |_   / ___ \\| |  | |_   |   | 
 |   |  \\____\\__,_|\\__| /_/   \\_\\_|   \\__|  |   | 
 |___|                                      |___| 
(_____)------------------------------------(_____)''',''' _____                                             _____ 
( ___ )-------------------------------------------( ___ )
 |   |                                             |   | 
 |   |   ____      _        _         _      ___   |   | 
 |   |  / ___|__ _| |_     / \\   _ __| |_   / _ \\  |   | 
 |   | | |   / _` | __|   / _ \\ | '__| __| | | | | |   | 
 |   | | |__| (_| | |_   / ___ \\| |  | |_  | |_| | |   | 
 |   |  \\____\\__,_|\\__| /_/   \\_\\_|   \\__|  \\___/  |   | 
 |___|                                             |___| 
(_____)-------------------------------------------(_____)''',''' _____                                                 _____ 
( ___ )-----------------------------------------------( ___ )
 |   |                                                 |   | 
 |   |   ____      _        _         _      ___   __  |   | 
 |   |  / ___|__ _| |_     / \\   _ __| |_   / _ \\ / _| |   | 
 |   | | |   / _` | __|   / _ \\ | '__| __| | | | | |_  |   | 
 |   | | |__| (_| | |_   / ___ \\| |  | |_  | |_| |  _| |   | 
 |   |  \\____\\__,_|\\__| /_/   \\_\\_|   \\__|  \\___/|_|   |   | 
 |___|                                                 |___| 
(_____)-----------------------------------------------(_____)''',''' _____                                                     _____ 
( ___ )---------------------------------------------------( ___ )
 |   |                                                     |   | 
 |   |   ____      _        _         _      ___   __  __  |   | 
 |   |  / ___|__ _| |_     / \\   _ __| |_   / _ \\ / _|/ _| |   | 
 |   | | |   / _` | __|   / _ \\ | '__| __| | | | | |_| |_  |   | 
 |   | | |__| (_| | |_   / ___ \\| |  | |_  | |_| |  _|  _| |   | 
 |   |  \\____\\__,_|\\__| /_/   \\_\\_|   \\__|  \\___/|_| |_|   |   | 
 |___|                                                     |___| 
(_____)---------------------------------------------------(_____)''',''' _____                                                       _____ 
( ___ )-----------------------------------------------------( ___ )
 |   |                                                       |   | 
 |   |   ____      _        _         _      ___   __  __ _  |   | 
 |   |  / ___|__ _| |_     / \\   _ __| |_   / _ \\ / _|/ _| | |   | 
 |   | | |   / _` | __|   / _ \\ | '__| __| | | | | |_| |_| | |   | 
 |   | | |__| (_| | |_   / ___ \\| |  | |_  | |_| |  _|  _| | |   | 
 |   |  \\____\\__,_|\\__| /_/   \\_\\_|   \\__|  \\___/|_| |_| |_| |   | 
 |___|                                                       |___| 
(_____)-----------------------------------------------------(_____)''',''' _____                                                         _____ 
( ___ )-------------------------------------------------------( ___ )
 |   |                                                         |   | 
 |   |   ____      _        _         _      ___   __  __ _ _  |   | 
 |   |  / ___|__ _| |_     / \\   _ __| |_   / _ \\ / _|/ _| (_) |   | 
 |   | | |   / _` | __|   / _ \\ | '__| __| | | | | |_| |_| | | |   | 
 |   | | |__| (_| | |_   / ___ \\| |  | |_  | |_| |  _|  _| | | |   | 
 |   |  \\____\\__,_|\\__| /_/   \\_\\_|   \\__|  \\___/|_| |_| |_|_| |   | 
 |___|                                                         |___| 
(_____)-------------------------------------------------------(_____)''',''' _____                                                               _____ 
( ___ )-------------------------------------------------------------( ___ )
 |   |                                                               |   | 
 |   |   ____      _        _         _      ___   __  __ _ _        |   | 
 |   |  / ___|__ _| |_     / \\   _ __| |_   / _ \\ / _|/ _| (_)_ __   |   | 
 |   | | |   / _` | __|   / _ \\ | '__| __| | | | | |_| |_| | | '_ \\  |   | 
 |   | | |__| (_| | |_   / ___ \\| |  | |_  | |_| |  _|  _| | | | | | |   | 
 |   |  \\____\\__,_|\\__| /_/   \\_\\_|   \\__|  \\___/|_| |_| |_|_|_| |_| |   | 
 |___|                                                               |___| 
(_____)-------------------------------------------------------------(_____)''',''' _____                                                                    _____ 
( ___ )------------------------------------------------------------------( ___ )
 |   |                                                                    |   | 
 |   |   ____      _        _         _      ___   __  __ _ _             |   | 
 |   |  / ___|__ _| |_     / \\   _ __| |_   / _ \\ / _|/ _| (_)_ __   ___  |   | 
 |   | | |   / _` | __|   / _ \\ | '__| __| | | | | |_| |_| | | '_ \\ / _ \\ |   | 
 |   | | |__| (_| | |_   / ___ \\| |  | |_  | |_| |  _|  _| | | | | |  __/ |   | 
 |   |  \\____\\__,_|\\__| /_/   \\_\\_|   \\__|  \\___/|_| |_| |_|_|_| |_|\\___| |   | 
 |___|                                                                    |___| 
(_____)------------------------------------------------------------------(_____)''']

    write("=== Welcome to ===")
    for frame in scrole:
        os.system('cls')
        print("=== Welcome to ===")
        print(frame)
        time.sleep(0.15)

    clear_console()
    write("The cat wakes up by the loud noices from the streets of the city, at first it feels like a completely normal morning. But something is wrong, the cat can't find it's family. It searches everywhere but can't find them. When the cat comes back home after the long search a crow sits in the little tree nearby. Someting very weird then happend, the crow talked.")
    write("Dear cat, yes you. I have something very important to tell you. - Crow")
    clear_console()
    name = input("Enter your cat's name:\n")

    clear_console()

    player = Player(name)
    write(f"Welcome, {player.name}! Your mission is to find all the three lost pieces of the cat amullet. When the amulet is complete all the cats will return. On your journey you will have to play smart, in some situations you have to be kind, in other you have to be brave. Good luck!")
    
    clear_console()
    write(f"Here are the stats for {name}:") 
    player.print_self()




# --- Main game ---
def main_game():
    start_up_game()
    while len(ally_list) > 0:
        road_choice(player, Rooms.street, Rooms.park,Rooms.market_ally)


    write("\nThanks for playing!")


main_game()
