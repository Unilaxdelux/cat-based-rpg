from operator import concat
import random as rand
import copy

from entity import *
from item import *
from declarations import *

# --- Encounters ---
#region

def enemy_generation(amount : int, options : list[Enemy], enemy_list) -> None:

    for _ in range(amount):
        choice = rand.choice(options)
        copied = copy.deepcopy(choice)
        enemy_list.append(copied)

#Fighting order of entities in fight determend by thier speed
def set_figting_order(enemy_list, ally_list):
    global fight_order
    fight_order = concat(enemy_list,ally_list)

    fight_order.sort(key=lambda a: a.speed)
    fight_order = fight_order[::-1]

def enemy_encounter(player,amount,options, enemy_list, ally_list):

    enemy_generation(amount, options)
    print("You encounter an enemy!")
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
        print("You defeated all the enemies!")
        #Gives random item from the items declared above in class Items
        random_reward = rand.choice(Item.item_rewards_list)
        player.add_item(random_reward)
    else:
        print("You have fallen in battle...")

# A npc appears, uses specific npc for information
def npc_interaction(player, npc_option, ally_list):

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

    if npc_option.reward_item == Items.amulet:
        amount_amulet += 1

#A trap appears and player loses hp
def trap_event(player):
    print("\n You triggered a trap! You lose 5 HP. Hehehe, you suck")
    player.hp -= 5
    if player.hp < 0:
        player.hp = 0
    print(f"Your HP is now {player.hp}/{player.max_hp}")

#Activites and leads the player to the boss fight also incloudes the boss fight 
def boss_active():
    clear_console()
    write("You have now found two of the three parts of the magical cat amulet. I believe you are now ready for the last and hardest challange. My information is that if you follow this road you may find the last piece...")
    
    Rooms.boss_room.enter_room()

#endregion