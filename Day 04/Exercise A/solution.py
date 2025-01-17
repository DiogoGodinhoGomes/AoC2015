import hashlib

with open("code.txt") as code:
    for line in code:
        string = line.strip()

i = 0

new_str = string + str(i)

while str(hashlib.md5(new_str.encode('utf-8')).hexdigest())[:5] != "00000":
    i += 1
    
    new_str = string + str(i)

print(i)