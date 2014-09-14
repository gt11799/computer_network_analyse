#!usr/bin/env python
'''
Test the resilience of computer network, ugraph generate with probability 
and ugraph concentrate on some nodes
'''

import pickle
from ugraph_compute import compute_resilience
from ugraph_compute2 import targeted_order
from computer_network import load_graph
from ER_ugraph import ugraph_probability
from UPA_ugraph import ugraph_UPA
from resilience_random import plot_attack

NODES = 1347
EDGES = 3112
P = 0.00345
M = 1

def attack_ordered(ugraphs):
    '''
    attack the ugraph with the ordered nodes
    '''
    result = []
    for ugraph in ugraphs:
        nodes_ordered = targeted_order(ugraph)
        resilience = compute_resilience(ugraph, nodes_ordered)
        result.append(resilience)
    data_file = open('data_resilience_ordered.p', 'wb')
    pickle.dump(result, data_file)
    data_file.close()
    return 'data_resilience_ordered.p'
    
    

def test_attack_ordered():
    ugraph_network = load_graph('computer_network.txt')
    ugraph_ER = ugraph_probability(NODES, P)
    attack_ordered((ugraph_network, ugraph_ER))
    data_file = open('data_resilience_ordered.p', 'rb') 
    
    cc_set = pickle.load(data_file)
    data_file.close()
    print('test attack:')     
    print("cc_network length: %d, cc_er length: %d" %(len(cc_set[0]), len(cc_set[1])))
    print("cc_network: %s\n%s" %(cc_set[0][-6:], cc_set[0][:6]))    
    print("cc_er: %s\n%s" %(cc_set[1][-6:], cc_set[1][:6])) 

def easy_test():
    UGRAPH10 = {0:set([]), 1:set([2,3,4]), 2:set([1,3]), 3:set([1,2]), 
    4:set([1]), 5:set([6]), 6:set([5]), 7:set([])}
    attack_ordered((UGRAPH10,))
    
    data_file = open('data_resilience_ordered.p', 'rb') 
    cc_set = pickle.load(data_file)
    data_file.close()
    print("easy_test: %s" %cc_set)

if __name__ == '__main__':
    #ugraph_network = load_graph('computer_network.txt')
    #ugraph_ER = ugraph_probability(NODES, P)
    #ugraph_UPA = ugraph_UPA(NODES, M)
    
    file_name = 'data_resilience_ordered.p'
    #file_name = attack_ordered((ugraph_network, ugraph_ER, ugraph_UPA))
    
    plot_attack(file_name)
    
    