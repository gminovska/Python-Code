def clip(lo, x, hi):
    '''
    Takes in three numbers and returns a value based on the value of x.
    Returns:
     - lo, when x < lo
     - hi, when x > hi
     - x, otherwise
    '''
    # Your code here
    a = min(lo, x, hi)
    b =max(lo, x, hi)
    c = lo + x + hi
    d = c - (a + b)
    return round(d, 2)

#elegant solution wit min and max only:

    return min(hi,max(lo,x)) 
