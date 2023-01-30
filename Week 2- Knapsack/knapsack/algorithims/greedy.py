from operator import attrgetter

def greedy_most_valueable_items(items,capacity):
    # sort the list in the reverse order of value
    items = sorted(items,key=attrgetter('value'),reverse=True)
    # fill the knapsack until capacity is full
    taken = [0]*len(items)
    filled_capacity=0
    obj_value = 0
    
    for item in items:
        if item.weight<= capacity - filled_capacity:
            taken[item.index] = 1
            filled_capacity += item.weight
            obj_value += item.value 
            if filled_capacity == capacity:
                break
    
    return (obj_value,taken)

def greedy_most_value_density_items(items,capacity):
    
    taken = [0]*len(items)
    obj_value = 0
    
    #calculate the value densities and sort in the descending order for these densities
    item_value_densities = {item:(item.value/item.weight) for item in items}
    item_value_densities = sorted(item_value_densities.items() , key = lambda x: x[1]  , reverse = True)
    
    # fill the knapsack until capacity is full
    filled_capacity=0
    for item,_ in item_value_densities:
        if item.weight<= capacity - filled_capacity:
            taken[item.index] = 1
            filled_capacity += item.weight
            obj_value += item.value 
            if filled_capacity == capacity:
                break
    
    return obj_value,taken


    