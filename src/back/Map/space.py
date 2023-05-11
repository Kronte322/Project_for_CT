from abc import ABC, abstractmethod

import src.back.Map.map
from src.back.Map.constants_for_map import *


class Space(ABC):
    def __init__(self, tiles, keys):
        self.tiles = tiles
        self.tiles_as_dict = {tile[0]: tile[1] for tile in self.tiles}
        self.keys = keys
        self.left_upper_corner = src.back.Map.map.Map.GetLeftUpperCornerForListOfTiles(self.tiles)

    def GetPosition(self):
        return self.left_upper_corner[0] * SIZE_OF_TILE, self.left_upper_corner[1] * SIZE_OF_TILE

    def GetTiles(self):
        return self.tiles

    def IsThere(self, position):
        intermediate = position[0] // SIZE_OF_TILE, position[1] // SIZE_OF_TILE
        return intermediate in self.tiles_as_dict

    def GetCoordinatesOfTiles(self):
        return [tile[0] for tile in self.tiles]

    def GetTile(self, coord):
        if coord in self.tiles_as_dict:
            return self.tiles_as_dict[coord]
        else:
            raise "There is no that coord"

    def GetKeys(self):
        return self.keys

    def GetSizeOfSpace(self):
        return len(self.tiles)

    @abstractmethod
    def GetSurface(self):
        pass


class RoomSpace(Space):
    def __init__(self, tiles, keys, doors):
        super().__init__(tiles, keys)
        self.surface = src.back.Map.map.Map.GetSurface(self.tiles)
        self.doors = doors

    def GetSurface(self):
        return self.surface

    def GetDoors(self):
        return self.doors


class PathSpace(Space):
    def __init__(self, tiles, keys):
        super().__init__(tiles, keys)

    def GetSurface(self):
        return src.back.Map.map.Map.GetSurface(self.tiles)
