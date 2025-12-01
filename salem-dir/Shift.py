
def rotate_list(lst, steps, direction="right"):
    

    steps = steps % len(lst)    
    
    if direction == "right":
        return lst[-steps:] + lst[:-steps]
    elif direction == "left":
        return lst[steps:] + lst[:steps]
    else:
        raise ValueError(" ")
        
l = [1, 2, 3, 4, 5]

print(rotate_list(l, 2, "right"))  
print(rotate_list(l, 3, "right"))  
print(rotate_list(l, 2, "left"))   
print(rotate_list(l, 3, "left"))
