def binary_array_to_number(arr):
    num = ""
    
    for i in arr:
        num += f"{i}"
​
    return int(num,2)