from advent2 import *


def get_power(game_data: [int, list]) -> int:
    cube_sets = game_data[1]
    max_counts = {'blue': 0, 'green': 0, 'red': 0}

    for cube_set in cube_sets:
        for color in max_counts.keys():
            max_counts[color] = max(max_counts[color], cube_set.get(color, 0))

    return max_counts['blue'] * max_counts['green'] * max_counts['red']


if __name__ == "__main__":
    with open('advent2_data.txt') as f:
        total = sum(get_power(parse_game(game)) for game in f)

    print(total)
