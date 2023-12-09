import os
import sys

contained_in_games = {
  "blue": 14,
  "green": 13,
  "red": 12,
}


# Let start with brute force approach
def cube_conundrum_part1(games):
  sum_of_ids = 0
  # O(N^3) 
  for game in games:
    game_sets = game.split(":")
    current_game = game_sets[0]
    current_game_id = int(current_game.split(" ")[1])
  
    game_sets = "".join(game_sets[1:]).split(";")

    not_possible = False
    for game_set in game_sets:
      exact_game = game_set.split(" ")[1:]
      i = 0
      while i < len(exact_game): 
        cube_color_count = int(exact_game[i])
        cube_color = exact_game[i+1].replace(',', '')
        if cube_color in contained_in_games:
            if cube_color_count > contained_in_games[cube_color]:
              not_possible = True
              break
        i += 2

        if not_possible:
          break
      
      if not_possible:
        break

    if not_possible:
      continue

    sum_of_ids += current_game_id

  return sum_of_ids

if __name__ == "__main__":
  for path in sys.argv[1:]:
    with open(path) as file:
      v = file.read().splitlines()
      print('Part 1: Cube Conundrum: ', cube_conundrum_part1(v))
