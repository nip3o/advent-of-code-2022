from typing import Iterable, TextIO
import click

def should_sample(clock: int) -> bool:
    return (clock + 20) % 40 == 0

def get_instructions(input: TextIO) -> Iterable[tuple[str, int]]:
    for line in input.readlines():
        cmd, arg = line[:4], line[4:].strip()

        yield ('noop', None)
        if cmd == 'addx':
            yield ('addx', arg)


def part_one(input: TextIO) -> None:
    samples = []
    clock = 1
    x = 1

    for (cmd, arg) in get_instructions(input):
        # Beginning of clock cycle.
        ...

        # During clock cycle.
        strength = clock * x

        if sample := should_sample(clock):
            samples.append(strength)

        print(f"{clock:3d}: {'S' if sample else ' '} {x=} => {strength}")

        # After clock cycle.
        if cmd == 'addx':
            x += int(arg)

        clock += 1

    print(f"{sum(samples)=}")


def part_two(input: TextIO) -> None:
    crt = [[] for r in range(6)]
    clock = 1
    x = 1

    for (cmd, arg) in get_instructions(input):
        # Beginning of clock cycle.
        ...

        # During clock cycle.
        position = (clock - 1) % 40
        row = (clock - 1) // 40 % (40 * 6)

        pixel = '#' if x in (position - 1, position, position + 1) else ' '
        crt[row].append(pixel)

        # After clock cycle.
        if cmd == 'addx':
            x += int(arg)

        clock += 1

    for row in crt:
        print(''.join(row))



@click.command()
@click.argument('input', type=click.File('r'))
@click.argument('part', type=click.INT)
def main(input: TextIO, part: int) -> None:
    if part == 1:
        return part_one(input)

    if part == 2:
        return part_two(input)

    raise AssertionError('Invalid part')


if __name__ == '__main__':
    main()
