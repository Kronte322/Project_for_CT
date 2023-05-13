from src.back.Map.space import *


class Eventor:
    def __init__(self, player, map_processor, mini_map):
        self.player = player
        self.map_processor = map_processor
        self.mini_map = mini_map
        self.room = self.map_processor.GetCurrentRoom()
        self.prev_position_of_player = None
        self.num_of_iterations = 0

    def EnterRoomEvent(self):
        if self.map_processor.GetCurrentRoom() is not self.room:
            if isinstance(self.map_processor.GetCurrentRoom(), RoomSpace):
                vectors = {'D': (0, SIZE_OF_TILE // 4), 'U': (0, -SIZE_OF_TILE // 4), 'R': (SIZE_OF_TILE // 4, 0),
                           'L': (-SIZE_OF_TILE // 4, 0)}
                self.player.ChangePosition(vectors[self.map_processor.GetSideOfDoor(self.prev_position_of_player)])
                self.mini_map.MoveMiniMap((-vectors[self.map_processor.GetSideOfDoor(self.prev_position_of_player)][0],
                                           -vectors[self.map_processor.GetSideOfDoor(self.prev_position_of_player)][1]))
        self.room = self.map_processor.GetCurrentRoom()
        self.prev_position_of_player = self.player.GetStandPosition()

    def OnStart(self):
        self.map_processor.GenerateExit()

    def Update(self):
        if self.num_of_iterations == 0:
            self.OnStart()
        if self.prev_position_of_player is None:
            self.prev_position_of_player = self.player.GetStandPosition()
        self.EnterRoomEvent()
        self.num_of_iterations += 1
