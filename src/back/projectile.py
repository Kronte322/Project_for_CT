import pygame
from math import sqrt, pi, sin

kSizeOfCharacter = 48
kSizeOfProjectile = 32

fireball_path = "../tile_sets/tiles_for_chars/ranged_attack/fireball_animation/sprite_"
flash_path = "../tile_sets/tiles_for_chars/ranged_attack/flash_animation/flash_"


class Projectile:
    def __init__(self, players_damage, players_pos: tuple, aim_pos: tuple, len_from_player, num_of_mineral,
                 sinnum, proj_path=fireball_path):
        self.image_path = proj_path + "4.png"
        self.path = proj_path
        # players_pos = (players_pos[0] + kSizeOfCharacter // 2, players_pos[1] + kSizeOfCharacter // 2)
        self.speed = 8
        # self.accel = 0
        self.damage = players_damage
        self.direction = (
            (aim_pos[0] - players_pos[0]) / sqrt(
                (players_pos[0] - aim_pos[0]) ** 2 + (players_pos[1] - aim_pos[1]) ** 2),
            (aim_pos[1] - players_pos[1]) / sqrt(
                (players_pos[0] - aim_pos[0]) ** 2 + (players_pos[1] - aim_pos[1]) ** 2))
        self.cur_dist = 0
        self.dist = 6000  # это просто рандомная чиселка пока что
        # self.image = pygame.Surface(
        #     (kSizeOfProjectile, kSizeOfProjectile), flags=pygame.SRCALPHA)
        # self.image.fill((0, 0, 0, 0))
        self.image_of_projectile = pygame.image.load(self.image_path).convert_alpha()
        self.image_of_projectile = pygame.transform.scale(
            self.image_of_projectile, (kSizeOfProjectile, kSizeOfProjectile))
        # self.image.blit(self.image_of_character, (0, 0))
        self.rect = self.image_of_projectile.get_rect(
            topleft=(players_pos[0] + self.direction[0] * 30 + (kSizeOfCharacter - kSizeOfProjectile) // 2,
                     players_pos[1] + self.direction[1] * 30 + (kSizeOfCharacter - kSizeOfProjectile) // 2))
        self.image_num = 0
        self.image_num_move = 0
        self.len = len_from_player if len_from_player <= self.dist else self.dist

        self.num_of_mineral = num_of_mineral
        self.sin_num = sinnum

    def render(self, display, mappa, rivals=None):
        is_touch_with_rival = False

        if rivals is None or rivals == []:
            rivals = []
        else:
            for rival in rivals:
                if self.rect.colliderect(rival.rect):
                    is_touch_with_rival = True
                    # тут будет вызываться команда от rival, которая нанесет ему урон (дебафф)

        if is_touch_with_rival or self.dist - self.cur_dist < 0 or not mappa.CanStandThere(
                (round(self.rect.x) + kSizeOfProjectile // 2,
                 round(self.rect.y) + kSizeOfProjectile)):
            if self.image_num // 2 >= 11:
                # self.image_num = 0
                # self.image_path = self.path + "6.png"
                # self.image_of_projectile = pygame.image.load(self.image_path).convert_alpha()
                # self.image_of_projectile = pygame.transform.scale(
                #     self.image_of_projectile, (kSizeOfProjectile, kSizeOfProjectile))
                # self.image_num_move = 8
                return True
            image_path_fire = self.path + str(
                self.image_num // 2) + ".png"
            image = pygame.image.load(image_path_fire).convert_alpha()
            image = pygame.transform.scale(
                image, (kSizeOfCharacter, kSizeOfCharacter))
            display.blit(image, self.rect)
            self.image_num += 1
        else:
            display.blit(self.image_of_projectile, self.rect)
            self.rect.x += self.direction[0] * self.speed
            self.rect.y += self.direction[1] * self.speed
            if self.num_of_mineral != 0:
                delta = self.len / pi * (
                        sin(((self.cur_dist + self.speed) % (2 * self.len)) * pi / self.len) - sin(
                    (self.cur_dist % (2 * self.len)) * pi / self.len))
                self.rect.x -= self.direction[1] * delta * (-1 if self.sin_num == 0 else 1)
                self.rect.y += self.direction[0] * delta * (-1 if self.sin_num == 0 else 1)
            self.cur_dist += self.speed
            self.image_path = self.path + str(
                self.image_num_move // 2 + 4) + ".png"
            self.image_of_projectile = pygame.image.load(self.image_path).convert_alpha()
            self.image_of_projectile = pygame.transform.scale(
                self.image_of_projectile, (kSizeOfProjectile, kSizeOfProjectile))
            self.image_num_move += 1
            self.image_num_move %= 6

        return False
