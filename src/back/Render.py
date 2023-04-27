from src.back.constants_for_map import *


class Render:
    def __init__(self, display, player, map_processor):
        self.display = display
        self.player = player
        self.map_processor = map_processor
        self.position_of_player_on_the_screen = POSITION_OF_PLAYER_ON_SCREEN

    def Update(self):
        pass

    def DrawPlayer(self):
        self.display.blit(self.player.GetImage(),
                          (self.position_of_player_on_the_screen[0] - self.player.GetSize()[0] // 2,
                           self.position_of_player_on_the_screen[1] - self.player.GetSize()[1] // 2))

    def DrawMap(self):
        position_to_blit = (self.player.GetPosition()[0] - self.map_processor.GetCurrentRoom().GetPosition()[0] +
                            self.position_of_player_on_the_screen[0],
                            self.player.GetPosition()[0] - self.map_processor.GetCurrentRoom().GetPosition()[0] +
                            self.position_of_player_on_the_screen[1])
        self.display(position_to_blit, self.map_processor.GetCurrentRoom().GetSurface())

    def Draw(self):
        self.Update()
        self.DrawMap()
        self.DrawPlayer()
