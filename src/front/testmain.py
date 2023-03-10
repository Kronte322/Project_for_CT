import os
import sys
import pygame
from src.back import class_map
from src.back import map_generator
import math

sys.setrecursionlimit(10000000)
mappa = class_map.Map()
pygame.init()

kSizeOfDisplay = [1920, 1000]

display = pygame.display.set_mode((kSizeOfDisplay[0], kSizeOfDisplay[1]))

clock = pygame.time.Clock()

kSizeOfMoveBox = [600, 300]

kSizeOfCharacter = 48
kFramesPerSec = 60
kSpawnPosition = [kSizeOfDisplay[0] // 2, kSizeOfDisplay[1] // 2]
image_for_zoom = pygame.Surface((kSizeOfDisplay[0], kSizeOfDisplay[1]), flags=pygame.SRCALPHA)
image_for_zoom.fill((0, 0, 0, 0))
image_for_zoo = pygame.image.load("../tile_sets/tiles_for_map/back_ground/sprite_01.png")
image_for_zoo = pygame.transform.scale(image_for_zoo, (kSizeOfDisplay[0], kSizeOfDisplay[1]))
image_for_zoom.blit(image_for_zoo, (0, 0))


class Player:
    def __init__(self):
        self.kSpeed = 7
        # self.kSpeed = 1.3

        self.image = pygame.Surface(
            (kSizeOfCharacter, kSizeOfCharacter), flags=pygame.SRCALPHA)
        self.image.fill((0, 0, 0, 0))
        self.image_of_character = pygame.image.load(
            "../tile_sets/tiles_for_chars/sprite_0.png")
        self.image_of_character = pygame.transform.scale(
            self.image_of_character, (kSizeOfCharacter, kSizeOfCharacter))
        self.image.blit(self.image_of_character, (0, 0))
        self.rect = pygame.Rect((kSpawnPosition[0], kSpawnPosition[1]), (kSizeOfCharacter, kSizeOfCharacter))
        # self.rect = pygame.Rect(
        #     (0, 0), (kSizeOfCharacter, kSizeOfCharacter))
        self.map_pos = mappa.SpawnPosition()
        self.moveBox = (kSizeOfDisplay[0] // 2 - kSizeOfMoveBox[0] // 2, kSizeOfDisplay[1] // 2 - kSizeOfMoveBox[1] //
                        2, kSizeOfDisplay[0] // 2 + kSizeOfMoveBox[0] // 2,
                        kSizeOfDisplay[1] // 2 + kSizeOfMoveBox[1] // 2)

    def move(self):
        mx, my = self.map_pos
        key = pygame.key.get_pressed()
        if key[pygame.K_w]:
            if mappa.CanStandThere(
                    (
                            self.rect.x - self.map_pos[0],
                            self.rect.y - self.map_pos[1] + kSizeOfCharacter - self.kSpeed - 8)):
                if mappa.CanStandThere((self.rect.x - self.map_pos[0] + kSizeOfCharacter,
                                        self.rect.y - self.map_pos[1] + kSizeOfCharacter - self.kSpeed - 8)):
                    self.rect.y -= self.kSpeed
        if key[pygame.K_a]:
            if mappa.CanStandThere(
                    (self.rect.x - self.map_pos[0] - self.kSpeed, self.rect.y - self.map_pos[1] + kSizeOfCharacter)):
                self.rect.x -= self.kSpeed
        if key[pygame.K_s]:
            if mappa.CanStandThere(
                    (self.rect.x - self.map_pos[0], self.rect.y - self.map_pos[1] + kSizeOfCharacter + self.kSpeed)):
                if mappa.CanStandThere((self.rect.x - self.map_pos[0] + kSizeOfCharacter,
                                        self.rect.y - self.map_pos[1] + kSizeOfCharacter + self.kSpeed)):
                    self.rect.y += self.kSpeed
        if key[pygame.K_d]:
            if mappa.CanStandThere(
                    (self.rect.x - self.map_pos[0] + kSizeOfCharacter + self.kSpeed,
                     self.rect.y - self.map_pos[1] + kSizeOfCharacter)):
                self.rect.x += self.kSpeed
        if player.rect.x <= self.moveBox[0]:
            self.rect.x += self.kSpeed
            mx += self.kSpeed
        elif player.rect.x >= self.moveBox[2] - 48:
            self.rect.x -= self.kSpeed
            mx -= self.kSpeed
        if player.rect.y <= self.moveBox[1]:
            self.rect.y += self.kSpeed
            my += self.kSpeed
        elif player.rect.y >= self.moveBox[3] - 48:
            self.rect.y -= self.kSpeed
            my -= self.kSpeed
        self.map_pos = (mx, my)

    def render(self, display):
        display.blit(self.image, (self.rect.x, self.rect.y))


player = Player()

RUNNING = True
while RUNNING:
    clock.tick(kFramesPerSec)
    # clock.tick()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False

    player.move()

    display.fill((37, 19, 26))
    mappa.Render(display, player.map_pos)
    if mappa.GetTile(
            (player.rect.x - player.map_pos[0] + kSizeOfCharacter // 2,
             player.rect.y - player.map_pos[1] + kSizeOfCharacter)) in [
        map_generator.kPath]:
        display.blit(image_for_zoom, (0, 0))
    player.render(display)

    pygame.display.flip()

pygame.quit()
