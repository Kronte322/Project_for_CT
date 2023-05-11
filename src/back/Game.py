import pygame.time

from src.back.Config import *
from src.back.Render import Render
from src.back.Window import Window
from src.back.class_map import MapProcessor
from src.back.class_minimap import MiniMap
from src.back.player import Player


class Game:
    @staticmethod
    def StartGameSession(character):
        window = Window()
        map_processor = MapProcessor()
        mini_map = MiniMap()
        player = Player(window.GetDisplay(), character, map_processor.GetSpawnPosition(mini_map))
        render = Render(window.GetDisplay(), player, map_processor)
        clock = pygame.time.Clock()

        while True:
            clock.tick(FPS)
            render.Draw()
