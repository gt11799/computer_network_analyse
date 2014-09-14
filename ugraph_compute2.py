#!/usr/bin/env python
'''
ugraph compute module given
'''

def copy_graph(graph):
    #make a copy of graph
    new_graph = {}
    for node in graph:
        new_graph[node] = set(graph[node])
    return new_graph
    
def delete_node(ugraph, node):
    #delete a node from an undirected graph
    neighbors = ugraph[node]
    ugraph.pop(node)
    for neighbor in neighbors:
        ugraph[neighbor].remove(node)
        
def targeted_order(ugraph):
    '''
    Compute a targeted attack order consisting of
    nodes of maximal degree
    return a list nodes
    '''
    new_graph = copy_graph(ugraph)
    
    order = []
    while len(new_graph) > 0:
        max_degree = -1
        for node in new_graph:
            if len(new_graph[node]) > max_degree:
                max_degree = len(new_graph[node])
                max_degree_node = node
                
        delete_node(new_graph, max_degree_node)
        order.append(max_degree_node)
    return order
    
def degrees_ugraph(ugraph):
    '''
    Take a ugraph
    return {node : degree}
    '''
    degrees = {}
    for node in ugraph:
        degrees[node] = len(ugraph[node])
    return degrees 
    
def fast_targeted_order(ugraph):
    '''
    a fast way to return a list of the nodes 
    with descending order
    ''' 
    degrees = degrees_ugraph(ugraph)
    degree_sets = {}
    degree_max = max(degrees.values())
    for item in range(degree_max+1):
        degree_sets[item] = set([k for k,v in degrees.items() if v == item])
    
    L = []
    i = 0
    for k in range(degree_max, -1, -1):
        while degree_sets[k]:
            u = degree_sets[k].pop()
            for v in ugraph[u]:
                d = [key for key,value in degree_sets.items() if v in value][0]
                degree_sets[d].remove(v)
                degree_sets[d-1].add(v)
            
            L.append(u)
            i += 1
            delete_node(ugraph, u)
            
    return L
            
    
def test_targeted_order():
    #for test
    UGRAPH10 = {0:set([]), 1:set([2,3,4]), 2:set([1,3]), 3:set([1,2]), 
    4:set([1]), 5:set([6]), 6:set([5]), 7:set([])}
    print("test targeted graph: %s" %targeted_order(UGRAPH10))
    
    #test degrees of ugraph
    print("test degree: %s" %degrees_ugraph(UGRAPH10))

def test_fast_order():
    #for test
    UGRAPH10 = {0:set([]), 1:set([2,3,4]), 2:set([1,3]), 3:set([1,2]), 
    4:set([1]), 5:set([6]), 6:set([5]), 7:set([])}
    print("test fast targeted order: %s" %fast_targeted_order(UGRAPH10))
    
def test_to_ER():
    #test targeted_order with ugraph_ER
    from ER_ugraph import ugraph_probability
    ugraph = ugraph_probability(10, 0.4)
    print("test targeted graph: %s" %targeted_order(ugraph))

if __name__ == '__main__':
    #test_targeted_order()
    #test_fast_order()
    test_to_ER()