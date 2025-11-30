def count(s):
    # The function code should be here
    count = {}
    if len(s) == 0:
        return {}
    else:
        for i in s:
            if i not in count:
                count[i] = 1
            else:
                count[i] += 1
    
    return count 