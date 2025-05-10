import random as rand
from entites.entity import Entity

class Enemy(Entity):
    def __init__ (self, name, description, image, max_hp, damage, speed):
        super().__init__(name, description, image, max_hp, damage, speed)
        

    def Find_target(self, enemy_list, ally_list):
        target = ally_list[rand.randint(0,len(ally_list)-1)]
        killed = self.attack(target)
        if killed:
            ally_list.remove(target)