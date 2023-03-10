import random
import time

random.seed(time.time())

kNumOfBasicRooms = 50
kNumOfSemiBasicRooms = 50

kMaxNumOfRoomsInSemiBasic = 2

kMinWidthOfBasicRoom = 5
kMaxWidthOfBasicRoom = 10

kNumOfRoomsOnMap = 10000000
kNumOfAdditionalRooms = 50

kMinFreqOfDoor = 10
kMaxFreqOfDoor = 20

kDoor = 'D'
kSign = 'S'
kFloor = '-'
kPath = 'P'
kWall = 'X'
kEmpty = 'E'
kOneWidthPath = 'O'
kBoardOfMap = 'B'


class MapGenerator:
    def __init__(self):
        self.main_matrix = []
        self.basic_rooms = []
        self.size = []

    def GenerateMap(self, size=(30, 20)):
        self.main_matrix = []
        self.basic_rooms = []
        self.size = size
        self.FillMatrix()
        self.SetBoardsOfMap()
        self.GenerateBasicRooms()
        self.GenerateMapWithRooms()
        self.AdditiobalGeneration()
        self.PostProcessing()
        return self.main_matrix

    def IsItWallForDoor(self, position: tuple):
        if self.GetTile(position) in [kWall]:
            if self.GetTile((position[0], position[1] + 1)) in [kWall, kDoor] and self.GetTile(
                    (position[0], position[1] - 1)) in [kWall, kDoor]:
                if self.GetTile((position[0] - 1, position[1])) in [kEmpty] and self.GetTile(
                        (position[0] + 1, position[1])) in [kFloor]:
                    return True
                if self.GetTile((position[0] - 1, position[1])) in [kFloor] and self.GetTile(
                        (position[0] + 1, position[1])) in [kEmpty]:
                    return True
            if self.GetTile((position[0] + 1, position[1])) in [kWall, kDoor] and self.GetTile(
                    (position[0] - 1, position[1])) in [kWall, kDoor]:
                if self.GetTile((position[0], position[1] - 1)) in [kEmpty] and self.GetTile(
                        (position[0], position[1] + 1)) in [kFloor]:
                    return True
                if self.GetTile((position[0], position[1] - 1)) in [kFloor] and self.GetTile(
                        (position[0], position[1] + 1)) in [kEmpty]:
                    return True
        return False

    def IsThereCorner(self, position: tuple):
        if self.IsThereAnyTile(position, [kEmpty]):
            if self.GetTile(position) in [kWall] and self.GetTile((position[0] - 1, position[1])) in [
                kWall] and self.GetTile((position[0], position[1] + 1)) in [kWall]:
                return True
            if self.GetTile(position) in [kWall] and self.GetTile((position[0] - 1, position[1])) in [
                kWall] and self.GetTile((position[0], position[1] - 1)) in [kWall]:
                return True
            if self.GetTile(position) in [kWall] and self.GetTile((position[0] + 1, position[1])) in [
                kWall] and self.GetTile((position[0], position[1] + 1)) in [kWall]:
                return True
            if self.GetTile(position) in [kWall] and self.GetTile((position[0] + 1, position[1])) in [
                kWall] and self.GetTile((position[0], position[1] - 1)) in [kWall]:
                return True
        return False

    def IsThereCutCorner(self, position: tuple):
        if self.IsThereAnyTile(position, [kEmpty]):
            if self.GetTile(position) in [kFloor] and self.GetTile((position[0] - 1, position[1])) in [
                kWall] and self.GetTile((position[0], position[1] + 1)) in [kWall]:
                return True
            if self.GetTile(position) in [kFloor] and self.GetTile((position[0] - 1, position[1])) in [
                kWall] and self.GetTile((position[0], position[1] - 1)) in [kWall]:
                return True
            if self.GetTile(position) in [kFloor] and self.GetTile((position[0] + 1, position[1])) in [
                kWall] and self.GetTile((position[0], position[1] + 1)) in [kWall]:
                return True
            if self.GetTile(position) in [kFloor] and self.GetTile((position[0] + 1, position[1])) in [
                kWall] and self.GetTile((position[0], position[1] - 1)) in [kWall]:
                return True
        return False

    def IsThereCutCornerAfterCreate(self, position: tuple):
        if self.IsThereAnyTile(position, [kFloor]):
            if self.GetTile(position) in [kEmpty] and self.GetTile((position[0] - 1, position[1])) in [
                kWall] and self.GetTile((position[0], position[1] + 1)) in [kWall]:
                return True
            if self.GetTile(position) in [kEmpty] and self.GetTile((position[0] - 1, position[1])) in [
                kWall] and self.GetTile((position[0], position[1] - 1)) in [kWall]:
                return True
            if self.GetTile(position) in [kEmpty] and self.GetTile((position[0] + 1, position[1])) in [
                kWall] and self.GetTile((position[0], position[1] + 1)) in [kWall]:
                return True
            if self.GetTile(position) in [kEmpty] and self.GetTile((position[0] + 1, position[1])) in [
                kWall] and self.GetTile((position[0], position[1] - 1)) in [kWall]:
                return True
        return False

    def GetTile(self, position: tuple):
        return self.main_matrix[position[0]][position[1]]

    def GetNeighbours(self, position: tuple):
        result = []
        if position[0] > 0:
            result.append((position[0] - 1, position[1]))
        if position[0] < len(self.main_matrix) - 1:
            result.append((position[0] + 1, position[1]))
        if position[1] > 0:
            result.append((position[0], position[1] - 1))
        if position[1] < len(self.main_matrix[0]) - 1:
            result.append((position[0], position[1] + 1))
        return result

    def GetAround(self, position: tuple):
        result = []
        interm = []

        if position[0] > 0 and position[1] > 0:
            interm.append((position[0] - 1, position[1] - 1))
        else:
            interm.append((-1, -1))
        if position[0] > 0:
            interm.append((position[0] - 1, position[1]))
        else:
            interm.append((-1, -1))
        if position[0] > 0 and position[1] < len(self.main_matrix[0]) - 1:
            interm.append((position[0] - 1, position[1] + 1))
        else:
            interm.append((-1, -1))
        result.append(interm.copy())

        interm.clear()

        if position[1] > 0:
            interm.append((position[0], position[1] - 1))
        else:
            interm.append((-1, -1))
        interm.append((position[0], position[1]))
        if position[1] < len(self.main_matrix[0]) - 1:
            interm.append((position[0], position[1] + 1))
        else:
            interm.append((-1, -1))
        result.append(interm.copy())

        interm.clear()

        if position[0] < len(self.main_matrix) - 1 and position[1] > 0:
            interm.append((position[0] + 1, position[1] - 1))
        else:
            interm.append((-1, -1))
        if position[0] < len(self.main_matrix) - 1:
            interm.append((position[0] + 1, position[1]))
        else:
            interm.append((-1, -1))
        if position[0] < len(self.main_matrix) - 1 and position[1] < len(self.main_matrix[0]) - 1:
            interm.append((position[0] + 1, position[1] + 1))
        else:
            interm.append((-1, -1))
        result.append(interm.copy())

        interm.clear()

        return result

    def GetLeftAround(self, position):
        around = self.GetAround(position).copy()
        around.pop()
        return around

    def GetUpAround(self, position):
        around = self.GetAround(position)
        res = []
        for i in range(len(around)):
            interm = []
            for j in range(len(around[0]) - 1):
                interm.append(around[i][j])
            res.append(interm)
        return res

    def GetRightAround(self, position):
        around = self.GetAround(position)
        res = []
        for i in range(1, len(around)):
            res.append(around[i])
        return res

    def GetDownAround(self, position):
        around = self.GetAround(position)
        res = []
        for i in range(len(around)):
            interm = []
            for j in range(1, len(around[0])):
                interm.append(around[i][j])
            res.append(interm)
        return res

    # def IsAbleToMove(self, position):

    def GetAroundForDFS(self, position, parent):
        if position[0] > parent[0]:
            return self.GetLeftAround(parent)
        if position[0] < parent[0]:
            return self.GetRightAround(parent)
        if position[1] > parent[1]:
            return self.GetUpAround(parent)
        if position[1] < parent[1]:
            return self.GetDownAround(parent)

    def GetAroundForDeadEnds(self, position, parent):
        if position[0] > parent[0]:
            return self.GetRightAround(position)
        if position[0] < parent[0]:
            return self.GetLeftAround(position)
        if position[1] > parent[1]:
            return self.GetDownAround(position)
        if position[1] < parent[1]:
            return self.GetUpAround(position)

    def WhatSideMyParent(self, position, parent):
        if position[0] > parent[0]:
            return 'R'
        if position[0] < parent[0]:
            return 'L'
        if position[1] > parent[1]:
            return 'D'
        if position[1] < parent[1]:
            return 'U'

    def NumOfTiles(self, list_of_tiles, position):
        res = 0
        for i in list_of_tiles:
            for j in i:
                if j not in [(-1, -1), position]:
                    if self.GetTile(j) not in [kEmpty, kBoardOfMap]:
                        res += 1
        return res

    def IsThereDeadEnd(self, position, parent_position):
        if self.NumOfTiles(self.GetAroundForDeadEnds(position, parent_position), position) == 0:
            return True
        return False

    def GetMap(self):
        return self.main_matrix

    def FillMatrix(self):
        for i in range(self.size[0]):
            interm = []
            for j in range(self.size[1]):
                interm.append(kEmpty)
            self.main_matrix.append(interm)

    def GenerateBasicRooms(self):
        for i in range(kNumOfBasicRooms):
            interm = []
            x_coord = random.randrange(
                kMinWidthOfBasicRoom, kMaxWidthOfBasicRoom)
            y_coord = random.randrange(
                kMinWidthOfBasicRoom, kMaxWidthOfBasicRoom)
            right_down_corner = (x_coord, y_coord)
            for i in range(right_down_corner[0]):
                interm_array = []
                for j in range(right_down_corner[1]):
                    interm_array.append(kFloor)
                interm.append(interm_array)
            self.basic_rooms.append(interm)

    def GetSizeOfBasicRoom(self, basic_room):
        width = len(basic_room)
        height = len(basic_room[0])
        return (width, height)

    def IsThereIntersec(self, room, pos_of_room: tuple) -> bool:
        size_of_room = self.GetSizeOfBasicRoom(room)
        bounds_for_loop = []
        if pos_of_room[0] > 1:
            bounds_for_loop.append(-2)
        else:
            bounds_for_loop.append(-1)

        if pos_of_room[0] + size_of_room[0] < len(self.main_matrix) - 1:
            bounds_for_loop.append(size_of_room[0] + 2)
        else:
            bounds_for_loop.append(size_of_room[0] + 1)

        if pos_of_room[1] > 1:
            bounds_for_loop.append(-2)
        else:
            bounds_for_loop.append(-1)

        if pos_of_room[1] + size_of_room[1] < len(self.main_matrix[0]) - 1:
            bounds_for_loop.append(size_of_room[1] + 2)
        else:
            bounds_for_loop.append(size_of_room[1] + 1)

        for i in range(bounds_for_loop[0], bounds_for_loop[1]):
            for j in range(bounds_for_loop[2], bounds_for_loop[3]):
                if self.main_matrix[pos_of_room[0] + i][pos_of_room[1] + j] != kEmpty:
                    return True
        return False

    def GenerateMapWithRooms(self):
        num_of_generated_rooms = 0
        num_of_generations = 0
        while num_of_generated_rooms != kNumOfRoomsOnMap:

            if num_of_generations == 1000:
                break
            num_of_generations += 1

            num_of_basic_room = random.randrange(0, kNumOfBasicRooms)
            basic_room = self.basic_rooms[num_of_basic_room]
            width_of_basic_room = self.GetSizeOfBasicRoom(basic_room)[0]
            height_of_basic_room = self.GetSizeOfBasicRoom(basic_room)[1]
            x_coord = random.randrange(2, self.size[0] - width_of_basic_room - 1)
            y_coord = random.randrange(2, self.size[1] - height_of_basic_room - 1)
            left_corner_position = (x_coord, y_coord)
            sign = False
            counter = 0
            while sign != True:
                if counter == 50:
                    break

                counter += 1
                if not self.IsThereIntersec(basic_room, left_corner_position):
                    sign = True
                    num_of_generated_rooms += 1
                    for i in range(-1, width_of_basic_room + 1):
                        for j in range(-1, height_of_basic_room + 1):
                            if i == -1 or i == width_of_basic_room or j == -1 or j == height_of_basic_room:
                                self.main_matrix[left_corner_position[0] +
                                                 i][left_corner_position[1] + j] = kWall
                            else:
                                self.main_matrix[left_corner_position[0] +
                                                 i][left_corner_position[1] + j] = kFloor

    def IsInCrossAnyTile(self, position, tiles) -> bool:
        if position[0] > 0:
            if self.main_matrix[position[0] - 1][position[1]] in tiles:
                return True
        if position[0] < len(self.main_matrix) - 1:
            if self.main_matrix[position[0] + 1][position[1]] in tiles:
                return True
        if position[1] > 0:
            if self.main_matrix[position[0]][position[1] - 1] in tiles:
                return True
        if position[1] < len(self.main_matrix) - 1:
            if self.main_matrix[position[0]][position[1] + 1] in tiles:
                return True
        if position[0] == 0 or position[0] == len(self.main_matrix) - 1 or position[1] == 0 or position[1] == len(
                self.main_matrix[0]) - 1:
            return True
        return False

    def IsThereAnyTile(self, position, tiles) -> bool:
        if self.main_matrix[position[0] - 1][position[1]] in tiles:
            return True
        if self.main_matrix[position[0] + 1][position[1]] in tiles:
            return True
        if self.main_matrix[position[0]][position[1] - 1] in tiles:
            return True
        if self.main_matrix[position[0]][position[1] + 1] in tiles:
            return True
        if self.main_matrix[position[0] - 1][position[1] + 1] in tiles:
            return True
        if self.main_matrix[position[0] - 1][position[1] - 1] in tiles:
            return True
        if self.main_matrix[position[0] + 1][position[1] + 1] in tiles:
            return True
        if self.main_matrix[position[0] + 1][position[1] - 1] in tiles:
            return True
        return False

    def AdditiobalGeneration(self):
        num_of_generated = 0
        while num_of_generated != kNumOfAdditionalRooms:
            num_of_generated += 1
            num_of_basic_room = random.randrange(0, kNumOfBasicRooms)
            basic_room = self.basic_rooms[num_of_basic_room]
            width_of_basic_room = self.GetSizeOfBasicRoom(basic_room)[0]
            height_of_basic_room = self.GetSizeOfBasicRoom(basic_room)[1]
            x_coord = random.randrange(2, self.size[0] - width_of_basic_room - 1)
            y_coord = random.randrange(2, self.size[1] - height_of_basic_room - 1)
            left_corner_position = (x_coord, y_coord)

            for i in range(-1, width_of_basic_room + 1):
                for j in range(-1, height_of_basic_room + 1):
                    if i == -1 or i == width_of_basic_room or j == -1 or j == height_of_basic_room:
                        if self.main_matrix[left_corner_position[0] +
                                            i][left_corner_position[1] + j] == kEmpty:
                            self.main_matrix[left_corner_position[0] +
                                             i][left_corner_position[1] + j] = kWall
                        elif self.main_matrix[left_corner_position[0] +
                                              i][left_corner_position[1] + j] == kWall and not self.IsInCrossAnyTile(
                            (left_corner_position[0] +
                             i, left_corner_position[1] + j), [kEmpty, kBoardOfMap]):
                            self.main_matrix[left_corner_position[0] +
                                             i][left_corner_position[1] + j] = kFloor
                    else:
                        self.main_matrix[left_corner_position[0] +
                                         i][left_corner_position[1] + j] = kFloor

    def IsThereAllFloors(self, position):
        counter = 0
        if position[0] > 0:
            if self.main_matrix[position[0] - 1][position[1]] in [kFloor, kWall]:
                counter += 1

        if position[0] < len(self.main_matrix[0]) - 1:
            if self.main_matrix[position[0] + 1][position[1]] in [kFloor, kWall]:
                counter += 1

        if position[1] > 0:
            if self.main_matrix[position[0]][position[1] - 1] in [kFloor, kWall]:
                counter += 1

        if position[1] < len(self.main_matrix) - 1:
            if self.main_matrix[position[0]][position[1] + 1] in [kFloor, kWall]:
                counter += 1

        if counter > 2:
            return True
        return False

    def DeleteWallsOnDiagonal(self):
        for i in range(len(self.main_matrix) - 1):
            for j in range(len(self.main_matrix[0]) - 1):
                if self.main_matrix[i][j] == kWall and self.main_matrix[i + 1][j] == kFloor and self.main_matrix[i][
                    j + 1] == kFloor and self.main_matrix[i + 1][j + 1] == kWall:
                    self.main_matrix[i + 1][j] = kWall
                    self.main_matrix[i][j + 1] = kWall
                elif self.main_matrix[i][j] == kFloor and self.main_matrix[i + 1][j] == kWall and self.main_matrix[i][
                    j + 1] == kWall and self.main_matrix[i + 1][j + 1] == kFloor:
                    self.main_matrix[i][j] = kWall
                    self.main_matrix[i + 1][j + 1] = kWall

    def OneWidthPaths(self):
        self.OneWidthPathsHorizontal()
        self.OneWidthPathsVertical()

    def OneWidthPathsVertical(self):
        for i in range(len(self.main_matrix)):
            for j in range(1, len(self.main_matrix[0]) - 1):
                if self.main_matrix[i][j] == kEmpty and self.main_matrix[i][j - 1] == kWall and self.main_matrix[i][
                    j + 1] == kWall:
                    self.main_matrix[i][j] = kOneWidthPath

    def OneWidthPathsHorizontal(self):
        for i in range(1, len(self.main_matrix) - 1):
            for j in range(len(self.main_matrix[0])):
                if self.main_matrix[i][j] == kEmpty and self.main_matrix[i - 1][j] == kWall and self.main_matrix[i + 1][
                    j] == kWall:
                    self.main_matrix[i][j] = kOneWidthPath

    def TwoWidthPaths(self):
        self.TwoWidthPathsHorizontal()
        self.TwoWidthPathsVertical()

    def TwoWidthPathsVertical(self):
        for i in range(len(self.main_matrix)):
            for j in range(1, len(self.main_matrix[0]) - 2):
                if self.main_matrix[i][j] == kEmpty and self.main_matrix[i][j - 1] == kWall and self.main_matrix[i][
                    j + 1] == kEmpty and self.main_matrix[i][j + 2] == kWall:
                    self.main_matrix[i][j] = kOneWidthPath
                    self.main_matrix[i][j + 1] = kOneWidthPath

    def TwoWidthPathsHorizontal(self):
        for i in range(1, len(self.main_matrix) - 2):
            for j in range(len(self.main_matrix[0])):
                if self.main_matrix[i][j] == kEmpty and self.main_matrix[i - 1][j] == kWall and self.main_matrix[i + 1][
                    j] == kEmpty and self.main_matrix[i + 2][j] == kWall:
                    self.main_matrix[i][j] = kOneWidthPath
                    self.main_matrix[i + 1][j] = kOneWidthPath

    def DeleteWallsInsideRooms(self):
        for i in range(len(self.main_matrix)):
            for j in range(len(self.main_matrix[0])):
                if self.main_matrix[i][j] == kWall:
                    if self.IsThereAllFloors((i, j)) and not self.IsInCrossAnyTile((i, j), [kEmpty, kBoardOfMap]):
                        self.main_matrix[i][j] = kFloor

    def IsThereDoorBetweenRooms(self, position: tuple):
        if (self.GetTile(position) in [kEmpty] and self.GetTile((position[0] - 1, position[1])) in [
            kWall] and self.GetTile((position[0] + 1, position[1])) in [kWall]) or (
                self.GetTile(position) in [kEmpty] and self.GetTile((position[0], position[1] - 1)) in [
            kWall] and self.GetTile((position[0], position[1] + 1)) in [kWall]):
            if self.GetTile((position[0] - 1, position[1] + 1)) in [kWall] and self.GetTile(
                    (position[0] - 1, position[1] - 1)) in [kWall]:
                if self.GetTile((position[0] + 1, position[1] + 1)) in [kWall] and self.GetTile(
                        (position[0] + 1, position[1] - 1)) in [kWall]:
                    return True
        return False

    def PostProcessing(self):
        self.DeleteWallsInsideRooms()
        self.DeleteWallsOnDiagonal()
        self.dfs = DFSAlgo(self)
        self.SetPathsOnMap()
        self.DeleteCutCorners()
        self.SetDoorsBetweenRooms()
        self.DeleteDubleDoors()
        self.SetFloorInFrontOfDoor()
        self.DeleteDeadEnds()
        self.DeleteFakeDoors()
        list_of_corners = []
        self.MakeCutCorners(list_of_corners)
        self.DeleteNotConnectedComponents()
        self.DeleteCutCornersAfterCreate(list_of_corners)
        self.DeleteWrongWall()
        self.DeleteCutCorners()

    def CountEmptyTiles(self, position):
        list = self.GetAround(position)
        res = 0
        for i in list:
            for j in i:
                if self.GetTile((j[0], j[1])) in [kEmpty, kBoardOfMap]:
                    res += 1
        return res

    def IsThereWrongWall(self, position):
        if self.GetTile(position) in [kWall] and self.CountEmptyTiles(position) > 5:
            return True
        return False

    def DeleteWrongWall(self):
        for i in range(1, len(self.main_matrix) - 1):
            for j in range(1, len(self.main_matrix[0]) - 1):
                if self.IsThereWrongWall((i, j)):
                    self.main_matrix[i][j] = kEmpty
        # self.SetDoorWaysOnMap()

    def IsThereFakeDoor(self, position):
        if self.GetTile((position[0] - 1, position[1])) in [kPath]:
            if self.GetTile((position[0] - 2, position[1])) in [kEmpty, kBoardOfMap]:
                return (position[0] - 1, position[1])
        if self.GetTile((position[0] + 1, position[1])) in [kPath]:
            if self.GetTile((position[0] + 2, position[1])) in [kEmpty, kBoardOfMap]:
                return (position[0] + 1, position[1])
        if self.GetTile((position[0], position[1] + 1)) in [kPath]:
            if self.GetTile((position[0], position[1] + 2)) in [kEmpty, kBoardOfMap]:
                return (position[0], position[1] + 1)
        if self.GetTile((position[0], position[1] - 1)) in [kPath]:
            if self.GetTile((position[0], position[1] - 2)) in [kEmpty, kBoardOfMap]:
                return (position[0], position[1] - 1)
        return False

    def DeleteFakeDoors(self):
        for i in range(1, len(self.main_matrix) - 1):
            for j in range(1, len(self.main_matrix[0]) - 1):
                if self.GetTile((i, j)) in [kDoor]:
                    interm = self.IsThereFakeDoor((i, j))
                    if interm != False:
                        self.main_matrix[i][j] = kWall
                        self.main_matrix[interm[0]][interm[1]] = kEmpty

    def SetBoardsOfMap(self):
        for i in range(len(self.main_matrix)):
            self.main_matrix[i][0] = kBoardOfMap
        for i in range(len(self.main_matrix[0])):
            self.main_matrix[len(self.main_matrix) - 1][i] = kBoardOfMap
        for i in range(len(self.main_matrix)):
            self.main_matrix[i][len(self.main_matrix[0]) - 1] = kBoardOfMap
        for i in range(len(self.main_matrix[0])):
            self.main_matrix[0][i] = kBoardOfMap

    def DeleteCutCorners(self):
        for i in range(1, len(self.main_matrix) - 1):
            for j in range(1, len(self.main_matrix[0]) - 1):
                if self.IsThereCutCorner((i, j)):
                    self.main_matrix[i][j] = kWall

    def DeleteCutCornersAfterCreate(self, list_of_corners):
        for i in list_of_corners:
            self.main_matrix[i[0]][i[1]] = kWall

    def MakeCutCorners(self, list_of_corners):
        for i in range(1, len(self.main_matrix) - 1):
            for j in range(1, len(self.main_matrix[0]) - 1):
                if self.IsThereCorner((i, j)):
                    list_of_corners.append((i, j))
                    self.main_matrix[i][j] = kEmpty

    def SetPathsOnMap(self):
        for i in range(1, len(self.main_matrix) - 1):
            for j in range(1, len(self.main_matrix[0]) - 1):
                if self.main_matrix[i][j] == kEmpty:
                    self.dfs.DFS((i, j))
                    for k in self.dfs.GetPath():
                        self.main_matrix[k[0]][k[1]] = kPath
        self.dfs.Clear()

    def SetDoorWaysOnMap(self):
        for i in range(1, len(self.main_matrix) - 1):
            for j in range(1, len(self.main_matrix[0]) - 1):
                if self.GetTile((i, j)) in [kWall] and self.IsThereCorner((i, j)):
                    self.dfs.DFSForCornersOfRoom((i, j))
                    # return
        for k in self.dfs.GetPath():
            self.main_matrix[k[0]][k[1]] = kSign
        self.dfs.Clear()

    def SetDoorsBetweenRooms(self):
        counter = 1
        freq_of_door = random.randrange(kMinFreqOfDoor, kMaxFreqOfDoor)
        for i in range(1, len(self.main_matrix) - 1):
            for j in range(1, len(self.main_matrix[0]) - 1):
                if self.IsThereDoorBetweenRooms((i, j)):
                    counter += 1
                    if counter % freq_of_door == 0:
                        if self.GetTile((i + 1, j)) in kWall:
                            self.main_matrix[i - 1][j] = kDoor
                            self.main_matrix[i + 1][j] = kDoor
                        else:
                            self.main_matrix[i][j - 1] = kDoor
                            self.main_matrix[i][j + 1] = kDoor

                        counter = 1
                        freq_of_door = random.randrange(
                            kMinFreqOfDoor, kMaxFreqOfDoor)

    def DeleteDubleDoors(self):
        for i in range(1, len(self.main_matrix) - 1):
            for j in range(1, len(self.main_matrix[0]) - 1):
                if self.dfs.used.get((i, j)) == None:
                    if self.GetTile((i, j)) in [kDoor] and self.GetTile((i - 1, j)) in [kDoor]:
                        self.main_matrix[i - 1][j] = kWall
                    if self.GetTile((i, j)) in [kDoor] and self.GetTile((i, j - 1)) in [kDoor]:
                        self.main_matrix[i][j - 1] = kWall

    def SetFloorInFrontOfDoor(self):
        for i in range(1, len(self.main_matrix) - 1):
            for j in range(1, len(self.main_matrix[0]) - 1):
                if self.GetTile((i, j)) in [kDoor]:
                    if self.GetTile((i + 1, j)) in [kFloor]:
                        self.main_matrix[i - 1][j] = kPath
                    if self.GetTile((i - 1, j)) in [kFloor]:
                        self.main_matrix[i + 1][j] = kPath
                    if self.GetTile((i, j + 1)) in [kFloor]:
                        self.main_matrix[i][j - 1] = kPath
                    if self.GetTile((i, j - 1)) in [kFloor]:
                        self.main_matrix[i][j + 1] = kPath

    def DeleteDeadEnds(self):
        for i in range(1, len(self.main_matrix) - 1):
            for j in range(1, len(self.main_matrix[0]) - 1):
                if self.GetTile((i, j)) in [kPath] and self.IsThereAnyTile((i, j), [kDoor]):
                    self.dfs.DFSforDeletingDeadEnds((i, j))
        self.dfs.Clear()

    def ClearMatrix(self):
        for i in range(len(self.main_matrix)):
            for j in range(len(self.main_matrix[0])):
                self.main_matrix[i][j] = kEmpty

    def DeleteNotConnectedComponents(self):
        matrix = []
        sign = False
        for i in range(1, len(self.main_matrix) - 1):
            for j in range(1, len(self.main_matrix[0]) - 1):
                if self.GetTile((i, j)) in [kDoor]:
                    self.dfs.FinalDFS((i, j), matrix)
                    sign = True
                    break
            if sign:
                break

        self.ClearMatrix()
        for i in matrix:
            self.main_matrix[i[0][0]][i[0][1]] = i[1]


