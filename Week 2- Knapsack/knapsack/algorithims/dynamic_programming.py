import numpy as np

def dynamic_programming(items,capacity):
    taken=[0]*len(items)
    obj_value = 0
    
    #initiate the value table
    value_table = [[0]*(len(items)+1) for _ in range(capacity+1)]
    for item_index in range(len(items)):
        if items[item_index].weight>capacity:
            pass
        else:
            for weight_index in range(1,capacity+1):
                if items[item_index].weight>weight_index:
                    # in case the weight is greater than current capacity, item can't be added.
                    # optimum value is the best value without considering that item
                    value_table[weight_index][item_index+1] = value_table[weight_index][item_index]
                else:
                    # if item can be added on current capacity, there are still 2 possibilities:
                    # - it can be added , so objective value can be its value + optimum value with 1 less item, and capacity - its weight
                    value_table[weight_index][item_index+1] = max(value_table[weight_index][item_index],
                                                                  items[item_index].value + value_table[weight_index-items[item_index].weight][item_index])
    
    obj_value = value_table[capacity][len(items)]
    
    weight_index = capacity
    for item_index in range(len(items),0,-1):
        # if optimum value at full capacity is different from previous then the item has been selected
        if value_table[weight_index][item_index] != value_table[weight_index][item_index-1]:
            taken[item_index-1]=1
            # change the index of that item in item list as 1 , reduce the weight index by that items weight
            weight_index = weight_index - items[item_index-1].weight
    
    return obj_value,taken

