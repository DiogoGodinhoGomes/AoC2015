text, uniq = [], set()

with open("code.txt") as file:
    for line in file:
        text = line.strip()

for i in [c for c in text]:
    if (ord(i) < ord("0") or ord(i) > ord("9")) and ord(i) != ord("-"):
        uniq.add(i)

for i in uniq:
    text = text.replace(i, " ")

print(sum([int(c) for c in text.strip().split()]))