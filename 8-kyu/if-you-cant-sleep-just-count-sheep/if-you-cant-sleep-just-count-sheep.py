def count_sheep(n):
    # your code
    if not n:
        return ""
    
    sheep_counter = ""
    
    for i in range(1,n+1):
        sheep_counter += f'{i} sheep...'
        
    return sheep_counter