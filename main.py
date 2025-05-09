
from operator import concat
import random as rand
import time
from turtle import delay
import os
import copy
import msvcrt

from player import *
from utilities import *
from loading_screen import LoadingScreen
from room import Rooms
from branches import road_choice

# Globals

amount_amulet = 0

enemy_list = []
fight_order= []



# --- Default settings ---

#region
player = Player("Cat")
ally_list = [player]

#endregion


# --- How the game works functions ---
#region



# -- Game startup --
def start_up_game():

    LoadingScreen.paint()

    clear_console()
    write("The cat wakes up by the loud noices from the streets of the city, at first it feels like a completely normal morning. But something is wrong, the cat can't find it's family. It searches everywhere but can't find them. When the cat comes back home after the long search a crow sits in the little tree nearby. Someting very weird then happend, the crow talked.")
    write("Dear cat, yes you. I have something very important to tell you. - Crow")
    clear_console()
    name = input("Enter your cat's name:\n")

    clear_console()

    player.name = name
    write(f"Welcome, {player.name}! Your mission is to find all the three lost pieces of the cat amullet. When the amulet is complete all the cats will return. On your journey you will have to play smart, in some situations you have to be kind, in other you have to be brave. Good luck!")
    
    clear_console()
    write(f"Here are the stats for {name}:") 
    player.print_self()

#endregion


# --- Main game ---

def main_game():
    #start_up_game()

    while len(ally_list) > 0:
        road_choice(player, Rooms.street, Rooms.park ,Rooms.market_ally)

    write("\nThanks for playing!")


#Main -----------------------------------------------------------------------------------------

main_game()
