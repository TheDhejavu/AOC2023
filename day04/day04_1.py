import sys


def scratch_cards(cards):
  total_points = 0
  for card in cards:
    numbers = card.split("|")
    winning_numbers = "".join(numbers[0]).split(":")[1]
    winning_numbers = winning_numbers.split(" ")
    haves  = "".join(numbers[1]).split(" ")
    points = 0
    for num in haves:
     if num in winning_numbers and num != '':
        if points == 0:
          points += 1
        else:
          points += points
    total_points += points

  return total_points

if __name__ == "__main__":
  for path in sys.argv[1:]:
    with open(path) as file: 
      v = file.read().splitlines()
      print('Day 4: Scratchcards ', scratch_cards(v))