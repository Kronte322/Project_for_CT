import pygame.time

from src.back.Config import *
from src.back.Map.map_processor import MapProcessor
from src.back.Map.minimap import MiniMap
from src.back.Render import Render
from src.back.Window import Window
from src.back.in_game_eventor import Eventor
from src.back.player import Player
from src.back.processes import OnStartProcess


class Game:
    @staticmethod
    def StartGame():
        window = Window()
        OnStartProcess(window.GetDisplay())

    @staticmethod
    def StartGameSession(character):
        window = Window()
        map_processor = MapProcessor()
        mini_map = MiniMap()
        player = Player(window.GetDisplay(), character, map_processor.GetSpawnPosition(mini_map))
        render = Render(window.GetDisplay(), player, map_processor, mini_map)
        clock = pygame.time.Clock()
        RUNNING = True
        map_processor.SpawnChestInCurrentRoom()
        in_game_eventor = Eventor(player, map_processor)
        while RUNNING:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    RUNNING = False
                mini_map.ProcessEvents(event=event)
            in_game_eventor.Update()
            render.Draw()
            player.update(map_processor, render)
            map_processor.UpdateCurrentRoom(player.GetStandPosition(), mini_map)
