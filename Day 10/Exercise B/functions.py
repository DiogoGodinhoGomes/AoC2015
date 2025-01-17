def process(init):
    if len(init) == 0:
        return init
    
    if len(init) == 1:
        return "1" + init
    
    index, counter, current, result = 1, 1, init[0], ""
    
    while index < len(init):        
        if init[index] == current:
            counter += 1
        else:
            result += str(counter) + str(current)
            
            counter, current = 1, init[index]
        
        index += 1
    
    return result + str(counter) + str(current)