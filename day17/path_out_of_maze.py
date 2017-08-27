from collections import deque
from sys import argv
from typing import Optional

from roommaze import Room, Direction, RoomMaze


def add_rooms_to_explore(current_room: Room, to_explore: deque) -> deque:
    for direction in Direction:
        if current_room.door_is_open(direction):
            extended_path = current_room.code_with_current_path + direction.name[0]
            to_explore.append(Room(current_room.maze, extended_path))
    return to_explore


# Shortest path search
def get_next_room_short_path(rooms_queue: deque) -> Room:
    if not len(rooms_queue):
        raise Exception("This maze is impossible to escape!")
    return rooms_queue.popleft()


def shortest_path_out_of_maze(rooms_to_explore: deque) -> str:
    """Returns the path out of the maze as a series of steps (U, D, L, R)
    for 'up', 'down', 'left', right'.  Path is determined using breadth-first
    search."""
    current_room = get_next_room_short_path(rooms_to_explore)
    while not current_room.is_final_room():
        rooms_to_explore = add_rooms_to_explore(current_room, rooms_to_explore)
        current_room = get_next_room_short_path(rooms_to_explore)
    return current_room.current_path()


# Longest path search
def get_next_room_long_path(rooms_queue: deque) -> Optional[Room]:
    if len(rooms_queue):
        return rooms_queue.popleft()
    else:
        return None


def longest_path_out_of_maze(rooms_to_explore: deque) -> str:
    longest_path = ""
    current_room = get_next_room_long_path(rooms_to_explore)
    while current_room is not None:
        if current_room.is_final_room():
            longest_path = current_room.current_path()
            current_room = get_next_room_long_path(rooms_to_explore)
        else:
            rooms_to_explore = add_rooms_to_explore(current_room, rooms_to_explore)
            current_room = get_next_room_long_path(rooms_to_explore)
    return longest_path


if __name__ == '__main__':
    if len(argv) != 3:
        print("Please enter starting passcode as argument 1, path-type as argument 2 (short/long)")
    else:
        maze = RoomMaze(4, 4)
        start_room = Room(maze, argv[1])
        road_map = deque()
        road_map.append(start_room)
        if argv[2] == 'short':
            print("Shortest path out of the maze: {}"
                  .format(shortest_path_out_of_maze(road_map)))
        elif argv[2] == 'long':
            final_longest_path = longest_path_out_of_maze(road_map)
            print("Longest path out of the maze: {}\nLongest path length: {}"
                  .format(final_longest_path, len(final_longest_path)))
        else:
            print("Unknwon path-type: {}".format(argv[2]))
