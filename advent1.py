with open('advent1_data.txt') as f:
    test_data = f.readlines()


def is_number(n):
    is_num = True
    try:
        int(n)
    except ValueError:
        is_num = False
    return is_num


def get_first_num(cal_val):
    for char in cal_val:
        if is_number(char):
            return int(char)


def get_last_num(cal_val):
    for char in reversed(cal_val):
        if is_number(char):
            return int(char)


if __name__ == "__main__":
    total = 0

    for cv in test_data:
        first_num = get_first_num(cv)
        last_num = get_last_num(cv)
        total += ((first_num * 10) + last_num)

    print(total)