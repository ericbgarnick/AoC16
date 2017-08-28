from collections import deque
from typing import Iterable

from trap_floor import FloorTile


class SlidingTrapFloor:
    def __init__(self, first_row: str, num_rows: int):
        self.tile_row = self.decode_first_row(first_row)
        self.total_safe = self._count_safe_tiles(list(self.tile_row)[1:])
        self.tiles_seen = len(list(self.tile_row)[1:])
        self.num_rows = num_rows

    # Setup first row
    def decode_first_row(self, row_code: str) -> deque:
        return self._insert_dummy_tile(
            deque(FloorTile(self._value_is_safe(code_value))
                  for code_value in row_code))

    @staticmethod
    def _value_is_safe(code_value: str):
        if code_value == '.':
            return True
        elif code_value == '^':
            return False
        else:
            raise Exception("Unknown code value: {}".format(code_value))

    @staticmethod
    def _insert_dummy_tile(floor_deque: deque):
        floor_deque.appendleft(FloorTile(True))
        return floor_deque

    @staticmethod
    def _count_safe_tiles(floor_tile_row: Iterable[FloorTile]):
        return sum(1 for tile in floor_tile_row if tile.is_safe)

    # Create trap floor
    def create_trap_floor(self):
        while not self.floor_is_finished():
            self.add_next_tile()

    def add_next_tile(self):
        new_tile = FloorTile(self.current_tile_is_safe())
        self.total_safe += int(new_tile.is_safe)
        self.tile_row.append(new_tile)
        self.tiles_seen += 1
        self.tile_row.popleft()

    def floor_is_finished(self):
        return self.tiles_seen == (len(self.tile_row) - 1) * self.num_rows

    def current_tile_is_safe(self):
        return (self.previous_row_left_is_safe() ==
                self.previous_row_right_is_safe())

    def previous_row_left_is_safe(self):
        return self.tiles_seen % (len(self.tile_row) - 1) == 0 or \
               self.tile_row[0].is_safe

    def previous_row_right_is_safe(self):
        return (self.tiles_seen + 1) % (len(self.tile_row) - 1) == 0 or \
               self.tile_row[2].is_safe
