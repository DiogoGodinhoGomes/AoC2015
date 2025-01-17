with open("code.txt") as code:
    for line in code:
        dirs = line.strip()

hor_e, ver_e, hor_o, ver_o, houses = 0, 0, 0, 0, set()

houses.add((hor_e, ver_e))

for i, d in enumerate(dirs):
    if i % 2 == 0:
        if d == "^":
            ver_e += 1
        elif d == ">":
            hor_e += 1
        elif d == "v":
            ver_e -= 1
        elif d == "<":
            hor_e -= 1
        else:
            assert()
        
        houses.add((hor_e, ver_e))
    elif i % 2 == 1:
        if d == "^":
            ver_o += 1
        elif d == ">":
            hor_o += 1
        elif d == "v":
            ver_o -= 1
        elif d == "<":
            hor_o -= 1
        else:
            assert()
        
        houses.add((hor_o, ver_o))
    else:
        assert()

print(len(houses))