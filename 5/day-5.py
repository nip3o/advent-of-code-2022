import re
import click

pattern = re.compile(r'move (\d+) from (\d+) to (\d+)')

def parse_input(input) -> tuple[dict[int, list[str]], list[str]]:
    definition = []
    movements = []

    for line in input.readlines():
        if line.startswith('move'):
            movements.append(line.strip())
        elif line.strip():
            definition.append(line.replace('\n', ''))

    stack_count = int(definition.pop()[-1])
    stacks = {i: [] for i in range(1, stack_count + 1)}

    for row in reversed(definition):
        for i in range(stack_count):
            if crate := row[i * 4:(i * 4) + 4].strip():
                stacks[i + 1].append(crate)

    return stacks, movements

def print_result(stacks: dict[int, list[str]]) -> None:
    message = ""
    for id, content in stacks.items():
        print(f"{id}: {' '.join(content)}")
        message += content[-1]

    print(message.replace('[', '').replace(']', ''))


def part_one(input) -> None:
    stacks, movements = parse_input(input)

    for move in movements:
        amount, origin, destination = re.match(pattern, move).groups()

        for i in range(int(amount)):
            stacks[int(destination)].append(stacks[int(origin)].pop())

    print_result(stacks)

def part_two(input):
    stacks, movements = parse_input(input)

    for move in movements:
        amount, origin, destination = re.match(pattern, move).groups()
        from_stack = stacks[int(origin)]

        crates = from_stack[-int(amount):]
        del from_stack[-int(amount):]

        stacks[int(destination)] += crates

    print_result(stacks)


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
