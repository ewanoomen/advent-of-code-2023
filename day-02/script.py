def input_as_dict():
    with open("input.txt") as input:
        games = {}
        for line in input.readlines():
            line = line.replace("Game ", "")
            game_id = line.split(":")[0]
            line = line.split(":")[1]
            cubes = []
            for round in line.split(";"):
                rounds = {}
                for color in round.split(","):
                    color_amount = color.split(" ")
                    rounds[color_amount[2].replace("\n", "")] = color_amount[1]
                cubes.append(rounds)
            games[game_id] = cubes
    return games

# part 1
# possible_games = []

# for game, cubes in input_as_dict().items():
#     possible = True

#     for round in cubes:
#         if int(round.get("red", 0)) > 12: possible = False
#         if int(round.get("green", 0)) > 13: possible = False
#         if int(round.get("blue", 0)) > 14: possible = False

#     if possible: possible_games.append(int(game))

# print(possible_games)
# print(sum(possible_games))

# part 2
total_power = []

for game, cubes in input_as_dict().items():
    color_amounts = {
        "red": [],
        "green": [],
        "blue": []
    }
    for round in cubes:
        if round.get("red"): color_amounts["red"].append(int(round.get("red")))
        if round.get("green"): color_amounts["green"].append(int(round.get("green")))
        if round.get("blue"): color_amounts["blue"].append(int(round.get("blue")))

    power = max(color_amounts["red"]) * max(color_amounts["green"]) * max(color_amounts["blue"])

    total_power.append(power)

print(total_power)
print(sum(total_power))
