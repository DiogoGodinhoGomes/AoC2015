import functions as fc

answer, path = -1, -1

dicti, cities, combis = fc.get_cities("code.txt")

for elem in combis:
    dist = 0
    
    for i in range(len(elem) - 1):
        mnm, mxm = min(elem[i], elem[i+1]), max(elem[i], elem[i+1])
        
        dist += dicti[(mnm, mxm)]
    
    if answer < 0 or (answer >= 0 and answer > dist):
        answer = dist
        path = elem

print(answer, path)