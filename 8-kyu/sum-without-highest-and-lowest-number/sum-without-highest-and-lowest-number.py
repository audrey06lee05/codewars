def sum_array(arr):
    #your code here
    if not arr or len(arr) == 1:
        return 0
    else:
        arr.sort()
        arr.pop() # remove last element
        arr.pop(0) # remove first element
    
    return sum(arr)