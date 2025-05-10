from utilities import row_devider

class Entity:
    def __init__(self,name,description,image, max_hp,damage,speed):
        self.name = name
        self.description = description
        self.image = image
        self.max_hp = max_hp
        self.hp = max_hp
        self.damage = damage
        self.speed = speed
        self.dead = False

    def __repr__(self):
        return self.name

    def is_alive(self):
        return not self.dead
    '''
    Returns whether that target was killed.
    '''

    def print_self(self):
        print(f"{self.name}:")
        print(self.description)
        print(self.image)
        print(f"Hp: {self.hp}/{self.max_hp}")
        print(f"Damge: {self.damage}")


    def attack(self, target) -> bool:
        '''
        Attacks the target of type entity.
        Returns whether that target was killed.
        '''
        target.hp -= self.damage
        if target.hp <= 0:
            target.hp = 0
            target.dead = True


        print(f"{self.name} attacked {target.name}, dealing {self.damage} damage!")
        print(f"{target.name}'s HP is now {target.hp}/{target.max_hp}")
        row_devider()
        return target.dead




