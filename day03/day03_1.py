import sys

def is_valid_symbol(char):
    return not (char.isdigit() or char == '.')

def extract_coordinates(schematic):
    mapping = {}
    height = len(schematic)
    width = len(schematic[0])
    tag = 0

    for y in range(height):
        visited = set()
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
                        visited.add(x)
                        digits.append(v)
                        x_x += 1
                    else:
                        break

                full_digits = "".join(digits)

                for i, _ in enumerate(full_digits):
                    if (x + i, y) not in mapping:
                        mapping[(x + i, y)] = {"value": full_digits, "tag": tag}

                if (x, y) not in mapping:
                    mapping[(x, y)] = {"value": full_digits, "tag": tag}
            elif c == ".":
                mapping[(x, y)] = {"value": ".", "tag": tag}
            else:
                mapping[(x, y)] = {"value": c, "tag": tag}
            tag += 1

    return mapping

def gear_ratios(schematic):
    sum_of_engine_schematic = 0
    adjacent_neighbors = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1), (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]

    mapping = extract_coordinates(schematic)
    visited_set = set()

    height = len(schematic)
    width = len(schematic[0])
    for y in range(height):
        for x in range(width):
            if (x, y) in mapping:
                symbol = mapping[(x, y)]

                if symbol["value"].isdigit() and symbol["tag"] not in visited_set:
                    adjacent = any(
                      is_valid_symbol(mapping.get((x + dx, y + dy), {}).get("value", ""))
                      for dx, dy in adjacent_neighbors
                      if 0 <= x + dx < width and 0 <= y + dy < height
                    )

                    if adjacent:
                        sum_of_engine_schematic += int(symbol["value"])
                        visited_set.add(symbol["tag"])

    return sum_of_engine_schematic

if __name__ == "__main__":
    for path in sys.argv[1:]:
        with open(path) as file:
            v = file.read().splitlines()
            print('Part 1: Gear Ratios:', gear_ratios(v))
