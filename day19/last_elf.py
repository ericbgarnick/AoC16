from sys import argv


def last_power_of_two(query_number: int) -> int:
    power_of_two = 2
    while power_of_two * 2 <= query_number:
        power_of_two *= 2
    return power_of_two


def last_elf_number(number_of_elves: int) -> int:
    return (number_of_elves - last_power_of_two(number_of_elves)) * 2 + 1


if __name__ == '__main__':
    if len(argv) != 2:
        print("Must enter a query number as the command line argument")
    else:
        print("Lucky else is number {}".format(last_elf_number(int(argv[1]))))
