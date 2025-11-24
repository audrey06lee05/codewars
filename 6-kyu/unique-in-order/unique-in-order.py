def unique_in_order(sequence):
    results = []
    prev = None 
    
    for i in sequence:
        if i != prev:
            results.append(i)
            prev = i 
        
            
    return results