class DFSAlgo:
    def __init__(self, matrix: MapGenerator):
        self.used = {}
        self.parents = {}
        self.path = []
        self.map = matrix
        self.counter_for_doors = 1
        self.freq_of_doors = random.randrange(kMinFreqOfDoor, kMaxFreqOfDoor)

    def RandFreq(self):
        self.freq_of_doors = random.randrange(kMinFreqOfDoor, kMaxFreqOfDoor)

    def GetPath(self):
        return self.path

    def Clear(self):
        self.parents.clear()
        self.path.clear()
        self.used.clear()

    def DFS(self, vertex):
        test = self.map.GetAround(vertex)
        sign = False
        for i in self.map.GetAround(vertex):
            for j in i:
                if j not in [(-1, -1), vertex]:
                    if self.parents.get(vertex) != None:
                        if self.map.IsItWallForDoor(j):
                            if self.used.get((j[0], j[1] - 2)) != None or self.used.get(
                                    (j[0], j[1] + 2)) != None or self.used.get(
                                (j[0] - 2, j[1])) != None or self.used.get((j[0] + 2, j[1])) != None:
                                if (self.parents.get(vertex)[0] == j[0] or self.parents.get(vertex)[1] == j[1]):
                                    if self.counter_for_doors % self.freq_of_doors == 0:
                                        self.counter_for_doors = 1
                                        self.RandFreq()
                                        self.map.main_matrix[j[0]][j[1]] = kDoor
                                    self.counter_for_doors += 1
                    if j == self.parents.get((vertex)):
                        continue

                    if self.map.GetTile(j) not in [kEmpty, kBoardOfMap]:
                        sign = True
                        continue

                    if self.used.get(j) == True:
                        second_sign = False
                        for i in self.map.GetAroundForDFS(vertex, self.parents[vertex]):
                            if j in i:
                                second_sign = True
                                break
                        if second_sign:
                            continue
                        sign = True
                        continue
        if sign == True:
            return
        self.used[vertex] = True
        self.path.append(vertex)

        neighbours = self.map.GetNeighbours(vertex).copy()
        while len(neighbours) != 0:
            i = random.choice(neighbours)
            neighbours.remove(i)
            if self.used.get(i) == None and i != self.parents.get(vertex) and self.map.GetTile(i) not in [kBoardOfMap]:
                self.parents[i] = vertex
                self.DFS(i)

    def DFSforDeletingDeadEnds(self, vertex):
        self.used[vertex] = True
        self.path.append(vertex)

        for i in self.map.GetNeighbours(vertex):
            if self.used.get(i) == None and i != self.parents.get(vertex) and self.map.GetTile(i) in [kPath]:
                self.parents[i] = vertex
                self.DFSforDeletingDeadEnds(i)
        if self.parents.get(vertex) != None:
            if self.map.IsThereDeadEnd(vertex, self.parents.get(vertex)):
                self.map.main_matrix[vertex[0]][vertex[1]] = kEmpty

    def FinalDFS(self, vertex, final_matrix):
        self.used[vertex] = True
        self.path.append(vertex)
        final_matrix.append((vertex, self.map.GetTile(vertex)))

        for i in self.map.GetNeighbours(vertex):
            if self.used.get(i) == None and i != self.parents.get(vertex) and self.map.GetTile(i) not in [kEmpty,
                                                                                                          kBoardOfMap]:
                self.parents[i] = vertex
                self.FinalDFS(i, final_matrix)
