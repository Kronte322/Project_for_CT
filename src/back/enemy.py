from abc import ABC, abstractmethod

from src.back.Config import *


class Enemy:
    def __init__(self, position, health, size):
        self.position = position
        self.health = health
        self.size = size
        self.direction_of_movement = None
        self.num_of_frames_with_movement = 0

    def Move(self):
        if self.num_of_frames_with_movement > 0:
            self.position[0] += self.direction_of_movement[0]
            self.position[1] += self.direction_of_movement[1]
            self.num_of_frames_with_movement = max(self.num_of_frames_with_movement - 1, 0)

    def StopMovement(self):
        self.num_of_frames_with_movement = 0

    def GetDirectionOfMovement(self):
        return self.direction_of_movement

    def IsMove(self):
        return self.num_of_frames_with_movement > 0

    def SetDirectionOfMovement(self, direction, num_of_frames):
        self.num_of_frames_with_movement = num_of_frames
        self.direction_of_movement = direction


    def GetCenter(self):
        return self.position[0] + self.size // 2, self.position[1] + self.size // 2

    def GetPosition(self):
        return self.position

    def SetPosition(self, position):
        self.position = position

    def GetPointsOfMovement(self):
        lst = [[self.position[0], self.position[1] + self.size // 2],
                [self.position[0] + self.size, self.position[1] + self.size],
                [self.position[0], self.position[1] + self.size],
                [self.position[0] + self.size, self.position[1] + self.size // 2]]
        return lst

    @abstractmethod
    def Attack(self):
        pass


class MeleeEnemy(Enemy):
    def __init__(self, position, health, size):
        super().__init__(position, health, size)

    def Attack(self):
        pass


class RangeEnemy(Enemy, ABC):
    def __init__(self, position, health, size):
        super().__init__(position, health, size)


class RangeSkeleton(RangeEnemy):
    def __init__(self, position):
        super().__init__(position, HEALTH_OF_SKELETON, SIZE_OF_SKELETON)

    def Attack(self):
        pass
