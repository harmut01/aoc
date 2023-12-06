from re import findall

word_to_number = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    'ten': 10,
}

def get_digits(line):
    pattern = f"(\d|one|two|three|four|five|six|seven|eight|nine|ten)"
    m = findall(fr'(?={pattern})', line)
    return [word_to_number[m] if m in word_to_number else int(m)  for m in m]

def get_input(path):
    with open(path, "r") as f:
        return f.readlines()

