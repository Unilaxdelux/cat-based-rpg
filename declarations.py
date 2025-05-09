from item import *
from entity import *

# --- Declaration of entites and items ---
#region

#Declaration of items
class Items():
    # Weapons
    stone = Equipable("Smol stone :)", "A small, but powerfull stone (+2 damage)", "weapon", 2)
    stick = Equipable("Battle Stick", "Looks insanely cool (+5 damage)", "weapon", 5)

    # Armour
    hat = Equipable("Smol Hat, hihi", "Simple protection (+1 defense)", "armour", 1)
    Necklace = Equipable("Magical ruby necklace", "Magical armour (+3 defense)", "armour", 3)

    #Usable
    potion = Usable("Health Potion", "Restores 10 HP", 1)

    # Amulet
    amulet = Progress_item("Amulet part","Part of a magical amulet that will bring back the cats if complete")


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
    cerberus = Enemy("","",'''                            /\\_/\\____,
              ,___/\\_/\\ \\  ~     /
              \\     ~  \\ )   XXX
                XXX     /    /\\_/\\___,
                   \\o-o/-o-o/   ~    /
                    ) /     \\    XXX
                   _|    / \\ \\_/
                ,-/   _  \\_/   \\
               / (   /____,__|  )
              (  |_ (    )  \\) _|
             _/ _)   \\   \\__/   (_
     b'ger  (,-(,(,(,/      \\,),),)''',80,8,2)
    
#In class you declare NPC, you can use them easily by npc.X
class Npcs():
    bird = Npc("Little bird","A small bird",'''   ,_
>' )
( ( \\ 
 ''|\\ ''',20,2,5,1, "Here is your quest, you need to ......",[Enemies.bird], Items.stone)

#endregion