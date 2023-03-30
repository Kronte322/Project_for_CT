import pygame
import random
import time
from src.back.map_generator import MapBuilder, DFSAlgoForMapBuilder
from src.back.constants_with_paths_to_files import *
from src.back.constants_for_map import *

# from src.front.testmain import kSpawnPosition

random.seed(time.time())
# random.seed(12)

list_with_up_walls = []
list_with_down_walls = []
list_with_left_walls = []
list_with_right_walls = []
list_with_floor = []

image_for_door = pygame.image.load(PATH_TO_DOOR_IMG)
image_for_door = pygame.transform.scale(
    image_for_door, (SIZE_OF_TILE, SIZE_OF_TILE))

image_for_empty = pygame.image.load(PATH_TO_EMPTY_IMG)
image_for_empty = pygame.transform.scale(
    image_for_empty, (SIZE_OF_TILE, SIZE_OF_TILE))

image_for_left_down_in_corner = pygame.image.load(PATH_TO_LEFT_DOWN_IN_CORNER)
image_for_left_down_in_corner = pygame.transform.scale(
    image_for_left_down_in_corner, (SIZE_OF_TILE, SIZE_OF_TILE))

image_for_left_down_out_corner = pygame.image.load(PATH_TO_LEFT_DOWN_OUT_CORNER)
image_for_left_down_out_corner = pygame.transform.scale(
    image_for_left_down_out_corner, (SIZE_OF_TILE, SIZE_OF_TILE))

image_for_right_down_in_corner = pygame.image.load(PATH_TO_RIGHT_DOWN_IN_CORNER)
image_for_right_down_in_corner = pygame.transform.scale(
    image_for_right_down_in_corner, (SIZE_OF_TILE, SIZE_OF_TILE))

image_for_right_down_out_corner = pygame.image.load(PATH_TO_RIGHT_DOWN_OUT_CORNER)
image_for_right_down_out_corner = pygame.transform.scale(
    image_for_right_down_out_corner, (SIZE_OF_TILE, SIZE_OF_TILE))

genered_floor = {}


def SetImage(path, number, size=SIZE_OF_TILE):
    result = pygame.image.load(path + str(number) + EXTENSION_OF_IMG_FILES)
    result = pygame.transform.scale(result, (SIZE_OF_TILE, SIZE_OF_TILE))
    return result


def SetTiles():
    for i in range(1, NUM_OF_UP_WALLS + 1):
        list_with_up_walls.append(SetImage(PATH_TO_UP_WALLS, i))
    for i in range(1, NUM_OF_DOWN_WALLS + 1):
        list_with_down_walls.append(SetImage(PATH_TO_DOWN_WALLS, i))
    for i in range(1, NUM_OF_RIGHT_WALLS + 1):
        list_with_right_walls.append(SetImage(PATH_TO_RIGHT_WALLS, i))
    for i in range(1, NUM_OF_LEFT_WALLS + 1):
        list_with_left_walls.append(SetImage(PATH_TO_LEFT_WALLS, i))
    for i in range(1, NUM_OF_FLOORS + 1):
        list_with_floor.append(SetImage(PATH_TO_FLOORS, i))


