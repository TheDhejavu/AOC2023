import sys
import os
import re
symbols = ["!", "#", "$", "%", "&", "*", "(", ")", "+", "-", "/", ":", ";", "<", "=", ">", "?", "@", "[", "]", "^", "_", "", "{", "|", "}", "~"]
resp = []
def is_within_range(index, values, memo , curr_idx):
   result = 0
   for key,value in values.copy().items():
      if key.isdigit():
        len_of_key = len(key)
        start = value
        end = start + len_of_key + 1
        if index >= start and index <= end:
            resp.append(key)
            result += int(key)
            # del memo[curr_idx][key]

   return result
    
      
def gear_ratios1(schematic):
    memo = [{} for _ in schematic]
    sum_of_engine_schematic = 0
    # print(schematic)
    i = 0
    while i < len(schematic):
        value = schematic[i]
        index = 0
        while index < len(value):
            char_or_symbol = value[index]
            if char_or_symbol.isdigit():
                number = re.findall(r"\d+", value[index:])[0]
                memo[i][number] = index -1 
                index += len(str(number))
            else:
                if char_or_symbol in symbols:
                    # print(char_or_symbol, index)
                    sym_key = f"{index}:{char_or_symbol}"
                    memo[i][sym_key] = index
                index += 1

        i += 1
    index = 0
    print(memo)
    while index < len(memo):
        current = memo[index]
        # print(current)
        for sym_key, value in current.copy().items():
            if ":" in sym_key:
                key = sym_key.split(":")[1]
                if key in symbols:
                    top_index = index - 1
                    bottom_index = index + 1
                    # check top list here 
                    if top_index >= 0:
                        top = memo[top_index]
                        sum_of_engine_schematic += is_within_range(value, top, memo, top_index)

                    # check bottom list here 
                    if bottom_index < len(memo):
                        bottom = memo[bottom_index]
                        sum_of_engine_schematic += is_within_range(value, bottom, memo, bottom_index)

                    # check current list here 
                    sum_of_engine_schematic += is_within_range(value, current, memo, index)

        index += 1


          
    # print(resp)
    return sum_of_engine_schematic


if __name__ == "__main__":
  for path in sys.argv[1:]:
    with open(path) as file: 
      v = file.read().splitlines()
      print('Part 1: Gear Ratios: ', gear_ratios1(v))