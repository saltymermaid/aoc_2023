symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+', '?', '_', '=', '<', '>', '/']


def is_number(n):
    is_num = True
    try:
        int(n)
    except ValueError:
        is_num = False
    return is_num


def get_next_part(row):
    end = 0
    for idx, char in enumerate(row):
        if is_number(char):
            end += 1
        else:
            return row[:end]
    return ''


def get_min_max(pos, engine):
    x, y = pos
    x1 = max(0, x - 1)
    x2 = min(x + 2, len(engine[0]))
    y1 = max(0, y - 1)
    y2 = min(y + 2, len(engine))
    return x1, x2, y1, y2


def check_around(pos, engine):
    x1, x2, y1, y2 = get_min_max(pos, engine)
    for row in range(y1, y2):
        for column in range(x1, x2):
            if engine[row][column] in symbols:
                return True
    return False


def check_parts(row_num, engine):
    row = engine[row_num]
    parts_in_row = 0
    for idx, char in enumerate(row):
        if is_number(char) and (idx == 0 or not is_number(row[idx - 1])):
            part = get_next_part(row[idx:])
            part_valid = False
            for i in range(len(part)):
                if check_around((idx + i, row_num), engine):
                    part_valid = True
            if part_valid:
                parts_in_row += int(part)
    return parts_in_row


if __name__ == "__main__":
    with open('advent3_data.txt') as f:
        test_data = f.readlines()

    total = 0
    for row_number, engine_row in enumerate(test_data):
        total += check_parts(row_number, test_data)

    print(total)
