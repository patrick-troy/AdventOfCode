from aocd import get_data

session = "53616c7465645f5faf5b07f02c599e770eb3890fef2f9160aa1d181" \
          "8008355b1039bff4b82dd31da6789c51ed44ffba3bd74d9af3975c26e245446ff30bcf2c7"

rucksacks = get_data(day=3, year=2022, session=session).split("\n")

# PART 1
total = 0

for items in rucksacks:
    compartment_split = int(len(items)/2)
    half_1 = items[:compartment_split]
    half_2 = items[compartment_split:]
    unique_matches = set(half_1) & set(half_2)
    match = next(iter(unique_matches))
    total += ord(match)-38 if match.isupper() else ord(match)-96

print(total)

# PART 2
total = 0

grouped_rucksacks = [rucksacks[i:i+3] for i in range(0, len(rucksacks), 3)]
for group in grouped_rucksacks:
    badge_match = set(group[0]) & set(group[1]) & set(group[2])
    badge = next(iter(badge_match))
    total += ord(badge) - 38 if badge.isupper() else ord(badge) - 96

print(total)
