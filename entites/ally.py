from entites.entity import Entity

class Ally(Entity):
    def __init__(self, name, description, image, max_hp, damage, speed, level):
        super().__init__(name, description, image, max_hp, damage, speed)
        self.level = level

    def Find_target(self, enemy_list, ally_list):
        # Attack enemy with lowest hp if same hp ->
        # Attack the enemy highest up (FRIST ENEMY)
        print("Ally attack!")
   
