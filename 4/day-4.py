import click

def to_range(s):
    lower, upper = s.split('-')
    return range(int(lower), int(upper) + 1)

def part_one(input):
    duplicates = []
    for line in input.readlines():
        first, second = line.strip().split(',')
        first_set = set(to_range(first))
        second_set = set(to_range(second))

        if first_set.issubset(second_set) or second_set.issubset(first_set):
            duplicates.append((first_set, second_set))

    print(f'{len(duplicates)=}')


def part_two(input):
    overlaps = []
    for line in input.readlines():
        first, second = line.strip().split(',')
        first_set = set(to_range(first))
        second_set = set(to_range(second))

        if first_set & second_set:
            overlaps.append((first_set, second_set))

    print(f'{len(overlaps)=}')



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
