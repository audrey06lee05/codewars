def high_and_low(numbers):
    # ...
    num = numbers.split()
    num = [int(i) for i in num]
    num.sort()
    
    return f'{num[-1]} {num[0]}'