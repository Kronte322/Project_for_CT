import pygame
from src.back import map_generator

kSizeOfTile = 48
kSizeOfMap = (128, 128)

image_for_wall = pygame.image.load(
    "../tile_sets/tiles_for_map/up_walls/sprite_001.png")
default_image_size_for_wall = (kSizeOfTile, kSizeOfTile)
image_for_wall = pygame.transform.scale(
    image_for_wall, default_image_size_for_wall)
image_rect_for_wall = image_for_wall.get_rect()

image_for_floor = pygame.image.load(
    "../tile_sets/tiles_for_map/floor/sprite_007.png")
default_image_size_for_floor = (kSizeOfTile, kSizeOfTile)
image_for_floor = pygame.transform.scale(
    image_for_floor, default_image_size_for_wall)
image_rect_for_floor = image_for_floor.get_rect()

image_for_door = pygame.image.load(
    "../tile_sets/tiles_for_map/doors/sprite_066.png")
default_image_size_for_door = (kSizeOfTile, kSizeOfTile)
image_for_door = pygame.transform.scale(
    image_for_door, default_image_size_for_wall)
image_rect_for_door = image_for_door.get_rect()


class Map:
    def __init__(self):
        self.map_generator = map_generator.MapGenerator()
        self.matrix_with_map = self.map_generator.GenerateMap(kSizeOfMap)
        self.mappa = pygame.Surface((kSizeOfMap[0] * kSizeOfTile, kSizeOfMap[1] * kSizeOfTile))
        x, y = 0, 0
        for i in range(len(self.matrix_with_map)):
            for tile in self.matrix_with_map[i]:
                if tile in [map_generator.kFloor, map_generator.kPath]:
                    image_rect_for_floor[0] = x
                    image_rect_for_floor[1] = y
                    self.mappa.blit(image_for_floor, image_rect_for_floor)
                elif tile in [map_generator.kWall]:
                    image_rect_for_wall[0] = x
                    image_rect_for_wall[1] = y
                    self.mappa.blit(image_for_wall, image_rect_for_wall)
                elif tile == map_generator.kOneWidthPath:
                    pygame.draw.rect(self.matrix_with_map, (196, 29, 29),
                                     ((x, y), (kSizeOfTile, kSizeOfTile)))
                elif tile == map_generator.kSign:
                    pygame.draw.rect(self.matrix_with_map, (255, 0, 0),
                                     ((x, y), (kSizeOfTile, kSizeOfTile)))
                elif tile == map_generator.kDoor:
                    image_rect_for_door[0] = x
                    image_rect_for_door[1] = y
                    self.mappa.blit(image_for_door, image_rect_for_door)
                # elif tile == mapgen.kPath:
                #   pygame.draw.rect(mappa, (255, 0, 0),
                #                    ((x, y), (kSizeOfTile, kSizeOfTile)))
                else:
                    pygame.draw.rect(self.mappa, (0, 0, 0), ((x, y), (kSizeOfTile, kSizeOfTile)))
                y += kSizeOfTile
            x += kSizeOfTile
            y = 0

    def GetTile(self, position):
        return self.matrix_with_map[position[0] // 48][position[1] // 48]

    def CanStandThere(self, position):
        tile = self.GetTile(position)
        return tile in [map_generator.kFloor]

    def Render(self, display, position):
        display.blit(self.mappa, position)
