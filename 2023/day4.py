import click
import re
from helpers import *
import pprint

def get_ints(string, start=0, end=-1):
    return re.findall("\\d+", string[start:end])

def set_dict(key, val):
    pass

def part1(data):
    points = 0
    for line in data:
        line = line[line.find(':'):]
        sep = line.find('|')
        winners = get_ints(line, end=sep)
        chosen = get_ints(line, start=sep)

        winning_nums = list(filter(lambda n: n in winners, chosen))
        if len(winning_nums):
            # print(winning_nums)
            points += 1 * 2 ** (len(winning_nums) - 1)
    print(points)


def part2(data):
    get_card_num  = lambda s: re.search("\\d+", s)[0]
    new_cards = {f"{i}": 1 for i in range(1, len(data) + 1)}
    print(new_cards)
    num_cards = len(data)

    for i, line in enumerate(data):
        current_card = get_card_num(line)
        winners = get_ints(line, start=line.find(':'), end=line.find('|'))
        chosen = get_ints(line, start=line.find('|'))

        winning_nums = list(filter(lambda n: n in winners, chosen))
        for j in range(1, len(winning_nums) + 1):
            card = get_card_num(data[i + j])
            if card not in new_cards:
                new_cards[card] = 1
            else:
                new_cards[card] += new_cards[current_card]
            # print(current_card, "new card = ", card, new_cards[card])
    print(sum(new_cards.values()))

@click.command()
@click.option("--test", is_flag=True)
def main(test):
    if test:
        data = get_input("data/test.in")
    else:
        data = get_input("data/4.in")
    
    part1(data)
    part2(data)

if __name__ == "__main__":
    main()

