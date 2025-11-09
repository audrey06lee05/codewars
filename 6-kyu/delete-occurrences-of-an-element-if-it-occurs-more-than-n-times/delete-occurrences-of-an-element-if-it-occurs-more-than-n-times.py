def delete_nth(order,max_e):
    check_times = {}
    new_list = []
    
    for i in order:
        if i not in check_times:
            check_times[i] = 0
        
        check_times[i] += 1
        
        if check_times[i] <= max_e:
            new_list.append(i)
            
    return new_list
            
            
    