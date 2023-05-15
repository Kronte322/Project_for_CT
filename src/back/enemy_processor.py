import math
import random

from src.back.Map.constants_for_map import *
from src.back.enemy import *


def rotate_vector(vector, angle):
    x = vector[0] * math.cos(angle) - vector[1] * math.sin(angle)
    y = vector[0] * math.sin(angle) + vector[1] * math.cos(angle)
    return [x, y]


class EnemyProcessor:
    def __init__(self, map_processor, player):
        self.map_processor = map_processor
        self.player = player
        self.enemies = []

    def GetEnemies(self):
        return self.enemies

    def AddEnemy(self, enemy):
        self.enemies.append(enemy)

    def SpawnInCurrentRoom(self, num_of_enemies):
        tiles = self.map_processor.GetCurrentRoom().GetCoordinatesOfTiles()
        for i in range(num_of_enemies):
            while True:
                position = random.choice(tiles)
                if self.map_processor.CanStandThere([position[0] * SIZE_OF_TILE, position[1] * SIZE_OF_TILE]):
                    self.AddEnemy(RangeSkeleton([position[0] * SIZE_OF_TILE, position[1] * SIZE_OF_TILE]))
                    break

    def CheckIfCanMove(self, enemy, vector):
        for point in enemy.GetPointsOfMovement():
            if not self.map_processor.CanStandThere([point[0] + vector[0], point[1] + vector[1]]):
                return False
        return True

    def GenerateNewMovement(self, enemy, vector_of_movement=None):
        if vector_of_movement is None:
            position_of_player = self.player.GetPosition()
            position_of_enemy = enemy.GetPosition()
            hypotenuse = math.dist(position_of_enemy, position_of_player)
            x_coord = position_of_player[0] - position_of_enemy[0]
            y_coord = position_of_player[1] - position_of_enemy[1]
            first_cos = x_coord / hypotenuse
            second_cos = y_coord / hypotenuse
            vector_of_movement = (
                SPEED_OF_ENEMY * first_cos, SPEED_OF_ENEMY * second_cos)
        vector_of_movement = rotate_vector(vector_of_movement, math.radians(random.randint(-45, 45)))
        enemy.SetDirectionOfMovement(vector_of_movement, NUM_OF_FRAMES_WITH_MOVEMENT)
        return vector_of_movement

    def Update(self):
        for enemy in self.enemies:
            if enemy.IsMove():
                if self.CheckIfCanMove(enemy, enemy.GetDirectionOfMovement()):
                    enemy.Move()
                else:
                    enemy.StopMovement()
            else:
                while True:
                    self.GenerateNewMovement(enemy, enemy.GetDirectionOfMovement())
                    if self.CheckIfCanMove(enemy, enemy.GetDirectionOfMovement()):
                        enemy.Move()
                        break
