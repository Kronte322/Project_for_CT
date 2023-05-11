
import sys
import pygame
from src.back.Map import map
from src.back.Map.constants_for_map import *
from src.back.Map.minimap import MiniMap
from src.back.player import Player
from src.back.personages import personages


sys.setrecursionlimit(10000000)
mappa = class_map.MapProcessor()
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


player = Player(display, personages[12], kSpawnPosition)

RUNNING = True
while RUNNING:
    clock.tick(kFramesPerSec)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
        mini_map.ProcessEvents(event=event)

    player.move(mappa, mini_map)

    display.fill((37, 19, 26))

    mappa.UpdateCurrentRoom([player.rect.x + kSizeOfCharacter // 2, player.rect.y + kSizeOfCharacter], mini_map)

    mappa.RenderRoom(display)

    player.render(display, mappa)
    # player.fire(display, mappa)

    mini_map.RenderMiniMap(display)

    pygame.display.flip()

pygame.quit()
