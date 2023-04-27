from src.back.class_map import MapProcessor
from src.back.Render import Render
from src.back.Window import Window


class Game:
    @staticmethod
    def StartGameSession(character):
        window = Window()
        map_processor = MapProcessor()
        # player = Player(character, map_processor.GetSpawnPosition())
        # render = Render(window.GetDisplay(), player, map_processor)
