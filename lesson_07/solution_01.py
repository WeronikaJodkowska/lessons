"""
НИспользуя условие первой задачи из урока, проверить то же самое только для коней.
"""


def do_figures_beat_each_other(x1, y1, x2, y2):
    figure_1 = [x1, y1]
    figure_2 = [x2, y2]
    figure1_moves = [figure_1]
    figure2_moves = [figure_2]
    intersecting_moves = []

    list_of_moves = [
        [1, 2], [-1, 2], [1, -2], [-1, -2],
        [2, 1], [-2, 1], [2, -1], [-2, -1]
    ]

    for move in list_of_moves:
        move1_x1 = figure_1[0] + move[0]
        move2_y1 = figure_1[1] + move[1]
        move1_x2 = figure_2[0] + move[0]
        move2_y2 = figure_2[1] + move[1]
        if 1 <= move1_x1 <= 8 and 1 <= move2_y1 <= 8 and 1 <= move1_x2 <= 8 and 1 <= move2_y2 <= 8:
            figure1_moves.append([move1_x1, move2_y1])
            figure2_moves.append([move1_x2, move2_y2])

    for i in figure1_moves:
        if i in figure2_moves:
            intersecting_moves.append(i)
    if len(intersecting_moves) != 0:
        print("Yes")
    else:
        print("No")


def main():
    x1 = int(input("Enter x1: "))
    y1 = int(input("Enter y1: "))
    x2 = int(input("Enter x2: "))
    y2 = int(input("Enter y2: "))

    do_figures_beat_each_other(x1, y1, x2, y2)


if __name__ == "__main__":
    main()
