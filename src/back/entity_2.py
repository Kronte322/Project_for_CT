import pygame
# import constants_for_map
from random import randint
import os
import sys
import pygame
from src.back import class_map
from src.back import map_generator
from src.back.constants_for_map import *
from src.back.class_minimap import MiniMap
from src.back.constants_with_paths_to_files import *
import math
from src.back.utils import get_mask_rect



kSize_of_enemy = 48
WINDOW_SIZE = [1920, 1000]
kSize_of_display = WINDOW_SIZE
kSpawnPosition = [kSize_of_display[0] // 2, kSize_of_display[1] // 2]


class Enemy:
    def __init__(self):
        self.speed = 10
        self.image = pygame.Surface((kSize_of_enemy, kSize_of_enemy), flags=pygame.SRCALPHA)
        self.image.fill((0, 0, 0, 0))
        self.image_of_character = pygame.image.load(PATH_TO_ENEMY)
        self.image_of_character = pygame.transform.scale(self.image_of_character, (kSize_of_enemy, kSize_of_enemy))
        self.image.blit(self.image_of_character, (0, 0))
        # self.rect = pygame.Rect((kSpawnPosition[0], kSpawnPosition[1]), (kSize_of_enemy, kSize_of_enemy))
        self.x, self.y = 0, 0
        self.dead = False  # жив или не
        self.cx, self.cy = 0, 0  # где противник появляется
        self.health = 3  # колво жизней
        self.hurt_distance = 72  # расстояние где проиивник модет стрелять
        self.velocity = [0,0]
        self.rect = self.image.get_rect()
        self.hitbox = self.hitbox = get_mask_rect(self.image, *self.rect.topleft)





    def die(self): #для удаления врага
        if not self.dead:
            self.dead = True
    def set_velocity(self, new_velocity):
        self.velocity = new_velocity

    def hurt(self, live): #метод нанесения урона
        if not self.dead:
            self.health -= live
            if self.health <= 0:
                self.die()

    def move(self, player_pos):
        return self.velocity[0] != 0 or self.velocity[1] != 0


    def render(self, display):
        display.blit(self.image, (self.rect.x, self.rect.y))

#
#
#
#
#
#
#
#
#
#
#
#
#
