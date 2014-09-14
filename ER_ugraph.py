#!/usr/bin/env python
'''
Take number of nodes, and probability,
return a undirective graph implemented with probability
'''
import random

def ugraph_probability(num_node, probability):
    '''
    Take the number of nodes, and the probability
    return a undirected graph as dictionary
    '''
    ugraph = {}
    
    #initial the set of edge
    for node in range(num_node):
        ugraph[node] = set([])
        
    for node in range(num_node):
        for value in range(node+1, num_node):
            if random.random() < probability:
                ugraph[node].add(value)
                ugraph[value].add(node)
                
    return ugraph
    
def test_up():
    ugraph = ugraph_probability(10, 0.5)
    print("test ugraph_probability: ")
    for key,value in ugraph.items():
        print(key, value)
        
def find_p():
    #find a probability, let edge approximately equal this
    NODES = 1347
    EDGES = 3112
    for p in range(340, 350):
        ugraph = ugraph_probability(NODES, p/100000.)
        print("p: %f, D-value of edges: %d" %(p/100000.,
        sum([len(value) for value in ugraph.values()]) / 2 - EDGES))
    #find p = 0.00345 
    
if __name__ == '__main__':
    find_p()