import unittest

from sliding_trap_floor import SlidingTrapFloor
from trap_floor import FloorTile


class TestSlidingTrapFloor(unittest.TestCase):
    def test_init_trap_floor_first_row(self):
        test_row_code = ".^.."
        test_floor_rows = 2
        trap_floor = SlidingTrapFloor(".^..", 2)

        # Test length and content of first row
        expected_first_row = [FloorTile(True), FloorTile(True), FloorTile(False),
                              FloorTile(True), FloorTile(True)]
        self.assertEqual(len(trap_floor.tile_row), len(expected_first_row))
        for tile_idx in range(len(expected_first_row)):
            current_expected_tile = expected_first_row[tile_idx]
            current_actual_tile = trap_floor.tile_row[tile_idx]
            self.assertEqual(current_actual_tile, current_expected_tile)

        # Test count of safe tiles in first row
        self.assertEqual(trap_floor.total_safe, test_row_code.count('.'))

        # Test number of tiles seen count
        self.assertEqual(trap_floor.tiles_seen, len(test_row_code))

        # Test num_rows set correctly
        self.assertEqual(trap_floor.num_rows, test_floor_rows)

    def test_previous_row_left_is_safe(self):
        # First tile in row, previous row starts safe
        trap_floor = SlidingTrapFloor(".^..", 2)
        self.assertTrue(trap_floor.previous_row_left_is_safe())

        # First tile in row, previous row starts trap
        trap_floor = SlidingTrapFloor("^^..", 2)
        self.assertTrue(trap_floor.previous_row_left_is_safe())

        # Second tile in row, tile is safe
        trap_floor = SlidingTrapFloor(".^..", 2)
        # Move forward one tile
        trap_floor.tile_row.append(FloorTile(True))
        trap_floor.tile_row.popleft()
        self.assertTrue(trap_floor.previous_row_left_is_safe())

        # Second tile in row, tile is safe
        trap_floor = SlidingTrapFloor(".^..", 2)
        # Move forward one tile
        trap_floor.tile_row.append(FloorTile(True))
        trap_floor.tile_row.popleft()
        trap_floor.tiles_seen += 1
        self.assertTrue(trap_floor.previous_row_left_is_safe())

        # Second tile in row, tile is trap
        trap_floor = SlidingTrapFloor("^^..", 2)
        # Move forward one tile
        trap_floor.tile_row.append(FloorTile(True))
        trap_floor.tile_row.popleft()
        trap_floor.tiles_seen += 1
        self.assertFalse(trap_floor.previous_row_left_is_safe())

    def test_previous_row_right_is_safe(self):
        # Last tile in row, previous row ends safe
        trap_floor = SlidingTrapFloor(".^^.", 2)
        # Move forward three tiles
        for _ in range(3):
            trap_floor.tile_row.append(FloorTile(True))
            trap_floor.tile_row.popleft()
            trap_floor.tiles_seen += 1
        self.assertTrue(trap_floor.previous_row_right_is_safe())

        # Last tile in row, previous row ends trap
        trap_floor = SlidingTrapFloor(".^^^", 2)
        # Move forward three tiles
        for _ in range(3):
            trap_floor.tile_row.append(FloorTile(True))
            trap_floor.tile_row.popleft()
            trap_floor.tiles_seen += 1
        self.assertTrue(trap_floor.previous_row_right_is_safe())

        # Second-to-last tile in row, previous row tile is safe
        trap_floor = SlidingTrapFloor(".^^.", 2)
        # Move forward three tiles
        for _ in range(2):
            trap_floor.tile_row.append(FloorTile(True))
            trap_floor.tile_row.popleft()
            trap_floor.tiles_seen += 1
        self.assertTrue(trap_floor.previous_row_right_is_safe())

        # Second-to-last tile in row, previous row tile is trap
        trap_floor = SlidingTrapFloor(".^^^", 2)
        # Move forward three tiles
        for _ in range(2):
            trap_floor.tile_row.append(FloorTile(True))
            trap_floor.tile_row.popleft()
            trap_floor.tiles_seen += 1
        self.assertFalse(trap_floor.previous_row_right_is_safe())


if __name__ == '__main__':
    unittest.main()
