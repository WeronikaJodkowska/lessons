"""
Who would've guessed? Doomsday devices take a LOT of power. Commander Lambda wants to supplement the LAMBCHOP's quantum
antimatter reactor core with solar arrays, and you've been tasked with setting up the solar panels.

Due to the nature of the space station's outer paneling, all of its solar panels must be squares. Fortunately,
you have one very large and flat area of solar material, a pair of industrial-strength scissors, and enough MegaCorp
Solar Tape(TM) to piece together any excess panel material into more squares. For example, if you had a total area of
12 square yards of solar material, you would be able to make one 3x3 square panel (with a total area of 9). That
would leave 3 square yards, so you can turn those into three 1x1 square solar panels.

Write a function solution(area) that takes as its input a single unit of measure representing the total area of solar
panels you have (between 1 and 1000000 inclusive) and returns a list of the areas of the largest squares you could
make out of those panels, starting with the largest squares first. So, following the example above, solution(12)
would return [9, 1, 1, 1].
"""


def solution(area: int):
    result_squares = []
    while area > 0:
        biggest_area = int(area ** 0.5) ** 2
        result_squares.append(biggest_area)
        area -= biggest_area
    return result_squares


def solution_rec(area: int):
    result_squares = []
    if area <= 0:
        return result_squares
    else:
        biggest_area = int(area ** 0.5) ** 2
        result_squares.append(biggest_area)
        result_squares += solution_rec(area - biggest_area)
        return result_squares


if __name__ == "__main__":
    print(solution(12))
    print(solution(777))
    print(solution(15324))

    print("Recursion solution:")
    print(solution_rec(12))
    print(solution_rec(777))
    print(solution_rec(15324))
