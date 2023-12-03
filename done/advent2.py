bag = {
    'red': 12,
    'green': 13,
    'blue': 14
}


def parse_game(game_string: str) -> [int, list]:
    game_num, cube_sets = game_string.split(':')
    game_num = int(game_num.split()[1])
    all_draws = [
        {color: int(num) for num, color in
         (cube_set.strip().split()[:2] for cube_set in cubes.split(','))}
        for cubes in cube_sets.split(';')
    ]
    return [game_num, all_draws]


def check_cubes(game_data: [int, list]) -> int:
    for draw in game_data[1]:
        for color, count in draw.items():
            if count > bag[color]:
                return 0
    return game_data[0]


if __name__ == "__main__":
    with open('advent2_data.txt') as f:
        total = sum(check_cubes(parse_game(game)) for game in f)

    print(total)
