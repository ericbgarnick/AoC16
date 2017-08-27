from hashlib import md5
from enum import Enum
from typing import Tuple


class Direction(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3


class RoomMaze:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height


class Room:
    LOCKED_VALUES = '0123456789a'
    UNLOCKED_VALUES = 'bcdef'

    def __init__(self, maze: RoomMaze, code_with_path: str):
        self.maze = maze
        self.code_with_current_path = code_with_path

    def passcode(self) -> str:
        passcode_len = 0
        for element in self.code_with_current_path:
            if element in 'UDLR':
                return self.code_with_current_path[:passcode_len]
            else:
                passcode_len += 1
        return self.code_with_current_path

    def current_path(self) -> str:
        return self.code_with_current_path[len(self.passcode()):]

    def is_final_room(self) -> bool:
        return self.get_coords_from_path() == (self.maze.width - 1,
                                               self.maze.height - 1)

    def door_is_open(self, direction: Direction) -> bool:
        return not (self.is_wall(direction) or self.is_locked(direction))

    def is_wall(self, direction: Direction) -> bool:
        room_coords = self.get_coords_from_path()
        if direction == Direction.LEFT:
            return room_coords[0] == 0
        elif direction == Direction.RIGHT:
            return room_coords[0] == self.maze.width - 1
        elif direction == Direction.UP:
            return room_coords[1] == 0
        elif direction == Direction.DOWN:
            return room_coords[1] == self.maze.height - 1

    def get_coords_from_path(self) -> Tuple[int, int]:
        x_coord = self.code_with_current_path.count('R') - self.code_with_current_path.count('L')
        y_coord = self.code_with_current_path.count('D') - self.code_with_current_path.count('U')
        return x_coord, y_coord

    def is_locked(self, direction: Direction):
        code_for_direction = self.get_up_down_left_right_codes()[direction.value]
        return self.is_locked_value(code_for_direction)

    def get_up_down_left_right_codes(self) -> str:
        return md5(self.code_with_current_path.encode()).hexdigest()[:len(Direction)]

    def is_locked_value(self, value: str) -> bool:
        if value in self.LOCKED_VALUES:
            return True
        elif value in self.UNLOCKED_VALUES:
            return False
        else:
            raise Exception("Invalid locked value {}".format(value))
