from npcs import Npcs
from enemies import Enemies
from room import Room

#In class you declare Rooms, you can use them easily by Rooms.x
class Rooms():      
    street = Room("The street", "a very busy street with cars and people.",[Enemies.bird,Enemies.rat],1, Npcs.bird)
    park = Room("The park", "it has many trees and a small lake.",[Enemies.bird,Enemies.frog],2, Npcs.bird)
    market_ally = Room("The market ally", "a narrow street ally with many diffrent stands selling everything you could think of. If you are lucky you may also find useful lost items.",[Enemies.rat,Enemies.bird],2, Npcs.bird)
    boss_room = Room("Boss Room","The final battle will soon take place.",[Enemies.cerberus],1,None)