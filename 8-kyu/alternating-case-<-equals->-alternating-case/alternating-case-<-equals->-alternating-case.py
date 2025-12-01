def to_alternating_case(string):
    output = ""
    for i in string:
        if i.islower():
            output += i.upper()
        else: output += i.lower()
    
    return output
​