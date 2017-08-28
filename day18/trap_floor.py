from collections import deque
from typing import List


class FloorTile:
    def __init__(self, is_safe: bool):
        self.is_safe = is_safe

    def __eq__(self, other):
        return self.is_safe == other.is_safe

    def __repr__(self):
        return '.' if self.is_safe else '^'


class TrapFloor:
    def __init__(self, first_row: str, num_rows: int):
        self.floor_tiles = self.decode_first_row(first_row)
        self.width = len(self.floor_tiles)
        self.num_rows = num_rows
        self.total_safe_tiles = self.count_safe_tiles(self.floor_tiles)
        print("TOTAL SAFE TILES:", self.total_safe_tiles)

    def __repr__(self):
        split_rows = []
        for i in range(0, len(self.floor_tiles), self.width):
            split_rows.append(' '.join([str(tile) for tile in
                                        self.floor_tiles[i: i + self.width]]))
        return '\n'.join(split_rows)

    # Setup first row
    def decode_first_row(self, row_code: str) -> List[FloorTile]:
        return [FloorTile(self.value_is_safe(code_value)) for
                code_value in row_code]

    @staticmethod
    def value_is_safe(code_value: str):
        if code_value == '.':
            return True
        elif code_value == '^':
            return False
        else:
            raise Exception("Unknown code value: {}".format(code_value))

    @staticmethod
    def count_safe_tiles(floor_tile_row: List[FloorTile]):
        return sum(1 for tile in floor_tile_row if tile.is_safe)

    # Build floor map main methods
    def build_full_floor_map(self):
        while len(self.floor_tiles) < self.floor_size():
            self.floor_tiles.append(FloorTile(self.current_tile_is_safe()))

    def build_sliding_floor_map(self):
        num_tiles_seen = len(self.floor_tiles)
        tile_queue = deque(self.floor_tiles)

        self.add_tile_sliding(tile_queue, num_tiles_seen)
        num_tiles_seen += 1

        while num_tiles_seen < self.floor_size():
            self.add_tile_sliding(tile_queue, num_tiles_seen)
            num_tiles_seen += 1
            tile_queue.popleft()

    # Build floor map helpers
    def add_tile_sliding(self, tile_queue: deque, num_tiles_seen: int):
        print("Sliding floor size: {}".format(len(tile_queue)))
        new_tile = FloorTile(self.current_tile_is_safe(num_tiles_seen))
        tile_queue.append(new_tile)
        if new_tile.is_safe:
            self.total_safe_tiles += 1

    def floor_size(self):
        return self.width * self.num_rows

    def current_tile_is_safe(self, current_index: int=None):
        if current_index is None:
            current_index = self.current_tile_index()
            sliding_builder = False
        else:
            sliding_builder = True
        safety = (self.previous_row_left_is_safe(current_index, sliding_builder) ==
                self.previous_row_right_is_safe(current_index, sliding_builder))
        print("Tile is safe: {}".format(safety))
        return safety

    def current_tile_index(self):
        return len(self.floor_tiles)

    def previous_row_left_is_safe(self, tile_index: int,
                                  sliding_builder: bool=False) -> bool:
        if self.is_next_to_left_wall(tile_index):
            return True
        else:
            prev_row_left_index = 0 if sliding_builder else tile_index - self.width - 1
            return self.floor_tiles[prev_row_left_index].is_safe

    def previous_row_right_is_safe(self, tile_index: int,
                                   sliding_builder: bool=False) -> bool:
        if self.is_next_to_right_wall(tile_index):
            return True
        else:
            prev_row_right_index = 2 if sliding_builder else tile_index - self.width + 1
            return self.floor_tiles[prev_row_right_index].is_safe

    def is_next_to_left_wall(self, tile_index: int):
        return tile_index % self.width == 0

    def is_next_to_right_wall(self, tile_index: int):
        return (tile_index + 1) % self.width == 0
