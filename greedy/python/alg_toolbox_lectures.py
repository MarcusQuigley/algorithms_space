def largest_number(numbers):
    maxindex = -1
    currentindex = 0
    #print(type(numbers))
    n = len(numbers)
    #results = []
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
        #numbers.pop(maxindex)
        #results.append(str(maxvalue))
    return ''.join(numbers)
    
    

