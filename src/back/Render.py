from src.back.constants_for_map import *
import pygame

class Render:
    def __init__(self, display, player, map_processor):
        self.display = display
        self.player = player
        self.map_processor = map_processor
        self.position_of_player_on_the_screen = POSITION_OF_PLAYER_ON_SCREEN
        self.moveBox = (WINDOW_SIZE[0] // 2 - SIZE_OF_MOVE_BOX[0] // 2, WINDOW_SIZE[1] // 2 - SIZE_OF_MOVE_BOX[1] // 2,
                        WINDOW_SIZE[0] // 2 + SIZE_OF_MOVE_BOX[0] // 2, WINDOW_SIZE[1] // 2 + SIZE_OF_MOVE_BOX[1] // 2)

    def GetPlayerPositionOnTheScreen(self):
        return self.position_of_player_on_the_screen

    def ChangePositionOfPlayerAccordingToMoveBox(self, vector):
        pass
        # if self.moveBox[0] <= self.position_of_player_on_the_screen[0] + vector[0] <= self.moveBox[2] - 48:
        #     self.position_of_player_on_the_screen[0] += vector[0]  # mappa.MoveMap([-self.direction[0], 0])
        #
        # if self.moveBox[1] <= self.position_of_player_on_the_screen[1] + vector[1] <= self.moveBox[3] - 48:
        #     self.position_of_player_on_the_screen[1] += vector[1]  # mappa.MoveMap([0, -self.direction[1]])

    def Update(self):

        pass

    # def DrawObjects(self):
    #

    def DrawPlayer(self):
        self.player.render(self.display, self.position_of_player_on_the_screen)

    def DrawMap(self):
        position_to_blit = (self.map_processor.GetCurrentRoom().GetPosition()[0] - self.player.GetPosition()[0]+
                            self.position_of_player_on_the_screen[0],
                            self.map_processor.GetCurrentRoom().GetPosition()[1] - self.player.GetPosition()[1] +
                            self.position_of_player_on_the_screen[1])
        self.display.blit(self.map_processor.GetCurrentRoom().GetSurface(), position_to_blit)

    def Draw(self):
        self.Update()
        self.display.fill((37, 19, 26))
        self.DrawMap()
        self.DrawPlayer()
        pygame.display.flip()
