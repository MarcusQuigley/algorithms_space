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

