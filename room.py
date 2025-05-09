from utilities import *
from declarations import *


# --- Rooms ---
#region
#Rooms are declared
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
    def enter_room(self, player):
        write(f"You have entered {self.name}. {self.desc}")

        row_devider()

        #When entering a the boss room the boss appears
        if self.enemy_options == Enemies.cerberus:
            enemy_encounter(player,1,self.enemy_options)
        
        #When entering a room there is a 1/3 chance of either enemy, npc or trap to appear
        else:
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
    boss_room = Room("Boss Room","The final battle will soon take place.",[Enemies.cerberus],1,None)

#endregion