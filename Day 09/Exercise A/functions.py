import itertools as it

def get_cities(filename):
    dicti, pairs, cities = {}, [], set()
    
    with open(filename) as code:
        for line in code:
            pairs.append(line.replace("to","").replace("=","").strip().split())
            
            cities.add(pairs[-1][0])
            cities.add(pairs[-1][1])
            
            pairs[-1][-1] = int(pairs[-1][-1])
    
    cities = sorted(list(cities))
    
    for i in range(len(cities)):
        for j in range(len(pairs)):
            for k in range(len(pairs[j])):
                if pairs[j][k] == cities[i]:
                    pairs[j][k] = i
    
    for j in range(len(pairs)):
        pairs[j] = [(min(pairs[j][0], pairs[j][1]), max(pairs[j][0], pairs[j][1])), pairs[j][2]]
    
    pairs = sorted(pairs)
    
    for e in pairs:
        dicti[e[0]] = e[1]
    
    combis = list(it.permutations(range(len(cities))))
    
    return dicti, cities, combis