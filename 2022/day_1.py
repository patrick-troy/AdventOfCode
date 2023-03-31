from aocd import get_data

session = "53616c7465645f5faf5b07f02c599e770eb3890fef2f9160aa1d181" \
          "8008355b1039bff4b82dd31da6789c51ed44ffba3bd74d9af3975c26e245446ff30bcf2c7"

data = get_data(day=4, year=2022, session=session).split("\n")

# PART 1
max_calories = 0
current_calories = 0

for row in data[0]:
    if pd.notna(row):
        current_calories += row
    else:
        max_calories = current_calories if current_calories > max_calories else max_calories
        current_calories = 0

print(max_calories)

# PART 2
max_calories_each = 0
max_calories_all = []

for row in data[0]:
    if pd.notna(row):
        max_calories_each += row
    else:
        max_calories_all.append(max_calories_each)
        max_calories_each = 0

print(sum(sorted(max_calories_all)[-3:]))
