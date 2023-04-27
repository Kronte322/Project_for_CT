import pygame
from src.back.constants_for_map import WINDOW_SIZE, SIZE_OF_MOVE_BOX
from src.back.constants_with_paths_to_files import PATH_TO_CHARACTER
from src.back.projectile import Projectile
from src.back.staff import Staff
from src.back.animation import Animation
from src.back.personages import Personage, personages
import time
from math import sqrt

kSizeOfDisplay = WINDOW_SIZE

kSizeOfCharacter = 48
kSpawnPosition = [kSizeOfDisplay[0] // 2, kSizeOfDisplay[1] // 2]

kOneHeartInHP = 200
kSizeOfHeart = 24
path_to_heart = "../tile_sets/tiles_for_chars/hearts/heart_"
path_to_skeleton = "../tile_sets/tiles_for_chars/personages/skeleton/skeleton_"


def norm(vector):
    return sqrt(vector[0] ** 2 + vector[1] ** 2)


def normalized(vector):
    if norm(vector) != 0:
        vector[0] /= norm(vector)
        vector[1] /= norm(vector)
    return vector


class Player:
    def __init__(self, display, personage: Personage, spawnposition):
        self.personage = personage
        self.image_stat = Animation(self.personage.path_stat, self.personage.num_stat,
                                    (kSizeOfCharacter, kSizeOfCharacter), self.personage.frequency)
        self.image_down = Animation(self.personage.path_down, self.personage.num_down,
                                    (kSizeOfCharacter, kSizeOfCharacter), self.personage.frequency)
        self.image_up = Animation(self.personage.path_up, self.personage.num_up,
                                  (kSizeOfCharacter, kSizeOfCharacter), self.personage.frequency)
        self.image_right = Animation(self.personage.path_right, self.personage.num_right,
                                     (kSizeOfCharacter, kSizeOfCharacter), self.personage.frequency)
        self.image_left = Animation(self.personage.path_left, self.personage.num_left,
                                    (kSizeOfCharacter, kSizeOfCharacter), self.personage.frequency)

        self.image_of_character = self.image_stat.get_image()

        self.moveBox = (
            kSizeOfDisplay[0] // 2 - SIZE_OF_MOVE_BOX[0] // 2, kSizeOfDisplay[1] // 2 - SIZE_OF_MOVE_BOX[1] //
            2, kSizeOfDisplay[0] // 2 + SIZE_OF_MOVE_BOX[0] // 2,
            kSizeOfDisplay[1] // 2 + SIZE_OF_MOVE_BOX[1] // 2)

        self.rect = self.image_of_character.get_rect(topleft=spawnposition)
        display.blit(self.image_of_character, self.rect)

        self.max_speed = 8
        # self.acceleration = 2  # ускорение
        self.direction = [0, 0]  # направление

        self.melee_attack_damage = 2  # урон ближней атакой
        self.ranged_attack_damage = 0  # урон дальней атакой
        self.max_health = 1000
        self.health_points = self.max_health
        self.health_recovery = 0.2
        self.max_magic = 10000
        self.magic_points = self.max_magic
        self.magic_recovery = 0.05

        self.slash_num = 0
        self.last_fire_slash = 0
        self.right_mouse_down = False
        self.right_mouse_up = False

        self.fires = []  # список еще не долетевших до цели выстрелов
        self.last_fire_time = 0  # чтобы сделать ограничение на кол-во выстрелов по времени
        self.left_mouse_down = False  # это либо будет полем игрока, либо глобальгной переменной
        self.left_mouse_up = False  # это либо будет полем игрока, либо глобальгной переменной

        self.staff = Staff("../tile_sets/tiles_for_chars/staff/staff.png", self.rect, display)
        self.sin_num = 0

        self.path_to_icon = self.personage.path_icon
        self.image_of_icon = pygame.image.load(self.path_to_icon).convert_alpha()
        self.image_of_icon = pygame.transform.scale(
            self.image_of_icon, (kSizeOfCharacter, kSizeOfCharacter))

    def GetImage(self):
        return self.image_of_character

    def GetPosition(self):
        return tuple(self.rect.x, self.rect.y)

    def GetSize(self):
        return self.rect.size

    def move(self, mappa, mini_map):
        self.direction = [0, 0]

        key = pygame.key.get_pressed()

        if key[pygame.K_w]:
            self.direction[1] -= 1
            self.staff.diff_with_players_x_num = 0

        if key[pygame.K_a]:
            self.direction[0] -= 1
            self.staff.diff_with_players_x_num = 0

        if key[pygame.K_s]:
            self.direction[1] += 1
            self.staff.diff_with_players_x_num = 1

        if key[pygame.K_d]:
            self.direction[0] += 1
            self.staff.diff_with_players_x_num = 1

        if self.direction != [0, 0]:
            self.direction = normalized(self.direction)
            self.direction[0] *= self.max_speed
            self.direction[1] *= self.max_speed
        else:
            self.staff.diff_with_players_x_num = 1

        self.direction[0] = round(self.direction[0])
        self.direction[1] = round(self.direction[1])

        if self.direction[0] < 0 and not mappa.CanStandThere(
                (self.rect.x + self.direction[0], self.rect.y + kSizeOfCharacter)):
            self.direction[0] = 0

        elif self.direction[0] > 0 and not mappa.CanStandThere(
                (self.rect.x + kSizeOfCharacter + self.direction[0], self.rect.y + kSizeOfCharacter)):
            self.direction[0] = 0

        if self.direction[1] < 0:
            if not mappa.CanStandThere(
                    (self.rect.x, self.rect.y + kSizeOfCharacter - 8 + self.direction[1])) or not mappa.CanStandThere(
                (self.rect.x + kSizeOfCharacter,
                 self.rect.y + kSizeOfCharacter - 8 + self.direction[1])):
                self.direction[1] = 0
        elif self.direction[1] > 0:
            if not mappa.CanStandThere(
                    (self.rect.x, self.rect.y + kSizeOfCharacter + self.direction[1])) or not mappa.CanStandThere(
                (self.rect.x + kSizeOfCharacter,
                 self.rect.y + kSizeOfCharacter + self.direction[1])):
                self.direction[1] = 0

        self.rect.x += self.direction[0]
        self.rect.y += self.direction[1]
        mini_map.MoveMiniMap([-self.direction[0], -self.direction[1]])

        if self.rect.x <= self.moveBox[0] or self.rect.x >= self.moveBox[2] - kSizeOfCharacter:
            self.rect.x -= self.direction[0]
            if self.fires:
                for fire in self.fires:
                    fire.rect.x -= self.direction[0]
            mappa.MoveMap([-self.direction[0], 0])

        if self.rect.y <= self.moveBox[1] or self.rect.y >= self.moveBox[3] - kSizeOfCharacter:
            self.rect.y -= self.direction[1]
            if self.fires:
                for fire in self.fires:
                    fire.rect.y -= self.direction[1]
            mappa.MoveMap([0, -self.direction[1]])

        if self.direction == [0, 0]:
            self.image_of_character = self.image_stat.get_image()

        elif self.direction[0] > 0:
            self.image_of_character = self.image_right.get_image()

        elif self.direction[0] < 0:
            self.image_of_character = self.image_left.get_image()

        elif self.direction[1] > 0:
            self.image_of_character = self.image_down.get_image()

        elif self.direction[1] < 0:
            self.image_of_character = self.image_up.get_image()

    def ranged_attack(self, display, mappa):
        self.left_mouse_up = not pygame.mouse.get_pressed()[0]
        if self.left_mouse_up and self.left_mouse_down and self.magic_points >= 5:  # and (time.time()-self.last_fire_time) > 0.3
            mouse = pygame.mouse.get_pos()
            len_from_player = sqrt((self.rect[0] - mouse[0]) ** 2 + (self.rect[1] - mouse[1]) ** 2)
            for i in range(self.staff.num_of_minerals):
                self.fires.append(Projectile(self.ranged_attack_damage,
                                             (self.rect.x, self.rect.y), mouse, len_from_player, i, self.sin_num))
                if i != 0:
                    self.sin_num += 1
                    self.sin_num %= 2

            self.last_fire_time = time.time()
            self.left_mouse_up = False
            # self.left_mouse_down = False
            self.magic_points -= 5

        self.left_mouse_down = pygame.mouse.get_pressed()[0]

        if self.fires:
            for (i, fire) in enumerate(self.fires):
                if fire.render(display, mappa):
                    self.fires.pop(i)

    def melee_attack(self, display, rivals=None):  # display, mappa
        self.right_mouse_up = not pygame.mouse.get_pressed()[2]

        if self.slash_num == 0 and self.right_mouse_up and self.right_mouse_down and \
                (time.time() - self.last_fire_slash) > 0.3:
            self.right_mouse_up = False
            # self.right_mouse_down = False
            self.last_fire_slash = time.time()

            slash_path = "../tile_sets/tiles_for_chars/slash/slash_0.png"
            image_of_slash = pygame.image.load(slash_path).convert_alpha()
            image_of_slash = pygame.transform.scale(
                image_of_slash, (1.5 * kSizeOfCharacter, 1.5 * kSizeOfCharacter))
            slash_rect = image_of_slash.get_rect(
                topleft=(self.rect[0] - kSizeOfCharacter // 4, self.rect[1] - kSizeOfCharacter // 4))
            display.blit(image_of_slash, slash_rect)
            self.slash_num += 1

            if rivals is None or not rivals:
                return
            else:
                for rival in rivals:
                    if slash_rect.colliderect(rival.rect):
                        # тут будет передаваться урон мобу
                        pass

        elif self.slash_num > 0:
            slash_path = "../tile_sets/tiles_for_chars/slash/slash_" + str(self.slash_num) + ".png"
            image_of_slash = pygame.image.load(slash_path).convert_alpha()
            image_of_slash = pygame.transform.scale(
                image_of_slash, (1.5 * kSizeOfCharacter, 1.5 * kSizeOfCharacter))
            display.blit(image_of_slash, (self.rect[0] - kSizeOfCharacter // 4, self.rect[1] - kSizeOfCharacter // 4))
            self.slash_num += 1
            self.slash_num %= 15

        self.right_mouse_down = pygame.mouse.get_pressed()[2]

    def health_icon(self, display):
        full_hearts = self.health_points // kOneHeartInHP
        is_mode_null = self.health_points % kOneHeartInHP == 0
        num_of_not_full_heart = 4 - ((self.health_points % kOneHeartInHP) * 5 // kOneHeartInHP)
        empty_hearts = self.max_health // kOneHeartInHP - full_hearts

        x = 100
        y = 15

        for i in range(full_hearts):
            image_path = path_to_heart + "0" + ".png"
            image_of_heart = pygame.image.load(image_path).convert_alpha()
            image_of_heart = pygame.transform.scale(
                image_of_heart, (kSizeOfHeart, kSizeOfHeart))
            display.blit(image_of_heart, (x, y))
            x += kSizeOfHeart * 5 // 4
        if not is_mode_null:
            image_path = path_to_heart + str(num_of_not_full_heart) + ".png"
            image_of_heart = pygame.image.load(image_path).convert_alpha()
            image_of_heart = pygame.transform.scale(
                image_of_heart, (kSizeOfHeart, kSizeOfHeart))
            display.blit(image_of_heart, (x, y))
            x += kSizeOfHeart * 5 // 4
            empty_hearts -= 1
        if empty_hearts != 0:
            for i in range(empty_hearts):
                image_path = path_to_heart + "4" + ".png"
                image_of_heart = pygame.image.load(image_path).convert_alpha()
                image_of_heart = pygame.transform.scale(
                    image_of_heart, (kSizeOfHeart, kSizeOfHeart))
                display.blit(image_of_heart, (x, y))
                x += kSizeOfHeart * 5 // 4

    @staticmethod
    def personage_icon(self, display):
        display.blit(self.image_of_icon, (26, 10))

    def mp_icon(self, display):
        path_to_mp_icon = "../tile_sets/tiles_for_chars/MP_icon.png"
        width = round(self.magic_points / self.max_magic * 215)
        pygame.draw.rect(display, (20, 160, 255), (93, 47, width, 20))
        image_of_mp_icon = pygame.image.load(path_to_mp_icon).convert_alpha()
        image_of_mp_icon = pygame.transform.scale(
            image_of_mp_icon, (240, 24))
        display.blit(image_of_mp_icon, (80, 45))

    def render(self, display, mappa):
        display.blit(self.image_of_character, self.rect)
        self.staff.render(display, self.rect)
        self.ranged_attack(display, mappa)
        self.melee_attack(display)
        self.health_icon(display)
        self.personage_icon(self, display)
        self.mp_icon(display)
        if self.magic_points <= self.max_magic - self.magic_recovery:
            self.magic_points += self.magic_recovery
        if self.health_points <= self.max_health - self.health_recovery:
            self.health_points += self.health_recovery
