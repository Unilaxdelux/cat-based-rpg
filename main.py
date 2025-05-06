from operator import concat
import random as rand
import time
from turtle import delay
import os
import copy

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
        action = input("Choose an action (1 or 2): ")

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
                return  # Skippar din tur om du inte har item att anvanda :(
        else:
            print("Invalid action. You hesitate...")
            return



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

class Equipable(Item):
    def __init__(self, name, description, type, bonus):
        super().__init__(name, description)
        self.type = type  # vapen och rustning
        self.bonus = bonus  # Boostar skada eller dmg resistance

# Weapons
stone = Equipable("Smol stone :)", "A small, but powerfull stone (+2 damage)", "weapon", 2)
stick = Equipable("Battle Stick", "Looks insanely cool (+5 damage)", "weapon", 5)

# Armour
hat = Equipable("Smol Hat, hihi", "Simple protection (+1 defense)", "armour", 1)
Necklace = Equipable("Magical ruby necklace", "Magical armour (+3 defense)", "armour", 3)




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

def npc_interaction(player):
    allies = [Ally("Little bird","A small bird",'''   ,_
>' )
( ( \\ 
 ''|\\ ''',20,2,5,1)]
    print("\nYou meet a kind bird who wants to help!")
    choice = input("how can the bird help? \n1) give you a Smol stone +2dam \n2) join your team")
    if choice == "1":
        player.add_item(stone)
        player.equip_item()
    else:
        ally_list.append(allies[0])
        print("the Smol bird joined your team")

def trap_event(player):
    print("\n You triggered a trap! You lose 5 HP. Hehehe, you suck")
    player.hp -= 5
    if player.hp < 0:
        player.hp = 0
    print(f"Your HP is now {player.hp}/{player.max_hp}")




#Rooms are declared
class Room():
    def __init__(self, name, desc,enemy_options):
        self.name = name
        self.desc = desc
        self.enemy_options = []

        #Makes copy of enemy, it is the copy that the room uses
        for enemy in enemy_options:
            copied = copy.deepcopy(enemy)
            self.enemy_options.append(copied)
        
        #eventuellt change if easier method found
        for enemy in enemy_options:
            self.enemy_options.append(copy.deepcopy(enemy))

    def __repr__(self):
        return self.name

    def enter_room(self, player):
        print(f"You have entered {self.name}. {self.desc}")

        #When entering room where is a 1/3 chance of ethier enemy, npc or trap to appear
        random_encounter = rand.randint(0,1)
        if random_encounter == 0:
            enemy_encounter(player,6,self.enemy_options)
        elif random_encounter == 1:
            npc_interaction()
        else:
            trap_event()

       
        

rooms = [Room("The street", "a very busy street with cars and people.",[Enemies.bird,Enemies.rat]), 
         Room("The park", "it has many trees and a small lake.",[Enemies.bird,Enemies.frog]), 
         Room("The market ally", "a narrow street ally with many diffrent stands selling everything you could think of. If you are lucky you may also find useful lost items.",[Enemies.rat,Enemies.bird])
         ]


# --- Hur spelet fungerar (Grenar) ---
#Prints and lets the player choose where to go to next
def road_choice(player, choice_1, choice_2, choice_3 = ""):
    i = 0
    while i < 1:
        print("Where do you want to go next?")
        print(f"1. {choice_1}")
        print(f"2. {choice_2}")
        print(f"3. {choice_3}")

        choice = int(input('''Answer with "1","2" or "3": '''))
        if choice < 1 or choice > 3:
            print("Invalid choice, please choose one of the oftional places to go to.")
            continue

        if choice == 1:
            choice_1.enter_room(player)
        elif choice == 2:
            choice_2.enter_room(player)
        else:
            choice_3.enter_room(player)
        i+=1



# --- writing system ---

def write(string):
    # For-loop which writes each letter with delay
    for cha in string:
        print(cha,end="",flush=True)
        # Wait before repeat loop
        time.sleep(0.05)
    print("")


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

    #Gora console blank !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    write("\nThe cat wakes up by the loud noices from the streets of the city, at first it feels like a completely normal morning. But something is wrong, the cat can't find it's family. It searches everywhere but can't find them. When the cat comes back home after the long search a crow sits in the little tree nearby. Someting very weird then happend, the crow talked.")
    write("Dear cat, yes you. I have something very important to tell you. - Crow")
    #print("") CONTINUE CONVERSASION !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    name = input("Enter your cat's name:\n")

    player = Player(name)
    write(f"\nWelcome, {player.name}! Your mission is to find all the three lost pieces of the cat amullet. When the amulet is complete all the cats will return. On your journey you will have to play smart, in some situations you have to be kind, in other you have to be brave. Good luck!")
    
    #GORA console blank !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    write(f"Here are the stats for {name}:") 
    player.print_self()

    write("")


# --- Main game ---
def main_game():
    #start_up_game()
    while len(ally_list) > 0:
        road_choice(player, rooms[0], rooms[1], rooms[2])


    write("\nThanks for playing!")


main_game()
