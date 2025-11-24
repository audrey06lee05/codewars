def find_short(s):
    # your code here
    splitted = s.split()
    len_list = []
    
    for i in splitted:
        len_list.append(len(i))
​
    return min(len_list)