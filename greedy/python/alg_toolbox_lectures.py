def largest_number(numbers):
    #numbers.sort(reverse=True)
    #startindex = -1
    maxindex = -1
    print(type(numbers))
    n = len(numbers)
    results = []
    while len(results) < n:
        maxvalue = -1
        for i in range(len(numbers)):
            if numbers[i] > maxvalue:
                maxvalue = numbers[i]
                maxindex = i
        numbers.pop(maxindex)
        results.append(str(maxvalue))
    return ''.join(results)
    
    

