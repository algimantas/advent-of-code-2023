limit = {'red': 12, 'green': 13, 'blue': 14}

def parse_games(lines):
    games = {}
    for line in lines:
        [game_title, game_info] = line.split(":", 1)
        game_num = int(game_title.split(" ", 1)[1])
        draws_str = game_info.split(";")
        draws = []
        for draw_str in draws_str:
            cubes_str = draw_str.split(",")
            draw = {'red': 0, 'green': 0, 'blue': 0}
            for cube_str in cubes_str:
                [count, color] = cube_str.strip().split(" ")
                draw[color] = int(count)
            draws.append(draw)
        games[game_num] = draws
    return games

def is_possible(draws):
    for draw in draws:
        if draw['red'] > limit['red'] or draw['green'] > limit['green'] or draw['blue'] > limit['blue']:
            return False
    return True

def possible_games(games):
    result = 0
    for game_num, draws in games.items():
        if is_possible(draws):
            result += game_num
    return result

# main

with open('input.txt', 'r') as file:
    lines = file.readlines()

games = parse_games(lines)
possible = possible_games(games)

print(possible)