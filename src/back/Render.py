import pygame

from src.back.Map.Objects.map_objects import *
from src.back.constants_with_paths_to_files import *


class Render:
    def __init__(self, display, player, enemy, map_processor, mini_map):
        self.display = display
        self.player = player
        self.enemy = enemy
        self.mini_map = mini_map
        self.map_processor = map_processor
        self.position_of_player_on_the_screen = POSITION_OF_PLAYER_ON_SCREEN
        self.position_of_enemy_on_the_screen = POSITION_OF_ENEMY_ON_SCREEN
        self.moveBox = (WINDOW_SIZE[0] // 2 - SIZE_OF_MOVE_BOX[0] // 2, WINDOW_SIZE[1] // 2 - SIZE_OF_MOVE_BOX[1] // 2,
                        WINDOW_SIZE[0] // 2 + SIZE_OF_MOVE_BOX[0] // 2, WINDOW_SIZE[1] // 2 + SIZE_OF_MOVE_BOX[1] // 2)
        self.images = {}
        self.SetImages()

    def GetPlayerPositionOnTheScreen(self):
        return self.position_of_player_on_the_screen

    def SetImage(self, tp, path, size):
        image = pygame.image.load(path)
        image = pygame.transform.scale(image, (size, size))
        self.images[tp] = image

    def SetImages(self):
        self.SetImage(BasicChest, PATH_TO_BASIC_CHEST, SIZE_OF_BASIC_CHEST)
        self.SetImage(Exit, PATH_TO_EXIT, SIZE_OF_TILE)

    def ChangePositionOfPlayerAccordingToMoveBox(self, vector):
        self.mini_map.MoveMiniMap((-vector[0], -vector[1]))
        if self.moveBox[0] <= self.position_of_player_on_the_screen[0] + vector[0] <= self.moveBox[2] - 48:
            self.position_of_player_on_the_screen[0] += vector[0]  # mappa.MoveMap([-self.direction[0], 0])

        if self.moveBox[1] <= self.position_of_player_on_the_screen[1] + vector[1] <= self.moveBox[3] - 48:
            self.position_of_player_on_the_screen[1] += vector[1]  # mappa.MoveMap([0, -self.direction[1]])
        pass

    def DrawPlayer(self):
        self.player.render(self.display, self.position_of_player_on_the_screen)

    def DrawMapObjects(self):
        for obj in self.map_processor.GetObjects():
            if self.map_processor.IsInCurrentRoom(obj.GetPosition()):
                position_to_blit = (
                    obj.GetPosition()[0] - self.player.GetPosition()[0] + self.position_of_player_on_the_screen[0],
                    obj.GetPosition()[1] - self.player.GetPosition()[1] + self.position_of_player_on_the_screen[1])
                self.display.blit(self.images[type(obj)], position_to_blit)

    def DrawMiniMap(self):
        self.mini_map.RenderMiniMap(self.display)

    def DrawMap(self):
        position_to_blit = (self.map_processor.GetCurrentRoom().GetPosition()[0] - self.player.GetPosition()[0] +
                            self.position_of_player_on_the_screen[0],
                            self.map_processor.GetCurrentRoom().GetPosition()[1] - self.player.GetPosition()[1] +
                            self.position_of_player_on_the_screen[1])
        self.display.blit(self.map_processor.GetCurrentRoom().GetSurface(), position_to_blit)

    def Draw(self):
        self.display.fill((37, 19, 26))
        self.DrawMap()
        self.DrawMapObjects()
        self.DrawPlayer()
        self.DrawMiniMap()
        pygame.display.flip()
