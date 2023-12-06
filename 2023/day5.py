import click
from helpers import *

def part1(data):
    print(data)

@click.command()
@click.option("--test", is_flag=True)
def main(test):
    if test:
        part1(get_input("data/test.in"))
    else:
        part1(get_input("data/5.in"))

if __name__ == "__main__":
    main()

