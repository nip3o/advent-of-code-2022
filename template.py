from typing import TextIO
import click

def part_one(input: TextIO) -> None:
    raise NotImplementedError

def part_two(input: TextIO) -> None:
    raise NotImplementedError


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
