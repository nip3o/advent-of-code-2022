from typing import TextIO
import click


def column_slice(grid: list[int], y: int, length: int, x: int):
    return [grid[y + i][x] for i in range(length)]

def is_visible(tree: int, trees: list[int]) -> bool:
    return tree > max(trees)

def visible_left(grid: list[int], y: int, x: int) -> bool:
    return x == 0 or is_visible(grid[y][x], grid[y][:x])

def visible_right(grid: list[int], y: int, x: int) -> bool:
    return x == len(grid) - 1 or is_visible(grid[y][x], grid[y][x + 1:])

def visible_top(grid: list[int], y: int, x: int) -> bool:
    return y == 0 or is_visible(grid[y][x], column_slice(grid, 0, y, x))

def visible_bottom(grid: list[int], y: int, x: int) -> bool:
    return y == len(grid) - 1 or is_visible(grid[y][x], column_slice(grid, y + 1, len(grid) - y - 1, x))


def get_distance(tree: int, trees: list[int]) -> bool:
    s = 0
    for t in trees:
        s += 1

        if t >= tree:
            return s

    return s

def distance_left(grid: list[int], y: int, x: int) -> bool:
    return get_distance(grid[y][x], reversed(grid[y][:x]))

def distance_right(grid: list[int], y: int, x: int) -> bool:
    return get_distance(grid[y][x], grid[y][x + 1:])

def distance_top(grid: list[int], y: int, x: int) -> bool:
    return get_distance(grid[y][x], reversed(column_slice(grid, 0, y, x)))

def distance_bottom(grid: list[int], y: int, x: int) -> bool:
    return get_distance(grid[y][x], column_slice(grid, y + 1, len(grid) - y - 1, x))


def part_one(input: TextIO) -> None:
    grid = [[int(c) for c in row.strip()] for row in input.readlines()]

    visible = []
    for x in range(len(grid)):
        for y in range(len(grid)):
            if visible_left(grid, y, x) or visible_right(grid, y, x) or visible_top(grid, y, x) or visible_bottom(grid, y, x):
                visible.append((x, y))

    print(f'{len(visible)=}')


def part_two(input: TextIO) -> None:
    grid = [[int(c) for c in row.strip()] for row in input.readlines()]

    scores = []
    for x in range(len(grid) - 1):
        for y in range(len(grid) - 1):
            score = distance_top(grid, y, x) * distance_left(grid, y, x) * distance_right(grid, y, x) * distance_bottom(grid, y, x)
            scores.append(score)

    print(f'{max(scores)=}')



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
