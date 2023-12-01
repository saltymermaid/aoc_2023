with open('advent1_data.txt') as f:
    test_data = f.readlines()


def is_number(n):
    is_num = True
    try:
        int(n)
    except ValueError:
        is_num = False
    return is_num


def get_num(cal_val, direction):
    values = cal_val[::direction]
    for char in values:
        if is_number(char):
            return int(char)


if __name__ == "__main__":
    total = 0

    for cv in test_data:
        first_num = get_num(cv, 1)
        last_num = get_num(cv, -1)
        total += ((first_num * 10) + last_num)

    print(total)