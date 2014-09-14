#!/usr/bin/env python
'''
test the efficiency of targeted_order and fast_targeted_order
'''
M = 5

from ugraph_compute2 import targeted_order, fast_targeted_order
from UPA_ugraph import ugraph_UPA
from time import time
import matplotlib.pyplot as plt

def efficiency_targeted():
    targeted_time = []
    for num_nodes in range(10, 1000, 10):
        ugraph = ugraph_UPA(num_nodes, M)
        
        time1 = time()
        targeted_order(ugraph)
        time2 = time()
        targeted_time.append(time2 - time1)
                
    return targeted_time
    
def efficiency_fast():
    fast_time = []
    for num_nodes in range(10, 1000, 10):
        ugraph = ugraph_UPA(num_nodes, M)
        
        time1 = time()
        fast_targeted_order(ugraph)
        time2 = time()
        fast_time.append(time2 - time1)
        
    return fast_time
    
def plot_efficiency():
    x = range(10, 1000, 10)
    fast_time = efficiency_fast()
    targeted_time = efficiency_targeted()
   
    
    plt.plot(x, targeted_time, 'r', label='targeted order')
    plt.plot(x, fast_time, 'b', label='fast targeted order')
    
    plt.legend(loc='best')
    plt.title('test efficiency with desktop Python')
    plt.xlabel('The Number of Nodes in UPA')
    plt.ylabel('The Time used')
    
    plt.show()
    
if __name__ == '__main__':
    plot_efficiency()
