def xo(s):
    xo_check = {"x":0, "o":0} #dictionary counter
    
    for letter in s:
        letter = letter.lower()
        if letter == "x":
            xo_check["x"] += 1
        elif letter == "o":
            xo_check["o"] += 1
            
    if xo_check["x"] == xo_check["o"]:
        return True
    else: return False