from item import Equipable, Usable, Progress_item

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
