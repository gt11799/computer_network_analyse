#!/usr/bin/env python

'''
load graph from a txt
'''

def load_graph(file_name):
    '''
    load a graph with given file,
    return a dictionary that models a graph
    '''
    graph_file = open(file_name, 'r')
    graph_text = graph_file.read()
    graph_lines = graph_text.split('\n')
    graph_file.close()
    
    print("Loaded graph with %s nodes" %len(graph_lines))
    
    answer_graph = {}
    for line in graph_lines:
        neighbors = line.split(' ')
        node = int(neighbors[0])
        answer_graph[node] = set([])
        for neighbor in neighbors[1 : -1]:
            answer_graph[node].add(int(neighbor))
            
    return answer_graph
        
def test_load():
    graph = load_graph('computer_network.txt')
    print("load a graph with %s nodes, %s edges" 
    %(len(graph.keys()), sum([len(value) for value in graph.values()]) / 2))
    for item in [1,2,3,4,len(graph)-1]:
        print("%s: %s" %(item, graph[item]))
        
if __name__ == "__main__":
    test_load()