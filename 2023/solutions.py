from helpers import get_input
from helpers import *
import re

from aocd import data

def day1(data):
    sum = 0
    for line in data:
        ints = get_digits(line)
        sum += ints[0]*10 + ints[-1]
    print(sum)

def day(data):
    sum_ids = 0
    max = {"red": 12, "green": 13, "blue": 14 }
    for line in data:
        pattern = r"(\d+)\s+(\w+)"
        m = findall(pattern, line)
        print(list(filter(lambda t: int(t[0]) > max[t[1]], m)))
        if not list(filter(lambda t: int(t[0]) > max[t[1]], m)):
            print(re.match("^\w+\s(\d)", line).groups()[0])
            sum_ids += int(re.match("^\w+\s(\d+)", line).groups()[0])
    
    print(sum_ids)

def day2_part2(data):
    sum_of_cubes = 0
    for line in data:
        pattern = r"(\d+)\s+(\w+)"
        m = findall(pattern, line)
        cubes = 1 

        for color in ["green", "red", "blue"]:
            cubes *= max(map(lambda t: int(t[0]), filter(lambda t: t[1] == color, m)))

        sum_of_cubes +=cubes
    print(sum_of_cubes)

def day(data):
    sum_of_parts = 0
    for i, line in enumerate(data):
        for match in re.finditer(r"\d+", line):
            start = match.start()
            val = match[0]
            box_width = len(match[0]) + 2 if start > 0 or start != len(line) else len(match[0]) + 1 
            row_start, row_end = max(i - 1, 0), i + 2
            col_start = max(start - 1, 0)

            for row in data[row_start:row_end]:
                if re.search(f"[^\n\.|\d]", row[col_start:col_start+box_width]):
                    sum_of_parts += int(val)
                    print(row[col_start:col_start+box_width].replace("\n",""), data[row_start:row_end], val)
                    break
    print(sum_of_parts)


def main():
    pass

if __name__ == "__main__":
    main()