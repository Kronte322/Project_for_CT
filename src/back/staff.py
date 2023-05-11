import pygame
from src.back.projectile import Projectile
import time

list_of_coord = ((0, 0), (1, 1), (2, 2), (3, 3), (5, 4), (7, 4), (9, 4), (11, 4),
                 (12, 4), (14, 4), (16, 4), (18, 4), (20, 3), (21, 2), (22, 1), (23, 0))

kSizeOfStaff = (32, 48)


class Staff:
    def __init__(self, path_to_staff, players_rect, display):
        self.path_to_staff = path_to_staff
        self.staff_y = 0
        self.staff_delta = 1
        self.diff_with_players_x = (28, -12)
        self.diff_with_players_x_num = 1

        self.image_of_staff = pygame.image.load(self.path_to_staff).convert_alpha()
        self.image_of_staff = pygame.transform.scale(
            self.image_of_staff, kSizeOfStaff)
        display.blit(self.image_of_staff,
                     (players_rect[0] + self.diff_with_players_x[self.diff_with_players_x_num],
                      players_rect[1] + self.staff_y))

        self.num_of_minerals = 3
        self.coord_y_of_minerals = (6, 14, 26)
        self.list_of_mineral_num = [0, 10, 5]
        self.mineral_delta = [1, 1, 1]
        self.path_to_minerals = []
        self.image_of_mineral = []

        for i in range(self.num_of_minerals):
            self.path_to_minerals.append("src/tile_sets/tiles_for_chars/magic_crystals/red_crystal.png")
            self.image_of_mineral.append(pygame.image.load(self.path_to_minerals[i]).convert_alpha())
            self.image_of_mineral[i] = pygame.transform.scale(
                self.image_of_mineral[i], (8, 8))
            display.blit(self.image_of_mineral[i], (
                players_rect[0] + self.diff_with_players_x[self.diff_with_players_x_num],
                players_rect[1] + self.staff_y + self.coord_y_of_minerals[i]))

    def blit_mineral(self, display, players_rect, diff_with_players_x_num, i):
        display.blit(self.image_of_mineral[i],
                     (players_rect[0] + self.diff_with_players_x[diff_with_players_x_num] +
                      list_of_coord[self.list_of_mineral_num[i] // 3][0],
                      players_rect[1] + self.staff_y + self.coord_y_of_minerals[i] + list_of_coord[self.list_of_mineral_num[i] // 3][
                          1]))

    def render(self, display, players_rect):
        for i in range(self.num_of_minerals):
            if self.mineral_delta[i] == -1:
                self.blit_mineral(display, players_rect, self.diff_with_players_x_num, i)

        display.blit(self.image_of_staff, (players_rect[0] + self.diff_with_players_x[self.diff_with_players_x_num],
                                           players_rect[1] + self.staff_y // 2))
        if abs(self.staff_y) >= 20:
            self.staff_delta *= -1
        self.staff_y += self.staff_delta
        for i in range(self.num_of_minerals):
            if self.mineral_delta[i] == 1:
                self.blit_mineral(display, players_rect, self.diff_with_players_x_num, i)

            self.list_of_mineral_num[i] += (self.mineral_delta[i] * (-1 if i == 1 else 1))
            if self.list_of_mineral_num[i] == 45 or self.list_of_mineral_num[i] == 0:
                self.mineral_delta[i] *= -1

    def change_mineral(self, num_of_mineral, path_to_mineral):
        self.path_to_minerals[num_of_mineral] = path_to_mineral
        self.image_of_mineral[num_of_mineral] = pygame.image.load(self.path_to_minerals[num_of_mineral]).convert_alpha()
        self.image_of_mineral[num_of_mineral] = pygame.transform.scale(
            self.image_of_mineral[num_of_mineral], (8, 8))
