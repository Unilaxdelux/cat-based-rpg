from entites.ally import Ally
from utilities import write

class Npc(Ally):
    def __init__(self, name, description, image, max_hp, damage, speed, level,question, quest_encounter, reward_item):
        super().__init__(name, description, image, max_hp, damage, speed, level)
        self.question = question
        self.quest_encounter = quest_encounter
        self.reward_item = reward_item