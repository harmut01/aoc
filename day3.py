import re
import click
from helpers import *

def part1(data):
    sum_of_parts = 0
    for i, line in enumerate(data):
        for match in re.finditer(r"\d+", line):
            start = match.start()
            val = match[0]
            box_width = len(match[0]) + 2 if start > 0 or start != len(line) else len(match[0]) + 1 
            row_start, row_end = max(i - 1, 0), i + 2
            col_start = max(start - 1, 0)

            for row in data[row_start:row_end]:
                if re.search(f"[^\n\\.|\\d]", row[col_start:col_start+box_width]):
                    sum_of_parts += int(val)
                    break
    print(sum_of_parts)


def part2(data):
    product = 0
    pos_dict = {}

    for i, line in enumerate(data):
        for match in re.finditer(r"\d+", line):
            start = match.start()
            val = match[0]
            box_width = len(match[0]) + 2 if start > 0 or start != len(line) else len(match[0]) + 1 
            row_start, row_end = max(i - 1, 0), i + 2
            col_start = max(start - 1, 0)

            for j, row in enumerate(data[row_start:row_end], start=row_start):
                m = re.search(f"\*", row[col_start:col_start+box_width])
                if m:
                    ast_pos = m.span()
                    ast_pos = (j, ast_pos[0] + col_start)
                    if ast_pos not in pos_dict:
                        pos_dict[ast_pos] = [int(val)]
                    else:
                        pos_dict[ast_pos].append(int(val))
            print(pos_dict)
    for pairs in filter(lambda pair: len(pair) > 1, pos_dict.values()):
        # print(pairs)
        product += pairs[0] * pairs[1]
    print(product)
            

@click.command()
@click.option("--test", is_flag=True, default=False)
def main(test):
    filename = "data/test.in" if test else "data/3.in"
    data = get_input(filename)
    
    part1(data)
    part2(data)

                         

if __name__ == "__main__":
    main()