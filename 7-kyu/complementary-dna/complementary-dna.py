def DNA_strand(dna):
    complements =''
    # code here
    for i in dna:
        if i == 'A':
            complements += 'T'
        elif i == 'T':
            complements += 'A'
        elif i == 'C':
            complements += 'G'
        else: complements += 'C'
    
    return complements