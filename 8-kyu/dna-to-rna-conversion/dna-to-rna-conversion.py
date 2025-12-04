def dna_to_rna(dna):
    for i in dna:
        if i == 'T':
            dna = dna.replace(i,'U')
            
    return dna