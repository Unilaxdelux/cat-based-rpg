from utilities import *
from room import Room

# -- Branches --
#Prints and lets the player choose where to go to next
def road_choice(player, room_1: Room, room_2: Room, room_3: Room = ""):
    i = 0
    while i < 1:
        print("Where do you want to go next?")
        print(f"1. {room_1}")
        print(f"2. {room_2}")
        print(f"3. {room_3}")

        #Let player choose way
        choice = int(input('''Answer with "1","2" or "3": \n'''))
        if choice < 1 or choice > 3:
            print("Invalid choice, please choose one of the oftional places to go to.")
            continue
        clear_console()
        #Entering room depending on choice
        if choice == 1:
            room_1.enter_room(player)
        elif choice == 2:
            room_2.enter_room(player)
        else:
            room_3.enter_room(player)
        i+=1