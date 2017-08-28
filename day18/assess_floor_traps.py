from sys import argv

from sliding_trap_floor import SlidingTrapFloor

if __name__ == '__main__':
    if len(argv) != 3:
        print("Enter first row data followed by the number of rows for the floor")
    else:
        trap_floor = SlidingTrapFloor(argv[1], int(argv[2]))
        trap_floor.create_trap_floor()
        print("Total safe tiles: {}".format(trap_floor.total_safe))
