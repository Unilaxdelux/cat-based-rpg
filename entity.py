import random as rand

from utilities import *
from interactions import *

# --- Entity classes ---
#region

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
        row_devider()
        return target.dead


class Enemy(Entity):
    def __init__ (self, name, description, image, max_hp, damage, speed):
        super().__init__(name, description, image, max_hp, damage, speed)
        

    def Find_target(self, ally_list):
        target = ally_list[rand.randint(0,len(ally_list)-1)]
        killed = self.attack(target)
        if killed:
            ally_list.remove(target)


class Ally(Entity):
    def __init__(self, name, description, image, max_hp, damage, speed, level):
        super().__init__(name, description, image, max_hp, damage, speed)
        self.level = level
    
    def Find_target(self, enemy_list, ally_list):
        #print(f"what do you want to do using {self}\n")
        #self.print_self()
        while True:
            row_devider()
            print("What will you do?")
            print("1. Attack")
            print("2. Use Item")
            print("3. Check Stats and inventory")
            action = int(input("Choose an action (1, 2 or 3):\n "))
            row_devider()

            if action == 1:
                index = 0
                if len(enemy_list) > 1:
                    print("What enemy do you want to attack\n")
                    i = 1
                    for enemy in enemy_list:
                        print(f"{i}: {enemy.name}: {enemy.hp}/{enemy.max_hp}")
                        i+= 1
                    index = int(input()) - 1
                target = enemy_list[index]

                killed = self.attack(target)
                if killed:
                    enemy_list.remove(target)
                    print(f"You killed a {target.name}!")

                break

            elif action == 2:
                used = self.use_items()

                if not used:
                    continue

            elif action == 3:
                for ally in ally_list:
                    ally.print_self()

                print("\nInventory:")
                #Skriva ut inventory !!!!!!!!!!!!
                continue
            else:
                print("Invalid action. You hesitate...")
                continue

            #If all enemies in room is deafeted
            if len(enemy_list) < 1:
                break



#Class for Npc
class Npc(Ally):
    def __init__(self, name, description, image, max_hp, damage, speed, level,question, quest_encounter, reward_item):
        super().__init__(name, description, image, max_hp, damage, speed, level)
        self.question = question
        self.quest_encounter = quest_encounter
        self.reward_item = reward_item

    
    #Quest for player from npc, specific enemy encounter to get the reward item 
    def quest(self, player):
        write(self.question)
        enemy_encounter(player, 1, self.quest_encounter)

#endregion