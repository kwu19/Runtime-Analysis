# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
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