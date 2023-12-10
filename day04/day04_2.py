import sys
def scratch_cards(cards):
  memo = {i: 1 for i in range(1, len(cards) + 1)}

  for card_num, card in enumerate(cards, 1):
    numbers = card.split("|")
    winning_numbers = "".join(numbers[0]).split(":")[1]
    winning_numbers = set(winning_numbers.split(" "))
    haves  = set("".join(numbers[1]).split(" "))

    overlapping_numbers = haves.intersection(winning_numbers)
    non_empty_overlapping_numbers = [num for num in overlapping_numbers if num != '']
    total_overlapping_numbers =  card_num + len(non_empty_overlapping_numbers)
  
    for matching in range(card_num+1, total_overlapping_numbers+1):
        memo[matching] += memo[card_num]
    
  return sum(memo.values())

if __name__ == "__main__":
  for path in sys.argv[1:]:
    with open(path) as file: 
      v = file.read().splitlines()
      print('Day 4: Scratchcards ', scratch_cards(v))