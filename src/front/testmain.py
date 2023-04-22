import os
import sys
import pygame
from src.back import class_map
from src.back import map_generator
from src.back.constants_for_map import *
from src.back.class_minimap import MiniMap
from src.back.constants_with_paths_to_files import *
import math
from src.back.projectile import Projectile
import time
from src.back.player import Player
from src.back.personages import Personage, personages


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

player = Player(display, personages[4])

RUNNING = True
while RUNNING:
    clock.tick(kFramesPerSec)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
        mini_map.ProcessEvents(event=event)

    player.move(mappa, mini_map)

    display.fill((37, 19, 26))

    mappa.SetCurrentRoom([player.rect.x + kSizeOfCharacter // 2, player.rect.y + kSizeOfCharacter], mini_map)
    mappa.Render(display)

    player.render(display, mappa)
    # player.fire(display, mappa)

    mini_map.RenderMiniMap(display)

    pygame.display.flip()

pygame.quit()
