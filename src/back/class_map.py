import pygame
import random
import time
import sys
from src.back import map_generator
# from src.front.testmain import kSpawnPosition
kSpawnPosition = [1920 // 2, 1000 // 2]

random.seed(time.time())
# random.seed(12)

kSizeOfTile = 72
kSizeOfMap = (128, 128)

kNumOfUpWalls = 3
kNumOfDownWalls = 4
kNumOfLeftWalls = 3
kNumOfRightWalls = 3
kNumOfFloors = 14

list_with_up_walls = []
list_with_down_walls = []
list_with_left_walls = []
list_with_right_walls = []
list_with_floor = []

image_for_door = pygame.image.load(
    "../tile_sets/tiles_for_map/doors/sprite_066.png")
image_for_door = pygame.transform.scale(
    image_for_door, (kSizeOfTile, kSizeOfTile))

image_for_empty = pygame.image.load(
    "../tile_sets/tiles_for_map/back_ground/sprite_078.png")
image_for_empty = pygame.transform.scale(
    image_for_empty, (kSizeOfTile, kSizeOfTile))

image_for_left_down_in_corner = pygame.image.load(
    "../tile_sets/tiles_for_map/left_down_corner/in_corner.png")
image_for_left_down_in_corner = pygame.transform.scale(
    image_for_left_down_in_corner, (kSizeOfTile, kSizeOfTile))

image_for_left_down_out_corner = pygame.image.load(
    "../tile_sets/tiles_for_map/left_down_corner/out_corner.png")
image_for_left_down_out_corner = pygame.transform.scale(
    image_for_left_down_out_corner, (kSizeOfTile, kSizeOfTile))

image_for_right_down_in_corner = pygame.image.load(
    "../tile_sets/tiles_for_map/right_down_corner/in_corner.png")
image_for_right_down_in_corner = pygame.transform.scale(
    image_for_right_down_in_corner, (kSizeOfTile, kSizeOfTile))

image_for_right_down_out_corner = pygame.image.load(
    "../tile_sets/tiles_for_map/right_down_corner/out_corner.png")
image_for_right_down_out_corner = pygame.transform.scale(
    image_for_right_down_out_corner, (kSizeOfTile, kSizeOfTile))


def SetImage(path, number, size=kSizeOfTile):
    result = pygame.image.load(path + str(number) + ".png")
    result = pygame.transform.scale(result, (kSizeOfTile, kSizeOfTile))
    return result


def SetTiles():
    for i in range(1, kNumOfUpWalls + 1):
        list_with_up_walls.append(SetImage("../tile_sets/tiles_for_map/up_walls/sprite_", i))
    for i in range(1, kNumOfDownWalls + 1):
        list_with_down_walls.append(SetImage("../tile_sets/tiles_for_map/down_walls/sprite_", i))
    for i in range(1, kNumOfRightWalls + 1):
        list_with_right_walls.append(SetImage("../tile_sets/tiles_for_map/right_walls/sprite_", i))
    for i in range(1, kNumOfLeftWalls + 1):
        list_with_left_walls.append(SetImage("../tile_sets/tiles_for_map/left_walls/sprite_", i))
    for i in range(1, kNumOfFloors + 1):
        list_with_floor.append(SetImage("../tile_sets/tiles_for_map/floor/sprite_", i))


class Map:
    def __init__(self):
        SetTiles()
        self.map_generator = map_generator.MapGenerator()
        self.matrix_with_map = self.map_generator.GenerateMap(kSizeOfMap)
        self.mappa = pygame.Surface((kSizeOfMap[0] * kSizeOfTile, kSizeOfMap[1] * kSizeOfTile))
        x, y = 0, 0
        for i in range(len(self.matrix_with_map)):
            for tile in self.matrix_with_map[i]:
                if tile in [map_generator.kFloor, map_generator.kPath]:
                    self.mappa.blit(random.choice(list_with_floor), (x, y))
                elif tile == map_generator.kDoor:
                    self.mappa.blit(image_for_door, (x, y))
                elif tile == map_generator.kUpWall:
                    self.mappa.blit(random.choice(list_with_up_walls), (x, y))
                elif tile == map_generator.kDownWall:
                    self.mappa.blit(random.choice(list_with_down_walls), (x, y))
                elif tile == map_generator.kRightWall:
                    self.mappa.blit(random.choice(list_with_right_walls), (x, y))
                elif tile == map_generator.kLeftWall:
                    self.mappa.blit(random.choice(list_with_left_walls), (x, y))
                elif tile == map_generator.kLeftDownInCorner:
                    self.mappa.blit(image_for_left_down_in_corner, (x, y))
                elif tile == map_generator.kLeftDownOutCorner:
                    self.mappa.blit(image_for_left_down_out_corner, (x, y))
                elif tile == map_generator.kRightDownInCorner:
                    self.mappa.blit(image_for_right_down_in_corner, (x, y))
                elif tile == map_generator.kRightDownOutCorner:
                    self.mappa.blit(image_for_right_down_out_corner, (x, y))
                else:
                    self.mappa.blit(image_for_empty, (x, y))
                y += kSizeOfTile
            x += kSizeOfTile
            y = 0

    def GetTile(self, position):
        return self.matrix_with_map[position[0] // kSizeOfTile][position[1] // kSizeOfTile]

    def CanStandThere(self, position):
        tile = self.GetTile(position)
        return tile in [map_generator.kFloor, map_generator.kDoor, map_generator.kPath]

    def Render(self, display, position):
        display.blit(self.mappa, position)

    def SpawnPosition(self):
        while True:
            x = random.randrange(1, kSizeOfMap[0])
            y = random.randrange(1, kSizeOfMap[1])
            if self.matrix_with_map[x][y] in [map_generator.kFloor]:
                return -x * kSizeOfTile + kSpawnPosition[0], -y * kSizeOfTile + kSpawnPosition[1]
