from advent3 import *


def get_row_gears(row):
    return [idx for idx, gear in enumerate(row) if gear == '*']


def get_whole_part(pos, row):
    x, y = pos
    start = end = y
    while start > 0 and is_number(row[start - 1]):
        start -= 1
    while end < len(row) and is_number(row[end + 1]):
        end += 1
    whole_part = ''.join(row[start:end + 1])
    return whole_part


def get_gear_parts(pos, engine):
    part_set = set()
    x1, x2, y1, y2 = get_adjacent_indices(pos, engine)
    for row in range(y1, y2):
        for column in range(x1, x2):
            if is_number(engine[row][column]):
                part_set.add(get_whole_part((row, column), engine[row]))
    parts = [int(p) for p in part_set]
    return parts


if __name__ == "__main__":
    with open('advent3_data.txt') as f:
        test_data = f.readlines()

    total = 0
    valid_gears = []
    for row_num, engine_row in enumerate(test_data):
        row_gears = get_row_gears(engine_row)
        for row_gear in row_gears:
            gear_parts = get_gear_parts((row_gear, row_num), test_data)
            if len(gear_parts) == 2:
                valid_gears.append((row_gear, row_num))
                total += gear_parts[0] * gear_parts[1]

    print(total)
