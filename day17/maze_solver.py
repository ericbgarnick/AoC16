from abc import ABC, abstractmethod
from collections import deque
from typing import Optional

from roommaze import Room, Direction


class MazeSolver(ABC):
    @abstractmethod
    def path_out_of_maze(self, start_room: Room) -> str:
        pass

    @abstractmethod
    def get_next_room(self, rooms_queue: deque) -> Optional[Room]:
        pass

    @staticmethod
    def add_rooms_to_explore(current_room: Room, to_explore: deque) -> deque:
        for direction in Direction:
            if current_room.door_is_open(direction):
                extended_path = current_room.code_with_current_path + direction.name[0]
                to_explore.append(Room(current_room.maze, extended_path))
        return to_explore




