from collections import deque
import itertools

from typing import Iterable, TextIO
import click

def window(seq: TextIO, n: int) -> Iterable:
    # https://stackoverflow.com/questions/6822725/rolling-or-sliding-window-iterator
    char_iterator = itertools.chain.from_iterable(seq)
    window = deque((next(char_iterator, None) for _ in range(n)), maxlen=n)
    yield window
    for e in char_iterator:
        window.append(e)
        yield window


def part_one(input: TextIO) -> None:
    MARKER_LENGTH = 4
    position = MARKER_LENGTH - 1

    for slice in window(input, MARKER_LENGTH):
        position += 1
        if len(slice) == len(set(slice)):
            break

    print(position)


def part_two(input: TextIO) -> None:
    MARKER_LENGTH = 14
    position = MARKER_LENGTH - 1

    for slice in window(input, MARKER_LENGTH):
        position += 1
        if len(slice) == len(set(slice)):
            break

    print(position)



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
