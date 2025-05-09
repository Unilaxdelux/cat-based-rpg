from entity import *
from item import *

# --- Player class ---

class Player(Ally):
    symbol = '''     _
  |\'/-..--.
 / _ _   ,  ;
`~=`Y'~_<._./
 <`-....__.'  '''

    def __init__(self, name):
        super().__init__(name, "The Hero", self.symbol, 30, 5, 3, 1)

        self.inventory = []

    def add_item(self, item):
        self.inventory.append(item)
        print(f"Obtained item: {item.name} - {item.description}")

    def equip_item(self):
        equipables = [item for item in self.inventory if isinstance(item, Equipable)]
        if not equipables:
            print("You have no equipment to equip.")
            return

        print("\nChoose equipment to equip:")
        for i, item in enumerate(equipables):
            print(f"{i+1}. {item.name} - {item.description}")

        choice = input("Enter number: ")
        if choice.isdigit():
            idx = int(choice) - 1
            if 0 <= idx < len(equipables):
                item = equipables[idx]
                if item.type == "weapon":
                    self.equipped_weapon = item 
                    self.damage += item.bonus
                    print(f"You equipped {item.name}. Damage increased to {self.damage}")
                elif item.type == "armour":
                    self.equipped_armour = item
                    print(f"You equipped {item.name}. Armour bonus: {item.bonus}")

    def use_items(self):
        if not self.inventory:
            print("You have no items!")
            return False

        usable_items = [item for item in self.inventory if isinstance(item, Usable) and item.unused()]
        if not usable_items:
            print("You have no usable items left!")
            return False

        print("\nChoose an item to use:")
        for i, item in enumerate(usable_items):
            print(f"{i+1}. {item.name} - {item.description}")

        choice = input("Enter the number of the item: ")
        if choice.isdigit():
            idx = int(choice) - 1
            if 0 <= idx < len(usable_items):
                item = usable_items[idx]
                print(f"You used {item.name}!")
                if item.name == "Health Potion":
                    heal_amount = 10
                    self.hp = min(self.max_hp, self.hp + heal_amount)
                    print(f"You healed {heal_amount} HP! Current HP: {self.hp}/{self.max_hp}")
                item.used -= 1
                return True

        print("Invalid choice.")
        return False

    #What is this used for???
    def player_stats(self, item):
        print(f"Statistics: \nDamage: {self.damage} + {item.bonus} \nHealth: {self.hp}")
