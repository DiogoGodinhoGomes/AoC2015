with open("code.txt") as code:
    for line in code:
        building = line.strip()

floor = 0

for f in building:
    if f == "(":
        floor += 1
    elif f == ")":
        floor -= 1
    else:
        assert()

print(floor)