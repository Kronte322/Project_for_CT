import sys
from src.back import class_map
import pygame

sys.setrecursionlimit(10000000)

pygame.init()

kSizeOfDisplay = [1920, 1000]

display = pygame.display.set_mode((kSizeOfDisplay[0], kSizeOfDisplay[1]))

clock = pygame.time.Clock()

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
mappa = class_map.Map()

RUNNING = True
while RUNNING:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False

    player.move()

    display.fill((0, 155, 0))
    mappa.Render(display, player.map_pos)
    player.render(display)

    pygame.display.flip()

pygame.quit()
