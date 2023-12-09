import os
import sys

contained_in_games = {
  "blue": 14,
  "green": 13,
  "red": 12,
}

# Let start with brute force approach
def cube_conundrum_part2(games):
  # O(N^3) 
  games_tracker = {}
  for game in games:
    game_sets = game.split(":")   
    current_game_id = game_sets[0].split(" ")[1]
    game_sets = "".join(game_sets[1:]).split(";")
    cube_tracker = {}
    
    for game_set in game_sets:
      exact_game = game_set.split(" ")[1:]
     
      i = 0
      while i < len(exact_game): 
        cube_color_count = int(exact_game[i])
        cube_color = exact_game[i+1].replace(',', '')
        if cube_color in cube_tracker:
          if cube_color_count > cube_tracker[cube_color]:
            cube_tracker[cube_color] = cube_color_count
        else:
          cube_tracker[cube_color] = cube_color_count
        i += 2

    power_of_cubes = None

    for cube_color in cube_tracker:
      if power_of_cubes == None:
        power_of_cubes = cube_tracker[cube_color]
      else:
        power_of_cubes = power_of_cubes * cube_tracker[cube_color]

    games_tracker[current_game_id] = power_of_cubes

  sum_of_games = None

  for game_id in games_tracker:
    if sum_of_games == None:
      sum_of_games = games_tracker[game_id]
    else:
      sum_of_games = sum_of_games + games_tracker[game_id]

  return sum_of_games


if __name__ == "__main__":
  for path in sys.argv[1:]:
    with open(path) as file:
      v = file.read().splitlines()
      print('Part 2: Cube Conundrum: ', cube_conundrum_part2(v))
