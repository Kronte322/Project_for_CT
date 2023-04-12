import os
import sys
import pygame
from src.back import class_map
from src.back import map_generator
from src.back.constants_for_map import *
from src.back.class_minimap import MiniMap
from src.back.constants_with_paths_to_files import *
import math
from src.back.entity_2 import Enemy
# from src.back.enemy import Entity

import math
import random

import pygame


sys.setrecursionlimit(10000000)
mappa = class_map.Map()
pygame.init()

kSizeOfDisplay = WINDOW_SIZE

display = pygame.display.set_mode((kSizeOfDisplay[0], kSizeOfDisplay[1]))

clock = pygame.time.Clock()

kSizeOfCharacter = 48
kFramesPerSec = 60
kSpawnPosition = [kSizeOfDisplay[0] // 2, kSizeOfDisplay[1] // 2]
image_for_zoom = pygame.Surface((kSizeOfDisplay[0], kSizeOfDisplay[1]), flags=pygame.SRCALPHA)
image_for_zoom.fill((0, 0, 0, 0))

mini_map = MiniMap()


mappa.SpawnPosition(mini_map)


class Player:
    def __init__(self):
        self.kSpeed = 14
        # self.kSpeed = 1.3dw
        self.image = pygame.Surface(
            (kSizeOfCharacter, kSizeOfCharacter), flags=pygame.SRCALPHA)
        self.image.fill((0, 0, 0, 0))
        self.image_of_character = pygame.image.load(PATH_TO_CHARACTER)
        self.image_of_character = pygame.transform.scale(
            self.image_of_character, (kSizeOfCharacter, kSizeOfCharacter))
        self.image.blit(self.image_of_character, (0, 0))
        self.rect = pygame.Rect((kSpawnPosition[0], kSpawnPosition[1]), (kSizeOfCharacter, kSizeOfCharacter))
        # self.rect = pygame.Rect(
        #     (0, 0), (kSizeOfCharacter, kSizeOfCharacter))

        self.moveBox = (
            kSizeOfDisplay[0] // 2 - SIZE_OF_MOVE_BOX[0] // 2, kSizeOfDisplay[1] // 2 - SIZE_OF_MOVE_BOX[1] //
            2, kSizeOfDisplay[0] // 2 + SIZE_OF_MOVE_BOX[0] // 2,
            kSizeOfDisplay[1] // 2 + SIZE_OF_MOVE_BOX[1] // 2)

    def move(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_w]:
            if mappa.CanStandThere(
                    (
                            self.rect.x,
                            self.rect.y + kSizeOfCharacter - self.kSpeed - 8)):
                if mappa.CanStandThere((self.rect.x + kSizeOfCharacter,
                                        self.rect.y + kSizeOfCharacter - self.kSpeed - 8)):
                    self.rect.y -= self.kSpeed
                    mini_map.MoveMiniMap([0, self.kSpeed])
            # self.rect.y -= self.kSpeed
        if key[pygame.K_a]:
            if mappa.CanStandThere(
                    (self.rect.x - self.kSpeed, self.rect.y + kSizeOfCharacter)):
                self.rect.x -= self.kSpeed
                mini_map.MoveMiniMap([self.kSpeed, 0])

            # self.rect.x -= self.kSpeed
        if key[pygame.K_s]:
            if mappa.CanStandThere(
                    (self.rect.x, self.rect.y + kSizeOfCharacter + self.kSpeed)):
                if mappa.CanStandThere((self.rect.x + kSizeOfCharacter,
                                        self.rect.y + kSizeOfCharacter + self.kSpeed)):
                    self.rect.y += self.kSpeed
                    mini_map.MoveMiniMap([0, -self.kSpeed])

            # self.rect.y += self.kSpeed
        if key[pygame.K_d]:
            if mappa.CanStandThere(
                    (self.rect.x + kSizeOfCharacter + self.kSpeed,
                     self.rect.y + kSizeOfCharacter)):
                self.rect.x += self.kSpeed
                mini_map.MoveMiniMap([-self.kSpeed, 0])

            # self.rect.x += self.kSpeed
        if player.rect.x <= self.moveBox[0]:
            self.rect.x += self.kSpeed
            mappa.MoveMap([self.kSpeed, 0])
        elif player.rect.x >= self.moveBox[2] - 48:
            self.rect.x -= self.kSpeed
            mappa.MoveMap([-self.kSpeed, 0])
        if player.rect.y <= self.moveBox[1]:
            self.rect.y += self.kSpeed
            mappa.MoveMap([0, self.kSpeed])
        elif player.rect.y >= self.moveBox[3] - 48:
            self.rect.y -= self.kSpeed
            mappa.MoveMap([0, -self.kSpeed])

    def get_player_position(player):
        return player.rect.x, player.rect.y

    def render(self, display):
        display.blit(self.image, (self.rect.x, self.rect.y))


player = Player()
enemy = Enemy()

RUNNING = True
while RUNNING:
    clock.tick(kFramesPerSec)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
        mini_map.ProcessEvents(event=event)

    player.move()
    # enemy.move(player.get_player_position())
    display.fill((37, 19, 26))

    mappa.SetCurrentRoom([player.rect.x + kSizeOfCharacter // 2, player.rect.y + kSizeOfCharacter], mini_map)
    mappa.Render(display)

    player.render(display)
    enemy.render(display)

    mini_map.RenderMiniMap(display)

    pygame.display.flip()

pygame.quit()
