from aocd import get_data

session = "53616c7465645f5faf5b07f02c599e770eb3890fef2f9160aa1d181" \
          "8008355b1039bff4b82dd31da6789c51ed44ffba3bd74d9af3975c26e245446ff30bcf2c7"

X = 1
Y = 2
Z = 3

win_combo = {"A": Y, "B": Z, "C": X}
draw_combo = {"A": X, "B": Y, "C": Z}
lose_combo = {"A": Z, "B": X, "C": Y}

converter = {"X": 1, "Y": 2, "Z": 3}

win = 6
draw = 3
lose = 0

points = 0

data = get_data(day=2, year=2022, session=session).split("\n")

# PART 1
for combination in data:
    if combination[2] == "X":
        points += X
    if combination[2] == "Y":
        points += Y
    if combination[2] == "Z":
        points += Z

    if win_combo[combination[0]] == converter[combination[2]]:
        points += win
    if draw_combo[combination[0]] == converter[combination[2]]:
        points += draw
    elif lose_combo[combination[0]] == converter[combination[2]]:
        points += lose

print(points)

# PART 2
points = 0
secret_combo = {"X": "lose", "Y": "draw", "Z": "win"}

for combination in data:
    if secret_combo[combination[2]] == "lose":
        points += lose
        points += lose_combo[combination[0]]
    if secret_combo[combination[2]] == "draw":
        points += draw
        points += draw_combo[combination[0]]
    elif secret_combo[combination[2]] == "win":
        points += win
        points += win_combo[combination[0]]

print(points)
