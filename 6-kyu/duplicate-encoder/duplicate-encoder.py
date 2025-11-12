def duplicate_encode(word):
    string = ""
    word = word.lower()
    
    #your code here
    for i in word:
        if word.count(i) > 1:
            string += ")"
        else: string += "("
        
    return string 