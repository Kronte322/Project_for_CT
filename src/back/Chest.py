from src.back.Config import *


class Chest:
    def __init__(self, position_on_the_map, size_of_chest):
        self.position_on_the_map = position_on_the_map
        self.list_with_items = []
        self.size_of_chest = size_of_chest

    def AddNewItem(self, item):
        self.list_with_items.append(item)

    def PopItem(self, item):
        self.list_with_items.pop(self.list_with_items.index(item))

    def GetCenterOfTheChest(self):
        self.position_on_the_map[0] += self.size_of_chest[0] // 2
        self.position_on_the_map[1] += self.size_of_chest[1] // 2


class BasicChest(Chest):
    def __init__(self, position_on_the_map):
        super().__init__(position_on_the_map, SIZE_OF_BASIC_CHEST)
