def alphabet_position(text):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    text = text.lower()
    num = ""
    
    for i in text:
        if i in alphabet:
            num += f'{str(alphabet.index(i)+1)} '
            
    return num.strip()