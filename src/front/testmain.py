import sys
# sys.path.insert(1, '/Project_for_CT/src/back')
import src.back.map_generator as mapgen
import pygame
import random
import importlib
import time

# import Project_for_CT.
sys.setrecursionlimit(10000000)

random.seed(time.time())
# random.seed(10)

map_generator = mapgen.MapGenerator((128, 128))

scene = map_generator.GetMap()

pygame.init()

kSizeOfMap = [22, 12]

kSizeOfTile = 12

kSizeOfDisplay = [1920, 1000]

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

display = pygame.display.set_mode((kSizeOfDisplay[0], kSizeOfDisplay[1]))

clock = pygame.time.Clock()

mappa = pygame.Surface((len(scene) * kSizeOfTile, len(scene[0]) * kSizeOfTile))
x, y = 0, 0
for i in range(len(scene)):
    for tile in scene[i]:
        if tile in [mapgen.kFloor, mapgen.kPath]:
            image_rect_for_floor[0] = x
            image_rect_for_floor[1] = y
            mappa.blit(image_for_floor, image_rect_for_floor)
        elif tile in [mapgen.kWall]:
            image_rect_for_wall[0] = x
            image_rect_for_wall[1] = y
            mappa.blit(image_for_wall, image_rect_for_wall)
        elif tile == mapgen.kOneWidthPath:
            pygame.draw.rect(mappa, (196, 29, 29),
                             ((x, y), (kSizeOfTile, kSizeOfTile)))
        elif tile == mapgen.kSign:
            pygame.draw.rect(mappa, (255, 0, 0),
                             ((x, y), (kSizeOfTile, kSizeOfTile)))
        elif tile == mapgen.kDoor:
            image_rect_for_door[0] = x
            image_rect_for_door[1] = y
            mappa.blit(image_for_door, image_rect_for_door)
        # elif tile == mapgen.kPath:
        #   pygame.draw.rect(mappa, (255, 0, 0),
        #                    ((x, y), (kSizeOfTile, kSizeOfTile)))
        else:
            pygame.draw.rect(mappa, (0, 0, 0), ((x, y), (kSizeOfTile, kSizeOfTile)))
        y += kSizeOfTile
    x += kSizeOfTile
    y = 0

kSizeOfMoveBox = [600, 300]


class Player:
    def __init__(self):
        self.image = pygame.Surface((32, 32), flags=pygame.SRCALPHA)
        self.image.fill((0, 0, 0, 0))
        self.image_of_character = pygame.image.load(
            "../tile_sets/tiles_for_chars/sprite_10.png")
        self.image_of_character = pygame.transform.scale(
            self.image_of_character, (32, 32))
        self.image.blit(self.image_of_character, (0, 0))
        self.rect = pygame.Rect(
            (kSizeOfDisplay[0] // 2, kSizeOfDisplay[1] // 2), (32, 32))
        self.map_pos = (0, 0)
        self.moveBox = (kSizeOfDisplay[0] // 2 - kSizeOfMoveBox[0] // 2, kSizeOfDisplay[1] // 2 - kSizeOfMoveBox[1] //
                        2, kSizeOfDisplay[0] // 2 + kSizeOfMoveBox[0] // 2,
                        kSizeOfDisplay[1] // 2 + kSizeOfMoveBox[1] // 2)

    def move(self):
        mx, my = self.map_pos
        key = pygame.key.get_pressed()
        if key[pygame.K_w]:
            self.rect.y -= 8
        if key[pygame.K_a]:
            self.rect.x -= 8
        if key[pygame.K_s]:
            self.rect.y += 8
        if key[pygame.K_d]:
            self.rect.x += 8
        if player.rect.x <= self.moveBox[0]:
            self.rect.x += 8
            mx += 8
        elif player.rect.x >= self.moveBox[2] - 32:
            self.rect.x -= 8
            mx -= 8
        if player.rect.y <= self.moveBox[1]:
            self.rect.y += 8
            my += 8
        elif player.rect.y >= self.moveBox[3] - 32:
            self.rect.y -= 8
            my -= 8
        self.map_pos = (mx, my)

    def render(self, display):
        display.blit(self.image, (self.rect.x, self.rect.y))


player = Player()

RUNNING = True
while RUNNING:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False

    player.move()

    display.fill((0, 155, 0))
    display.blit(mappa, player.map_pos)
    player.render(display)

    pygame.display.flip()

pygame.quit()
