import sys

import src.back.personages as personages
from src.back.Game import Game

sys.setrecursionlimit(10000000)

Game.StartGameSession(personages.personages[12])
