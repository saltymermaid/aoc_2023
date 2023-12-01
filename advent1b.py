from advent1 import *

with open('advent1_data.txt') as f:
    test_data = f.readlines()

digits = [
    'zero',
    'one',
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eight',
    'nine'
]


def get_word_num(num_str, direction):
    for i, digit in enumerate(digits):
        num_len = len(digit)
        candidate = num_str[:num_len]
        if candidate[::direction] == digit:
            return i
    return None


def get_num(cal_val, direction):
    values = cal_val[::direction]
    for i, char in enumerate(values):
        if is_number(char):
            return int(char)
        word_num = get_word_num(values[i:], direction)
        if word_num:
            return word_num


if __name__ == "__main__":
    total = 0

    for cv in test_data:
        first_num = get_num(cv, 1)
        last_num = get_num(cv, -1)
        total += ((first_num * 10) + last_num)

    print(total)