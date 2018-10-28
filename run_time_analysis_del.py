# -*- coding: utf-8 -*-
"""
In the previous program, I create two lists to store my time of del operator on dictionary and list.
We can see that Dict < List is true, so that the time for del operator on dictionary is smaller than time we need on list.

From running the code above, we can see that the time of delete from both dictionary and list are different. 
And the time for dictionary is much smaller than the time for list. For the program I wrote, 
I chose 5000 times for convenience, since large number will cause more running time. However, 
I tried to delete 10000 times, and the results are much clearer. 
The result for deleting 1000000 goes like this: 0.17455267498735338 seconds for dictionary 
and 162.49849915600498 seconds for list.

@author: Kefei Wu
"""

import timeit
import matplotlib.pyplot as plt

# initialize lists and dictionary
D = {}
L = []

Dict = []
List = []
n_num = []


def dict_code(n):
    """a method that I want to time"""
    D = {i: i for i in range(n)} # create dictionary
    for i in range(n):
        del D[i] # make a delete

def list_code(n):
    """a method that I want to time"""
    L = list(range(n)) # create list
    for i in range(n-1):
        del L[0] # make a delete 

for n in range(5000, 50001, 5000):
    # n is the number of deletes that we want to remove from each dictionary or list
    print("Operation time of deleting n elements","\t","\t", "Dictionary","\t","\t","\t","\t", "List")

    # time how much it takes to delete n times from dictionary
    dict_setup = "from __main__ import D, n, dict_code"
    dict_del = timeit.Timer("dict_code(n)", dict_setup)
    dict_time = dict_del.timeit(1)
    Dict.append(dict_time)
    
    # time how much it takes to delete n times from list
    list_setup = "from __main__ import L, n, list_code"
    list_del = timeit.Timer("list_code(n)", list_setup)
    list_time = list_del.timeit(1)
    List.append(list_time)
    
    n_num.append(n)
    
    print(n,"\t","\t","\t","\t","\t","\t", dict_time,"\t","\t","\t", list_time)

# plot dictionary delete time and list delete time in one graph
plt.title('Comparing Delete Time on Dictionary and List')
plt.xlabel('Delete time')
plt.ylabel('Number of Operations')
plot_dict, = plt.plot(Dict, n_num, label = 'Dictionary')
plot_list, = plt.plot(List, n_num, label = 'List')
plt.legend(handles = [plot_dict, plot_list])
plt.show()
