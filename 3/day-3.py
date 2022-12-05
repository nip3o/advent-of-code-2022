import click
import string
import itertools

WEIGHTS = {
    char: i
    for i, char in
    enumerate(string.ascii_letters, 1)
}

def grouper(iterable, n):
    # https://stackoverflow.com/questions/8991506/iterate-an-iterator-by-chunks-of-n-in-python
    it = iter(iterable)
    while True:
        chunk = tuple(itertools.islice(it, n))
        if not chunk:
            return
        yield chunk


def part_one(input):
    common_weights = []

    for line in input.readlines():
        line = line.strip()

        item_count = int(len(line) / 2)
        first, second = line[:item_count], line[item_count:]
        [common] = set(first).intersection(set(second))
        common_weights.append(WEIGHTS[common])

    print(f'{sum(common_weights)=}')


def part_two(input):
    badge_weights = []

    for group in grouper(input.readlines(), 3):
        contents = []
        for elf in group:
            contents.append(set(elf.strip()))

        [badge_type] = contents[0] & contents[1] & contents[2]
        badge_weights.append(WEIGHTS[badge_type])

    print(f'{sum(badge_weights)=}')


@click.command()
@click.argument('input', type=click.File('r'))
@click.argument('part', type=click.INT)
def main(input, part):
    if part == 1:
        return part_one(input)

    if part == 2:
        return part_two(input)

    raise AssertionError('Invalid part')


if __name__ == '__main__':
    main()
