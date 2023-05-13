import pygame

from src.back.Map.Objects.map_objects import *


class MouseEventProcessor:
    def __init__(self, map_processor, player, render, game):
        self.map_processor = map_processor
        self.player = player
        self.render = render
        self.game = game
        self.actions = {Exit: self.ExitAction, BasicChest: self.ChestAction}

    def ExitAction(self):
        self.game.StartGameSession(self.player.GetPersonage())

    def ChestAction(self):
        pass

    def ActionWithMapObjects(self):
        mouse_position = self.GetMousePositionOnTheMap()
        if pygame.mouse.get_pressed()[0]:
            for obj in self.map_processor.GetObjects():
                if self.map_processor.IsInCurrentRoom(mouse_position) and dist(self.player.GetCenterPosition(),
                                                                               obj.GetCenter()) <= DISTANCE_OF_ACTION:
                    if obj.IsThere(mouse_position):
                        self.actions[type(obj)]()

    def Update(self):
        self.ActionWithMapObjects()

    def GetMousePositionOnTheMap(self):
        return self.player.GetPosition()[0] - self.render.GetPlayerPositionOnTheScreen()[0] + pygame.mouse.get_pos()[0], \
               self.player.GetPosition()[1] - self.render.GetPlayerPositionOnTheScreen()[1] + pygame.mouse.get_pos()[1]
