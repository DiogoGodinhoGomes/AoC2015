with open("code.txt") as code:
    for line in code:
        dirs = line.strip()

hor, ver, houses = 0, 0, set()

houses.add((hor, ver))

for d in dirs:
    if d == "^":
        ver += 1
    elif d == ">":
        hor += 1
    elif d == "v":
        ver -= 1
    elif d == "<":
        hor -= 1
    else:
        assert()
    
    houses.add((hor, ver))

print(len(houses))