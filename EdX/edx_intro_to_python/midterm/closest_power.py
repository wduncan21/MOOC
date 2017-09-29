def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
    i=1
    lower=base**0
    higher=base**1
    while lower<num and higher<num:
        lower=base**i        
        i+=1
        higher=base**i
    if lower>=num:
        return 0
    else:
        lowdiff=abs(lower-num)
        highdiff=abs(higher-num)
        if lowdiff<=highdiff:
            return i-1
        else:
            return i