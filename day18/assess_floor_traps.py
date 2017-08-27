from sys import argv

from sliding_trap_floor import SlidingTrapFloor
from trap_floor import TrapFloor

if __name__ == '__main__':
    if len(argv) != 3:
        print("Enter first row data followed by the number of rows for the floor")
    else:
        # trap_floor = TrapFloor(argv[1], int(argv[2]))
        # trap_floor.build_full_floor_map()
        # print(trap_floor)
        # print("This floor plan has {} safe tiles".format(
        #     sum([1 for tile in trap_floor.floor_tiles if tile.is_safe])))
        # trap_floor.build_sliding_floor_map()
        # print("This floor plan has {} safe tiles".format(trap_floor.total_safe_tiles))

        trap_floor = SlidingTrapFloor(argv[1], int(argv[2]))
        trap_floor.create_trap_floor()
        print("Total safe tiles: {}".format(trap_floor.total_safe))
