#!/usr/bin/env python
'''
Helper class for implementing efficient version
of UPA algorithm
'''
import random
from ugraph_compute import complete_ugraph

class UPATrial:
    '''
    Simple class to encapsulate optimizated trials for the UPA algorithm
    Maintains a list of node numbers with multiple instance of each number.
    The number of instance of each node number are
    in the same proportion as the desired probabilities
    
    Uses random.choice() to select a node number from this list for each trial
    '''
    def __init__(self, num_nodes):
        '''
        Initialize a UPATrial object corresponding to a
        complete graph with num_nodes nodes
        
        Note the initial list of node numbers has num_nodes copies of 
        each node number
        '''
        self._num_nodes = num_nodes
        self._node_numbers = [node for node in range(num_nodes) 
        for dummy_idx in range(num_nodes)]
        
    def run_trial(self, num_nodes):
        '''
        Conduct num_nodes trials using by applying random.choice()
        to the list if node numbers
        
        Update the list of node numbers so that each node number
        appears in correct ratio
        
        return set of nodes
        '''
        
        #compute the neighbors for the newly-created node
        new_node_neighbors = set([])
        for _ in range(num_nodes):
            new_node_neighbors.add(random.choice(self._node_numbers))
            
        #update the list of node numbers so that each node number
        #appears in the correct ratio
        self._node_numbers.append(self._num_nodes)
        
        for dummy_idx in range(len(new_node_neighbors)):
            self._node_numbers.append(self._num_nodes)
        self._node_numbers.extend(list(new_node_neighbors))
        
        #update the number of nodes
        self._num_nodes += 1
        return new_node_neighbors
        
def ugraph_UPA(num_nodes, m):
    ugraph = complete_ugraph(m)
    ugraph_ge = UPATrial(m)
    for item in range(m, num_nodes):
        ugraph[item] = ugraph_ge.run_trial(m)
        
    #make sure the edge is bothway
    for key,values in ugraph.items():
         for value in values:
             ugraph[value].add(key)
             
    return ugraph
        
def test_UPA():
    ugraph = ugraph_UPA(100, 10)
    print("test UPA:\n%s\n%s\n%s" %(ugraph[90], ugraph[6], ugraph[7]))
    
    
    
def find_m():
    NODES = 1347
    EDGES = 3112
    for m in range(1, 6):
        ugraph = ugraph_UPA(NODES, m)
        num_edge = sum([len(value) for value in ugraph.values()])
        print("m: %d, the difference: %d" %(m, num_edge-EDGES))
    #m = 2
    
if __name__ == '__main__':
    test_UPA()