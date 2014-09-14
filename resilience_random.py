#!/usr/bin/env python

'''
Computer network, ugraph generated with probability, ugraph concentrate on some nodes,
whose resilience is better?
Let we test it
'''

import random
import pickle
from ugraph_compute import compute_resilience
from computer_network import load_graph
from ER_ugraph import ugraph_probability
from UPA_ugraph import ugraph_UPA
from matplotlib import pyplot as plt

NODES = 1347
EDGES = 3112
P = 0.00345
M = 1

def random_order(ugraph):
    #shuffle the nodes
    nodes = ugraph.keys()
    random.shuffle(nodes)
    return nodes
    
def test_ro():
    ugraph = ugraph_probability(10, 0.3)
    print random_order(ugraph)
    
def attack(ugraphs):
    '''
    simulate an attack to the given ugraph
    shuffle the nodes, and remove then one by one
    return the cc_size of the ugraph after removed the nodes.
    save the lists into a file.
    '''
    result = []
    for ugraph in ugraphs:
        nodes_random = random_order(ugraph)
        resilience = compute_resilience(ugraph, nodes_random)
        result.append(resilience)
    data_file = open('data_resilience.p', 'wb')
    pickle.dump(result, data_file)
    data_file.close()
    return 'data_resilience.p'
    
def test_attack():
    ugraph_network = load_graph('computer_network.txt')
    ugraph_ER = ugraph_probability(NODES, P)
    attack((ugraph_network, ugraph_ER))
    data_file = open('data_resilience.p', 'rb') 
    
    cc_set = pickle.load(data_file)
    data_file.close()
    print('test attack:')     
    print("cc_network length: %d, cc_er length: %d" %(len(cc_set[0]), len(cc_set[0])))
    print("cc_network: %s\n%s" %(cc_set[0][-6:], cc_set[0][:6]))    
    print("cc_er: %s\n%s" %(cc_set[1][-6:], cc_set[1][:6]))    
    
        
def plot_attack(file_name):
    '''
    plot the cc_size of the ugraph after attacked
    '''
    try:
        data_file = open(file_name, 'rb')
    except(IOError):
        print("please execute the attack function first.")
        return
    
    cc_sets = pickle.load(data_file)
    data_file.close()
    
    #define a figure
    fig = plt.figure(dpi=100)
    
    colors = ('r', 'b', 'y')
    names = ('Network', 'ER,P=%s'%P, 'UPA,M=%s'%M)
    
    foo = 0
    for cc_set in cc_sets:
        x = range(len(cc_sets[foo]))
        plt.plot(x, cc_sets[foo], colors[foo], label=names[foo])
        foo += 1
    
    plt.legend(loc='best')    
    plt.title('Resilience with attack')
    plt.xlabel('Number of Nodes Removed')
    plt.ylabel('Size of the Largest Connect Component')
    
    plt.savefig('resilience_random.png', dpi=120)
    plt.show()
    
if __name__ == '__main__':
    #ugraph_network = load_graph('computer_network.txt')
    #ugraph_ER = ugraph_probability(NODES, P)
    #ugraph_UPA = ugraph_UPA(NODES, M)
    
    #set default file name
    file_name = 'data_resilience.p'
    #file_name = attack((ugraph_network, ugraph_ER, ugraph_UPA))
    plot_attack(file_name)
    
    