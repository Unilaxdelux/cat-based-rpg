from entites.npc import Npc
from items import Items
from enemies import Enemies

#In class you declare NPC, you can use them easily by npc.X
class Npcs():
    bird = Npc("Little bird","A small bird",'''   ,_
>' )
( ( \\ 
 ''|\\ ''',20,2,5,1, "Here is your quest, you need to ......",[Enemies.bird], Items.stone)