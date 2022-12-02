import click

def part_one(input):
    elf_totals = []
    elf_total = 0

    for line in input.readlines():
        line = line.strip()

        if not line:
            elf_totals.append(elf_total)
            elf_total = 0
            continue

        elf_total += int(line)

    print(f'{max(elf_totals)=}')
    return elf_totals

def part_two(input):
    elf_totals = sorted(part_one(input))
    print(f'Top three elf totals: {elf_totals[-3:]}')
    print(f"{sum(elf_totals[-3:])=}")



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
