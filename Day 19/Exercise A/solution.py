pairs, molec = {}, ""

with open("code.txt") as file:
    for line in file:
        if "=" in line:
            temp = line.strip().split()
            
            if temp[0] not in pairs.keys():
                pairs[temp[0]] = [temp[2]]
            else:
                pairs[temp[0]].append(temp[2])
        elif len(line) > 0:
            molec = line.strip()

# FIND ALL THE LOCATIONS OF ALL THE REPLACEABLE MOLECULAR COMPONENTS IN THE MOLECULE
#     Al [x, y, z, ...]
#     B  [a, b, c, ...]
#     Ca [o, p, q, ...]
#     etc.