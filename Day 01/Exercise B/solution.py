with open("code.txt") as code:
    for line in code:
        building = line.strip()

i, floor = 0, 0

while i <= len(building) and floor >= 0:
    if building[i] == "(":
        floor += 1
    elif building[i] == ")":
        floor -= 1
    else:
        assert()
    
    i += 1

print(i, floor)