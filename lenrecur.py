def lenRecur(aStr):
    '''
    aStr: a string
    
    returns: int, the length of aStr
    '''
    # Your code here
    a = 1
    if aStr == "":
        return a - 1
    else:
        return a  + lenRecur(aStr[1:])

# alternative method


 a = 0
    if aStr == "":
        return a - 1 
    else:
        a = a + 2
        return a  + lenRecur(aStr[1:-1])
