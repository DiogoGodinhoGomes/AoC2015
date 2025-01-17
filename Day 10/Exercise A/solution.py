import functions as fc

i, lim = 0, 40

with open("code.txt") as file:
    for line in file:
        init = line.strip()

while i < lim:
    init = fc.process(init)
    
    i += 1

print(len(init))