from src.back.Map.map_generator import MapBuilder
from src.back.Map.space import *


class Eventor:
    def __init__(self, player, map_processor):
        self.player = player
        self.map_processor = map_processor
        self.room = self.map_processor.GetCurrentRoom()
        self.prev_position_of_player = None

    def EnterRoomEvent(self):
        if self.map_processor.GetCurrentRoom() is not self.room:
            if isinstance(self.map_processor.GetCurrentRoom(), RoomSpace):
                vectors = {'D': (0, SIZE_OF_TILE), 'U': (0, -SIZE_OF_TILE), 'R': (SIZE_OF_TILE, 0),
                           'L': (-SIZE_OF_TILE, 0)}
                self.player.ChangePosition(vectors[self.map_processor.GetSideOfDoor(self.prev_position_of_player)])
                self.map_processor.CloseDoors()

        self.room = self.map_processor.GetCurrentRoom()
        self.prev_position_of_player = self.player.GetStandPosition()

    def Update(self):
        if self.prev_position_of_player is None:
            self.prev_position_of_player = self.player.GetStandPosition()
        self.EnterRoomEvent()
