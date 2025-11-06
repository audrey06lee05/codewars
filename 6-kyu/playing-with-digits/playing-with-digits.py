def dig_pow(n, p):
    # your code
    
    add = 0
    total = 0
    
    for i in str(n):
        total += int(i) ** (p+add)
        add += 1
    
    k = total/int(n)
    if total%int(n) != 0:
        return -1
    else: return k