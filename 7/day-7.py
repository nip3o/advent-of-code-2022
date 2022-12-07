import re
from typing import TextIO
import click
from anytree import Node, RenderTree, Resolver, PreOrderIter

file_pattern = re.compile(r'(\d+) ([\w\.]+)')


def create_node(name: str, parent: Node = None) -> Node:
    return Node(name, parent=parent, files=[], total_size=0)


def add_nodes_from_file(input: TextIO, root: Node):
    resolver = Resolver('name')
    current = root

    while line := input.readline().strip():
        if line == '$ ls':
            while line := input.readline().strip():
                if line.startswith('$'):
                    break
                elif line.startswith('dir'):
                    create_node(line[4:], parent=current)
                else:
                    size, name = re.match(file_pattern, line).groups()
                    current.files.append((name, int(size)))

        if line.startswith('$ cd'):
            path = line[5:]
            match path:
                case '/':
                    current = root
                case _:
                    current = resolver.get(current, path)

            assert current


def total_size(node: Node) -> int:
    file_size = sum(size for name, size in node.files)
    if not node.children:
        return file_size

    child_size = sum(total_size(child) for child in node.children)
    return file_size + child_size


def annotate_with_total_sizes(root: Node):
    for node in PreOrderIter(root):
        node.total_size = total_size(node)


def part_one(input: TextIO) -> None:
    root = create_node('root')

    add_nodes_from_file(input, root)
    annotate_with_total_sizes(root)

    print(RenderTree(root))
    print()

    answer = sum(
        s for node in PreOrderIter(root) if (s := node.total_size) <= 100000
    )
    print(f'{answer=}')


def part_two(input: TextIO) -> None:
    root = create_node('root')

    add_nodes_from_file(input, root)
    annotate_with_total_sizes(root)

    free = 70000000 - root.total_size
    needed = 30000000 - free

    large_enough = [
        s for node in PreOrderIter(root) if (s := node.total_size) >= needed
    ]
    print(large_enough)
    print(f'{free=}, {needed=}, {min(large_enough)=}')


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
