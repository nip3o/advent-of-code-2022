import click




class Rock:
    score = 1

    def defeats(self, other):
        return isinstance(other, Scissors)

    def get_proposal(self, code: str):
        # X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win. Good luck!"
        match code:
            case "X":
                return Scissors()
            case "Y":
                return Rock()
            case "Z":
                return Paper()

class Paper:
    score = 2

    def defeats(self, other):
        return isinstance(other, Rock)

    def get_proposal(self, code: str):
        match code:
            case "X":
                return Rock()
            case "Y":
                return Paper()
            case "Z":
                return Scissors()

class Scissors:
    score = 3

    def defeats(self, other):
        return isinstance(other, Paper)

    def get_proposal(self, code: str):
        match code:
            case "X":
                return Paper()
            case "Y":
                return Scissors()
            case "Z":
                return Rock()

def calculate_score(opponent, proposed):
    score = proposed.score

    if proposed.defeats(opponent):
        score += 6
    elif type(opponent) == type(proposed):
        score += 3

    return score

def part_one(input):
    # The score for a single round is the score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors) plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).
    def parse_type(code: str):
        match code:
            case 'A' | 'X':
                return Rock()
            case 'B' | 'Y':
                return Paper()
            case 'C' | 'Z':
                return Scissors()

    round_scores = []

    for line in input.readlines():
        row = line.strip().split(" ")
        opponent = parse_type(row[0])
        proposed = parse_type(row[1])
        round_scores.append(calculate_score(opponent, proposed))

    print(f"{sum(round_scores)=}")


def part_two(input):
    def parse_type(code: str):
        return {'A': Rock(), 'B': Paper(), 'C': Scissors()}[code]

    round_scores = []

    for line in input.readlines():
        row = line.strip().split(" ")
        opponent = parse_type(row[0])
        proposed = opponent.get_proposal(row[1])
        round_scores.append(calculate_score(opponent, proposed))

    print(f"{sum(round_scores)=}")


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
