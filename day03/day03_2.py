import sys

def is_valid_symbol(char):
  return not (char.isdigit() or char == '.')

def extract_cordinates(schematic):
    mapping = {}
    
    height = len(schematic)
    width = len(schematic[0])
    tag = 0
    for y in range(height):
      visited = []
      for x in range(width):
        if x in visited:
          continue

        c = schematic[y][x]
        if c.isdigit():
          x_x = x + 1
          digits = [c]
          while x_x < width:
            v = schematic[y][x_x]
            if v.isdigit():
              visited.append(x)
              digits.append(v)
              x_x += 1
            else:
              break
              
          full_digits = "".join(digits)

          for (i, _) in enumerate(full_digits):
            
            if (x + i, y) not in mapping:
              mapping[(x + i, y)] =  {"value": full_digits ,"tag": tag}
          
          if (x, y) not in mapping:
            mapping[(x, y)] =  {"value": full_digits ,"tag": tag}
        elif c == ".":
          mapping[(x, y)] =  {"value": "." ,"tag": tag}
        else:
          mapping[(x, y)] =  {"value": c ,"tag": tag}
        tag += 1

    # print(mapping)
    
    return mapping
def gear_ratios2(schematic):
    memo = [{} for _ in schematic]
    sum_of_engine_schematic = 0
    adjacent_neighbors = [
        (-1, -1), # Top-left
        (-1, 0),  # Up
        (-1, 1),  # Top-right
        (0, -1),  # Left
        (0, 1),   # Right
        (1, -1),  # Bottom-left
        (1, 0),   # Down
        (1, 1)    # Bottom-right
    ]

    mapping = extract_cordinates(schematic)
    visited = []
    height = len(schematic)
    width = len(schematic[0])
    memo = {}
    for y in range(height):
      for x in range(width):
        if (x, y) in mapping:
          symbol = mapping[(x, y)]

          if symbol["value"].isdigit():
            if symbol["tag"] in visited:
              continue
            
            for dx, dy in adjacent_neighbors:
              nx, ny = x + dx, y + dy  # Calculate the coordinates of the neighbor
              if nx < 0 or ny < 0:
                continue
              
              if nx >= width or ny >= height:
                continue
              
              result = mapping[(nx, ny)]
              v = result["value"]
              if v == "*":
                if (nx, ny) in memo:
                  sum_of_engine_schematic += int(symbol["value"]) * int(memo[(nx, ny)])
                else:
                   memo[(nx, ny)] = symbol["value"]

                visited.append(symbol["tag"])
                break

    return sum_of_engine_schematic


if __name__ == "__main__":
  for path in sys.argv[1:]:
    with open(path) as file: 
      v = file.read().splitlines()
      print('Part 2: Gear Ratios: ', gear_ratios2(v))