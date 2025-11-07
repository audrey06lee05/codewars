def find_next_square(sq):
    # Return the next square if sq is a square, -1 otherwise
    sqrt = sq**0.5
    if not sqrt.is_integer():
        return -1
    else: return ((sqrt)+1)**2
    
​