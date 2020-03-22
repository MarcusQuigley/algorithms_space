def largest_number(numbers):
    maxindex = -1
    currentindex = 0
    n = len(numbers)
    while currentindex < n:
        maxvalue = -1
        for i in range(currentindex, n):
            if numbers[i] > maxvalue:
                maxvalue = numbers[i]
                maxindex = i
        temp = str(numbers[maxindex])
        numbers[maxindex] = numbers[currentindex]
        numbers[currentindex] = temp
        currentindex += 1
    return ''.join(numbers)
    
def fractional_knapsack(bagcapacity, weights, values):
    n = len(weights)
    #voverw = [0] * n 
    result = 0
   
    usedweights = set()
    while result < bagcapacity or len(usedweights) < n:
        maxvalue = -1
        maxindex = -1
        for index in range(n):
            w = weights[index]
            if w not in usedweights: #this should be set difference if 2 not in usedweights
                v = int(w /values[index])
                if v > maxvalue:
                    maxvalue = v
                    maxindex = index
        #bagcapacity -= weights[maxindex]
        if (maxindex == -1):
            break
        weight = weights[maxindex]
        value = values[maxindex]
        
        if value < (bagcapacity - result):
            result += value
            usedweights.add(weight)
        else:
            val = value // (bagcapacity - result)  
            result += val
            usedweights.add(weight) #??
            #break


    return result
            


            





