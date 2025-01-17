total, dims = 0, []

with open("code.txt") as code:
    for line in code:
        dims.append(list(map(int, line.strip().split("x"))))

for box in dims:
    a, b, c = box[0], box[1], box[2]
    
    total += 2 * min(a + b, b + c, c + a) + a * b * c

print(total)