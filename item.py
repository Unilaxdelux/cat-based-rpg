class Item:

    items_rewards_list = []

    def __init__(self, name, description, isReward = True):
        self.name = name
        self.description = description
        if isReward == True:
            Item.items_rewards_list.append(self)

class Usable(Item):
    def __init__(self, name, description, used):
        super().__init__(name, description)
        self.used = used

    def unused(self):
        return self.used > 0

# Boostar skada eller dmg resistance       
class Equipable(Item):
    def __init__(self, name, description, type, bonus):
        super().__init__(name, description)
        self.type = type   # vapen och rustning
        self.bonus = bonus  
        

class Progress_item(Item):
    def __init__(self, name, description):
        super().__init__(name, description, False)
