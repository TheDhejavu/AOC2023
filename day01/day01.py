import os
import sys

NUMBER_WORDS = {
    'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7,
    'eight': 8, 'nine': 9, 'ten': 10, 'eleven': 11, 'twelve': 12, 'thirteen': 13,
    'fourteen': 14, 'fifteen': 15, 'sixteen': 16, 'seventeen': 17, 'eighteen': 18,
    'nineteen': 19, 'twenty': 20, 'thirty': 30, 'forty': 40, 'fifty': 50, 'sixty': 60,
    'seventy': 70, 'eighty': 80, 'ninety': 90, 'hundred': 100, 'thousand': 1000,
    'million': 1000000,
}

def extract_digits(value):
    new_chars = ""
    n = len(value)

    for i in range(n):
        j = i
        while j < n:
            current_v = value[i:j + 1]
            if current_v in NUMBER_WORDS:
                new_chars += str(NUMBER_WORDS[current_v])
            elif current_v.isdigit():
                new_chars += str(current_v)
            j += 1

    return [char for char in new_chars if char.isdigit()]

def sum_of_calibration_values(values):
    results = []

    for value in values:
        digits = extract_digits(value)

        if len(digits) == 1:
            result = int(digits[0] + digits[0])
        elif len(digits) >= 2:
            result = int(digits[0] + digits[-1])
        else:
            result = None

        results.append(result)

    total_sum = sum(result for result in results if result is not None)

    return total_sum

if __name__ == "__main__":
    for path in sys.argv[1:]:
        with open(path) as file:
            v = file.read().splitlines()
            print('Sum Of Calibration', sum_of_calibration_values(v))
