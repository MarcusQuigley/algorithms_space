def peoplegrouper(group): # #1282 Group the People Given the Group Size They Belong To
    if group is None or len(group) == 0:
        return []
    n = len(group)
    temp = [0] * 500
    result = []
    for i in range(n):
        value = group[i]
        if temp[value] == 0:
            temp[value] = [i]
        else:
            temp[value].append(i)
    
    for j in range(500):
        if temp[j]!=0:
            internallist = []
            for k in range(len(temp[j])):
                if k == 0 or k % j == 0:
                    if len(internallist) > 0:
                        result.append(internallist)
                    internallist = []
                internallist.append(temp[j][k])
            result.append(internallist)
    return result
                
