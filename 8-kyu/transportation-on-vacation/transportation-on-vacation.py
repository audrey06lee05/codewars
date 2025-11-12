def rental_car_cost(d):
    cost = 0 
    # your code
    if d < 3:
        cost = 40 * d
    elif d >= 3 and d < 7:
        cost = 40 * d - 20
    elif d >= 7:
        cost = 40 * d - 50
        
    return cost