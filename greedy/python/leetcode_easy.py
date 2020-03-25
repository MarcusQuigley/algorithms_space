def balancedStringSplit(s) -> int:
    result = 0
    lchars= 0 
    rchars= 0
    
    for i in range(len(s)-1, -1, -1):
        currentchar = s[i]
        if currentchar == "L":
            lchars += 1
        else:
            rchars += 1
        if lchars == rchars:
            result += 1
            lchars = 0
            rchars = 0
    
    return result      

def minDeletionSize(list) -> int:
    result = 0
    if len(list) > 0:
        n = len(list[0])
        
        for i in range(n):
            for j in range(len(list) - 1):
                if list[j][i] > list[j+1][i]:
                    result += 1
                    break

    return result
#1046 https://leetcode.com/problems/last-stone-weight/
def laststoneweight1(stones):
    while len(stones) > 1:
        maxval1 = -1
        maxval2 = -1
        maxindex1 = -1
        maxindex2 = -1

        for i in range(len(stones)):
            if stones[i] > maxval1:
                maxval1 = stones[i]
                maxindex1 = i
            elif stones[i] > maxval2:
                maxval2 = stones[i]
                maxindex2 = i
            if maxval1 > maxval2:
                temp = maxval1
                maxval1 = maxval2
                maxval2 = temp
                temp = maxindex1
                maxindex1 = maxindex2
                maxindex2 = temp
        if maxval2 > maxval1:
            diff = maxval2 - maxval1
            stones[maxindex2] = diff
            stones.pop(maxindex1)
        else:
            if maxindex2 > maxindex1:
                stones.pop(maxindex2)
                stones.pop(maxindex1)
            else:
                stones.pop(maxindex1)                
                stones.pop(maxindex2)
    if len(stones)>0:
        return stones[0]
    return 0

#1046 https://leetcode.com/problems/last-stone-weight/
#cleaner
def laststoneweight(stones):
    while len(stones) > 1:
        stones.sort(reverse = True)
        diff = stones[0] - stones[1]
        if diff == 0:
            stones.pop(1)
        else:
            stones[1] = diff
        stones.pop(0)
    return 0 if len(stones) == 0 else stones[0]
    


def issubsequence(parent, child): # 392
    if len(parent) == 0 and len(child) == 0:
        return True
    if len(child) > len(parent):
        return False
    if len(child) == 0:
        return True
    if len(parent) == 0:
        return False
        
    childindex = 0
    for p in parent:
        if child[childindex] == p:
            if len(child) == childindex + 1:
                return True
            childindex+=1
    return False


