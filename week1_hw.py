
"""
    Write a function moving_average_window(x,n_neighbours) that takes a list x and the number of neighbours (n_neighbours)
    on either side of a given member from the list to consider.

    For each value in x, moving_average_window computes the average of the value and the value of its neighbours

    moving_average_window should return a list of averaged values that is the same length as the original list

    If there are not enough neighbours, substitute the original value for a neighbour for each missing neighbour

    Use your function to find the moving window sum of x = [0,10,5,3,1,5] and n_neighbours = 1
"""

import random

def moving_window_average(x,n_neighbours=1):

    n = len(x)
    width = n_neighbours * 2 + 1
    x = [x[0]] * n_neighbours + x + [x[-1]] * n_neighbours
    #print(extended_list,x)
    out_list = []
    val_list = []

    for the_index in range(n):
        val_list = x[the_index:(the_index+width)]
        value = sum(val_list) / len(val_list)
        out_list.append(value)
        val_list = []

    return out_list


# x = [0,10,5,3,1,5]
# print(moving_window_average(x,2))


random.seed(1) # This line fixes the value called by your function,
               # and is used for answer-checking.
    
R = 10
x = []

for i in range(R):
    x.append(random.uniform(0,1))
    
Y = []

n_neighbours = range(1,10)

for val in n_neighbours:
    out = moving_window_average(x,val)
    Y.append(out)
    
#print(Y)

# for ele in Y:
#     if ele[0] == 5:
#         #print(ele[0])
#         v1 = ele[2]

# test_val = ele[1]
# v2 = (moving_window_average(test_val,5))
# print(v2[9])
# #print(v1 == v2)

ranges = []

for ele in Y:
    max_val = max(ele)
    min_val = min(ele)
    ranges.append(max_val-min_val)

print(ranges)