class Map:
    def __init__(self):
        SetTiles()
        self.matrix_with_map = MapBuilder.GenerateMap(SIZE_OF_MAP)

        self.mappa = pygame.Surface((SIZE_OF_MAP[0] * SIZE_OF_TILE, SIZE_OF_MAP[1] * SIZE_OF_TILE))

        self.dfs = DFSAlgoForMapBuilder()

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
        self.current_room = pygame.Surface((width * SIZE_OF_TILE,
                                            height * SIZE_OF_TILE))
        matrix_with_map = []
        for i in range(width):
            interm = []
            for j in range(height):
                interm.append(CHAR_FOR_EMPTY)
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
                if matrix[i][j] in [CHAR_FOR_FLOR, CHAR_FOR_PATH]:
                    if (i + left_corner[0], j + left_corner[1]) in genered_floor:
                        surface.blit(genered_floor[(i + left_corner[0], j + left_corner[1])], (x, y))
                    else:
                        genered_floor[(i + left_corner[0], j + left_corner[1])] = random.choice(list_with_floor)
                        surface.blit(genered_floor[(i + left_corner[0], j + left_corner[1])], (x, y))
                elif matrix[i][j] == CHAR_FOR_DOOR:
                    surface.blit(image_for_door, (x, y))
                elif matrix[i][j] == CHAR_FOR_UP_WALL:
                    surface.blit(random.choice(list_with_up_walls), (x, y))
                elif matrix[i][j] == CHAR_FOR_DOWN_WALL:
                    surface.blit(random.choice(list_with_down_walls), (x, y))
                elif matrix[i][j] == CHAR_FOR_RIGHT_WALL:
                    surface.blit(random.choice(list_with_right_walls), (x, y))
                elif matrix[i][j] == CHAR_FOR_LEFT_WALL:
                    surface.blit(random.choice(list_with_left_walls), (x, y))
                elif matrix[i][j] == CHAR_FOR_LEFT_DOWN_IN_CORNER:
                    surface.blit(image_for_left_down_in_corner, (x, y))
                elif matrix[i][j] == CHAR_FOR_LEFT_DOWN_OUT_CORNER:
                    surface.blit(image_for_left_down_out_corner, (x, y))
                elif matrix[i][j] == CHAR_FOR_RIGHT_DOWN_IN_CORNER:
                    surface.blit(image_for_right_down_in_corner, (x, y))
                elif matrix[i][j] == CHAR_FOR_DOWN_OUT_CORNER:
                    surface.blit(image_for_right_down_out_corner, (x, y))
                else:
                    surface.blit(image_for_empty, (x, y))
                y += SIZE_OF_TILE
            x += SIZE_OF_TILE
            y = 0

    def GetTile(self, position):
        return self.matrix_with_map[position[0] // SIZE_OF_TILE][position[1] // SIZE_OF_TILE]

    @staticmethod
    def GetPositionOfTile(position):
        return position[0] // SIZE_OF_TILE, position[1] // SIZE_OF_TILE

    def CanStandThere(self, position):
        tile = self.GetTile((position[0] - self.global_map_position[0], position[1] - self.global_map_position[1]))
        return tile in [CHAR_FOR_FLOR, CHAR_FOR_DOOR, CHAR_FOR_PATH]

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
                if self.GetTile(player_position) in [CHAR_FOR_PATH]:
                    self.dfs.DFSOnTheSpecificTiles(self.matrix_with_map, self.GetPositionOfTile(player_position),
                                                   current_room,
                                                   [CHAR_FOR_PATH, CHAR_FOR_DOOR], depth=5)
                    self.tiles_for_current_room[
                        (self.GetPositionOfTile(player_position), self.GetTile(player_position))] = True
                elif MapBuilder.GetTile(self.matrix_with_map, self.GetPositionOfTile(player_position)) in [
                    CHAR_FOR_FLOR,
                    CHAR_FOR_DOOR]:
                    self.dfs.DFSOnTheSpecificTiles(self.matrix_with_map, self.GetPositionOfTile(player_position),
                                                   current_room,
                                                   SET_WITH_WALLS + [CHAR_FOR_DOOR,
                                                                     CHAR_FOR_FLOR],
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
                    self.global_map_position[0] + left_upper_corner[0] * SIZE_OF_TILE,
                    self.global_map_position[1] + left_upper_corner[1] * SIZE_OF_TILE]

            else:
                self.current_room = self.saved_rooms[self.GetPositionOfTile(player_position)][0]
                self.tiles_for_current_room = self.saved_rooms[self.GetPositionOfTile(player_position)][2]
                self.current_room_position = [
                    self.global_map_position[0] + self.saved_rooms[self.GetPositionOfTile(player_position)][1][
                        0] * SIZE_OF_TILE,
                    self.global_map_position[1] + self.saved_rooms[self.GetPositionOfTile(player_position)][1][
                        1] * SIZE_OF_TILE]

    def Render(self, display):
        # display.blit(self.mappa, self.global_map_position)
        display.blit(self.current_room, self.current_room_position)

    def MoveMap(self, position):
        self.global_map_position[0] += position[0]
        self.global_map_position[1] += position[1]
        self.current_room_position[0] += position[0]
        self.current_room_position[1] += position[1]

    def SpawnPosition(self):
        while True:
            x = random.randrange(1, SIZE_OF_MAP[0])
            y = random.randrange(1, SIZE_OF_MAP[1])
            if self.matrix_with_map[x][y] in [CHAR_FOR_FLOR]:
                self.global_map_position = [-x * SIZE_OF_TILE + SPAWN_POSITION[0], -y * SIZE_OF_TILE + SPAWN_POSITION[1]]
                self.SetCurrentRoom((x * SIZE_OF_TILE, y * SIZE_OF_TILE), flag=True)
                return None
