import pygame.time

import src.back.Config
from src.back.Map.map_processor import MapProcessor
from src.back.Map.minimap import MiniMap
from src.back.Render import Render
from src.back.Window import Window
from src.back.in_game_eventor import Eventor
from src.back.player import Player
from src.back.processes import OnStartProcess
from src.back.input_processor import *
from src.back.enemy_processor import *
from src.back.inventory import Inventory
from src.back.controller import Controller


class Game:
    def __init__(self):
        self.window = Window()

    def StartGame(self):
        OnStartProcess(self.window.GetDisplay(), self)

    def StartGameSession(self, character):
        map_processor = MapProcessor()
        mini_map = MiniMap()
        player = Player(self.window.GetDisplay(), character, map_processor.GetSpawnPosition(mini_map))
        enemy_processor = EnemyProcessor(map_processor, player)
        inventory = Inventory(player.staff.crystals)
        controller = Controller(player, inventory)
        render = Render(self.window.GetDisplay(), player, map_processor, mini_map, enemy_processor, inventory)
        clock = pygame.time.Clock()
        map_processor.SpawnChestInCurrentRoom()
        in_game_eventor = Eventor(player, map_processor, mini_map, enemy_processor)
        mouse_processor = MouseEventProcessor(map_processor, player, render, self)
        while src.back.Config.RUNNING:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    src.back.Config.RUNNING = False
                mini_map.ProcessEvents(event=event)
            mouse_processor.Update()
            enemy_processor.Update(map_processor, player, render.GetPlayerPositionOnTheScreen())
            in_game_eventor.Update()
            controller.update(render.GetPlayerPositionOnTheScreen())
            controller.test_delete_enemies(enemy_processor.GetEnemies())
            player.update(map_processor, render, enemy_processor.GetEnemies())
            src.back.Config.RUNNING = player.is_alive() and src.back.Config.RUNNING
            map_processor.UpdateCurrentRoom(player.GetStandPosition(), mini_map)
            render.Draw()
