import copy
import random as rand
from utilities import *
from enemies import Enemies
from entites.npc import Npc
from interactions import enemy_encounter, npc_interaction, trap_event

class Room():
    def __init__(self, name, desc,enemy_options, enemy_amount, npc_option: Npc):
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
    def enter_room(self, player, enemy_list, ally_list):
        write(f"You have entered {self.name}. {self.desc}")

        row_devider()

        #When entering a the boss room the boss appears
        if self.enemy_options == Enemies.cerberus:
            enemy_encounter(player,1,self.enemy_options, enemy_list, ally_list)
        
        #When entering a room there is a 1/3 chance of either enemy, npc or trap to appear
        else:
            random_encounter = rand.randint(0,1)
            if random_encounter == 0:
                enemy_encounter(player, self.enemy_amount,self.enemy_options, enemy_list, ally_list)
            elif random_encounter == 1:
                npc_interaction(player, self.npc_option, enemy_list, ally_list)
            else:
                trap_event(player)
