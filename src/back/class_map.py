import pygame
import random
import time
import sys
from src.back import map_generator

# from src.front.testmain import kSpawnPosition
kSpawnPosition = [1920 // 2, 1000 // 2]

random.seed(time.time())
# random.seed(12)

kSizeOfTile = 12
kSizeOfMap = (128, 128)
# kSizeOfMap = (20, 20)
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

genered_floor = {}


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
        self.dfs = map_generator.DFSAlgo(self.map_generator)
        self.visited_tiles = {}
        self.tiles_for_current_room = {}
        self.current_matrix = []
        self.current_room = pygame.Surface((0, 0))
        self.saved_rooms = {}
        self.global_map_position = [0, 0]
        self.current_room_position = [0, 0]
        self.Blit(self.mappa, self.matrix_with_map, (0, 0))

    def BlitMap(self, list_with_map):
        left_upper_corner = (
            min(list_with_map, key=lambda item: item[0][0])[0][0],
            min(list_with_map, key=lambda item: item[0][1])[0][1])
        right_down_corner = (
            max(list_with_map, key=lambda item: item[0][0])[0][0],
            max(list_with_map, key=lambda item: item[0][1])[0][1])
        width = right_down_corner[0] - left_upper_corner[0] + 1
        height = right_down_corner[1] - left_upper_corner[1] + 1
        self.current_room = pygame.Surface((width * kSizeOfTile,
                                            height * kSizeOfTile))
        matrix_with_map = []
        for i in range(width):
            interm = []
            for j in range(height):
                interm.append(map_generator.kEmpty)
            matrix_with_map.append(interm)

        for i in list_with_map:
            matrix_with_map[i[0][0] - left_upper_corner[0]][i[0][1] - left_upper_corner[1]] = i[1]
        self.Blit(self.current_room, matrix_with_map, left_upper_corner)
        return left_upper_corner

    @staticmethod
    def Blit(surface, matrix, left_corner):
        x, y = 0, 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] in [map_generator.kFloor, map_generator.kPath]:
                    if (i + left_corner[0], j + left_corner[1]) in genered_floor:
                        surface.blit(genered_floor[(i + left_corner[0], j + left_corner[1])], (x, y))
                    else:
                        genered_floor[(i + left_corner[0], j + left_corner[1])] = random.choice(list_with_floor)
                        surface.blit(genered_floor[(i + left_corner[0], j + left_corner[1])], (x, y))
                elif matrix[i][j] == map_generator.kDoor:
                    surface.blit(image_for_door, (x, y))
                elif matrix[i][j] == map_generator.kUpWall:
                    surface.blit(random.choice(list_with_up_walls), (x, y))
                elif matrix[i][j] == map_generator.kDownWall:
                    surface.blit(random.choice(list_with_down_walls), (x, y))
                elif matrix[i][j] == map_generator.kRightWall:
                    surface.blit(random.choice(list_with_right_walls), (x, y))
                elif matrix[i][j] == map_generator.kLeftWall:
                    surface.blit(random.choice(list_with_left_walls), (x, y))
                elif matrix[i][j] == map_generator.kLeftDownInCorner:
                    surface.blit(image_for_left_down_in_corner, (x, y))
                elif matrix[i][j] == map_generator.kLeftDownOutCorner:
                    surface.blit(image_for_left_down_out_corner, (x, y))
                elif matrix[i][j] == map_generator.kRightDownInCorner:
                    surface.blit(image_for_right_down_in_corner, (x, y))
                elif matrix[i][j] == map_generator.kRightDownOutCorner:
                    surface.blit(image_for_right_down_out_corner, (x, y))
                else:
                    surface.blit(image_for_empty, (x, y))
                y += kSizeOfTile
            x += kSizeOfTile
            y = 0

    def GetTile(self, position):
        return self.matrix_with_map[position[0] // kSizeOfTile][position[1] // kSizeOfTile]

    @staticmethod
    def GetPositionOfTile(position):
        return position[0] // kSizeOfTile, position[1] // kSizeOfTile

    def CanStandThere(self, position):
        tile = self.GetTile((position[0] - self.global_map_position[0], position[1] - self.global_map_position[1]))
        return tile in [map_generator.kFloor, map_generator.kDoor, map_generator.kPath]

    def SetCurrentRoom(self, player_position, flag=False):
        if not flag:
            player_position = [player_position[0] - self.global_map_position[0],
                               player_position[1] - self.global_map_position[1]]

        if (self.GetPositionOfTile(player_position), self.GetTile(player_position)) not in list(
                self.tiles_for_current_room.keys()):
            if self.GetPositionOfTile(player_position) not in list(self.saved_rooms.keys()):
                current_room = []
                self.tiles_for_current_room = {}
                keys = []
                if self.GetTile(player_position) in [map_generator.kPath]:
                    self.dfs.DFSOnTheSpecificTiles(self.GetPositionOfTile(player_position), current_room,
                                                   [map_generator.kPath, map_generator.kDoor], depth=10)
                    self.tiles_for_current_room[
                        (self.GetPositionOfTile(player_position), self.GetTile(player_position))] = True
                elif self.map_generator.GetTile(self.GetPositionOfTile(player_position)) in [map_generator.kFloor,
                                                                                             map_generator.kDoor]:
                    self.dfs.DFSOnTheSpecificTiles(self.GetPositionOfTile(player_position), current_room,
                                                   map_generator.kWalls + [map_generator.kDoor, map_generator.kFloor],
                                                   keys=keys, flag='room')
                    for i in current_room:
                        self.tiles_for_current_room[i] = True
                if (self.GetPositionOfTile(player_position), self.GetTile(player_position)) not in list(
                        self.visited_tiles.keys()):
                    for i in current_room:
                        self.visited_tiles[i] = True
                left_upper_corner = self.BlitMap(current_room)
                copy = [self.current_room.copy(), left_upper_corner, self.tiles_for_current_room.copy()]
                for i in keys:
                    self.saved_rooms[i] = copy
                self.current_room_position = [
                    self.global_map_position[0] + left_upper_corner[0] * kSizeOfTile,
                    self.global_map_position[1] + left_upper_corner[1] * kSizeOfTile]

            else:
                self.current_room = self.saved_rooms[self.GetPositionOfTile(player_position)][0]
                self.tiles_for_current_room = self.saved_rooms[self.GetPositionOfTile(player_position)][2]
                self.current_room_position = [
                    self.global_map_position[0] + self.saved_rooms[self.GetPositionOfTile(player_position)][1][
                        0] * kSizeOfTile,
                    self.global_map_position[1] + self.saved_rooms[self.GetPositionOfTile(player_position)][1][
                        1] * kSizeOfTile]

    def Render(self, display):
        display.blit(self.mappa, self.global_map_position)
        # display.blit(self.current_room, self.current_room_position)

    def MoveMap(self, position):
        self.global_map_position[0] += position[0]
        self.global_map_position[1] += position[1]
        self.current_room_position[0] += position[0]
        self.current_room_position[1] += position[1]

    def SpawnPosition(self):
        while True:
            x = random.randrange(1, kSizeOfMap[0])
            y = random.randrange(1, kSizeOfMap[1])
            if self.matrix_with_map[x][y] in [map_generator.kFloor]:
                self.global_map_position = [-x * kSizeOfTile + kSpawnPosition[0], -y * kSizeOfTile + kSpawnPosition[1]]
                self.SetCurrentRoom((x * kSizeOfTile, y * kSizeOfTile), flag=True)
                return None
