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

image_for_empty = pygame.image.load(PATH_TO_EMPTY_IMG)

image_for_left_down_in_corner = pygame.image.load(PATH_TO_LEFT_DOWN_IN_CORNER)

image_for_left_down_out_corner = pygame.image.load(PATH_TO_LEFT_DOWN_OUT_CORNER)

image_for_right_down_in_corner = pygame.image.load(PATH_TO_RIGHT_DOWN_IN_CORNER)

image_for_right_down_out_corner = pygame.image.load(PATH_TO_RIGHT_DOWN_OUT_CORNER)

generated_floor = {}


def SetImage(path, number, size_of_tile=SIZE_OF_TILE):
    result = pygame.image.load(path + str(number) + EXTENSION_OF_IMG_FILES)
    return result


def ScaleImage(image, size_of_tile=SIZE_OF_TILE):
    image = pygame.transform.scale(image, (size_of_tile, size_of_tile))
    return image


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
        self.map_for_minimap = pygame.Surface(
            (SIZE_OF_MAP[0] * SIZE_OF_TILE_ON_MINI_MAP, SIZE_OF_MAP[1] * SIZE_OF_TILE_ON_MINI_MAP))
        self.mini_map = pygame.Surface(SIZE_OF_MINI_MAP)

        self.dfs = DFSAlgoForMapBuilder()

        self.visited_tiles = {}
        self.tiles_for_current_room = {}

        self.current_matrix = []
        self.current_room = pygame.Surface((0, 0))

        self.saved_rooms = {}

        self.global_map_position = [0, 0]
        self.current_room_position = [0, 0]
        self.mini_map_position = [0, 0]
        self.position_of_minimap_on_screen = POSITION_OF_MINI_MAP

        self.Blit(self.mappa, self.matrix_with_map, (0, 0))

    @staticmethod
    def BlitTileOnMap(surface, position_for_blit, tile, size_of_tile=SIZE_OF_TILE):
        if tile == CHAR_FOR_DOOR:
            surface.blit(ScaleImage(image_for_door, size_of_tile), position_for_blit)
        elif tile == CHAR_FOR_UP_WALL:
            surface.blit(ScaleImage(random.choice(list_with_up_walls), size_of_tile), position_for_blit)
        elif tile == CHAR_FOR_DOWN_WALL:
            surface.blit(ScaleImage(random.choice(list_with_down_walls), size_of_tile), position_for_blit)
        elif tile == CHAR_FOR_RIGHT_WALL:
            surface.blit(ScaleImage(random.choice(list_with_right_walls), size_of_tile), position_for_blit)
        elif tile == CHAR_FOR_LEFT_WALL:
            surface.blit(ScaleImage(random.choice(list_with_left_walls), size_of_tile), position_for_blit)
        elif tile == CHAR_FOR_LEFT_DOWN_IN_CORNER:
            surface.blit(ScaleImage(image_for_left_down_in_corner, size_of_tile), position_for_blit)
        elif tile == CHAR_FOR_LEFT_DOWN_OUT_CORNER:
            surface.blit(ScaleImage(image_for_left_down_out_corner, size_of_tile), position_for_blit)
        elif tile == CHAR_FOR_RIGHT_DOWN_IN_CORNER:
            surface.blit(ScaleImage(image_for_right_down_in_corner, size_of_tile), position_for_blit)
        elif tile == CHAR_FOR_DOWN_OUT_CORNER:
            surface.blit(ScaleImage(image_for_right_down_out_corner, size_of_tile), position_for_blit)
        else:
            surface.blit(ScaleImage(image_for_empty, size_of_tile), position_for_blit)

    @staticmethod
    def SetTilesOnMap(surface, matrix, left_corner):
        """blit map according to the matrix and position of left corner relative to left corner of the main matrix"""

        x, y = 0, 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] in [CHAR_FOR_PATH]:
                    if (i + left_corner[0], j + left_corner[1]) in generated_floor:
                        surface.blit(generated_floor[(i + left_corner[0], j + left_corner[1])], (x, y))
                    else:
                        generated_floor[(i + left_corner[0], j + left_corner[1])] = random.choice(list_with_floor)
                        surface.blit(generated_floor[(i + left_corner[0], j + left_corner[1])], (x, y))
                else:
                    surface.blit(ScaleImage(image_for_empty), (x, y))
                y += SIZE_OF_TILE
            x += SIZE_OF_TILE
            y = 0

    @staticmethod
    def SetSpecificOnMatrix(matrix, list_of_tiles):
        """set tiles on matrix according to following list"""

        for tile in list_of_tiles:
            matrix[tile[0][0]][tile[0][1]] = tile[1]

    @staticmethod
    def BlitSpecificOnMap(surface, list_of_tiles, size_of_tile=SIZE_OF_TILE):
        """blit tiles on map according to following list"""

        for tile in list_of_tiles:
            x_coord = size_of_tile * tile[0][0]
            y_coord = size_of_tile * tile[0][1]
            if tile[1] in [CHAR_FOR_PATH, CHAR_FOR_FLOOR]:
                if tile[0] not in generated_floor:
                    generated_floor[tile[0]] = random.choice(list_with_floor)

                surface.blit(ScaleImage(generated_floor[tile[0]], size_of_tile), (x_coord, y_coord))
            else:
                Map.BlitTileOnMap(surface, (x_coord, y_coord), tile[1], size_of_tile)

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
    def Blit(surface, matrix, left_corner, size_of_tile=SIZE_OF_TILE, mini_map=False):
        x, y = 0, 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] in [CHAR_FOR_FLOOR, CHAR_FOR_PATH]:
                    if (i + left_corner[0], j + left_corner[1]) not in generated_floor:
                        generated_floor[(i + left_corner[0], j + left_corner[1])] = random.choice(list_with_floor)

                    surface.blit(
                        ScaleImage(generated_floor[(i + left_corner[0], j + left_corner[1])], size_of_tile),
                        (x, y))
                else:
                    Map.BlitTileOnMap(surface, (x, y), matrix[i][j], size_of_tile)
                y += size_of_tile
            x += size_of_tile
            y = 0

    def GetTile(self, position):
        return self.matrix_with_map[position[0] // SIZE_OF_TILE][position[1] // SIZE_OF_TILE]

    @staticmethod
    def GetPositionOfTile(position):
        return position[0] // SIZE_OF_TILE, position[1] // SIZE_OF_TILE

    def CanStandThere(self, position):
        tile = self.GetTile((position[0] - self.global_map_position[0], position[1] - self.global_map_position[1]))
        return tile in [CHAR_FOR_FLOOR, CHAR_FOR_DOOR, CHAR_FOR_PATH]

    def SetCurrentRoom(self, player_position, minimap, flag=False):
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
                    CHAR_FOR_FLOOR,
                    CHAR_FOR_DOOR]:
                    self.dfs.DFSOnTheSpecificTiles(self.matrix_with_map, self.GetPositionOfTile(player_position),
                                                   current_room,
                                                   SET_WITH_WALLS + [CHAR_FOR_DOOR,
                                                                     CHAR_FOR_FLOOR],
                                                   keys=keys, flag='room')
                    for i in current_room:
                        self.tiles_for_current_room[i] = True
                if (self.GetPositionOfTile(player_position), self.GetTile(player_position)) not in list(
                        self.visited_tiles.keys()):
                    for i in current_room:
                        self.visited_tiles[i] = True

                minimap.BlitOnMiniMap(current_room)
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

    def MoveMiniMap(self, position):
        self.mini_map_position[0] += position[0] * SIZE_OF_TILE_ON_MINI_MAP / SIZE_OF_TILE
        self.mini_map_position[1] += position[1] * SIZE_OF_TILE_ON_MINI_MAP / SIZE_OF_TILE

    def MoveMap(self, position):
        self.global_map_position[0] += position[0]
        self.global_map_position[1] += position[1]
        self.current_room_position[0] += position[0]
        self.current_room_position[1] += position[1]

    def SpawnPosition(self, minimap):
        while True:
            x = random.randrange(1, SIZE_OF_MAP[0])
            y = random.randrange(1, SIZE_OF_MAP[1])
            if self.matrix_with_map[x][y] in [CHAR_FOR_FLOOR]:
                self.global_map_position = [-x * SIZE_OF_TILE + SPAWN_POSITION[0],
                                            -y * SIZE_OF_TILE + SPAWN_POSITION[1]]
                minimap.SetStartPosition((-x, -y))
                self.mini_map_position = [-x * SIZE_OF_TILE_ON_MINI_MAP + SIZE_OF_MINI_MAP[0] // 2,
                                          -y * SIZE_OF_TILE_ON_MINI_MAP + SIZE_OF_MINI_MAP[1] // 2]
                self.SetCurrentRoom((x * SIZE_OF_TILE, y * SIZE_OF_TILE), minimap, flag=True)
                return None

