# ue1, Jack Heseltine
# 1.1

#prints all nodes in g in alphabetical order
def print_all_nodes(g): 
    nlist = [n for n in g['v']] # assuming a datastructure of dictionary for g
            # with vertices in a list in a dictionary, in the entry 'v'
            # and edges as tuples in a list, in the entry 'e' 
            #
            # ex. g = {'e': [('a','b'), ('a','c')], 'v': ['a','b','c']}
            #
    nlist.sort()
    print(nlist)

#adds the nodes start, start+1, start+2,….start+count-1 to the grapgh g
def add_nodes_(g, start, count): # g now assumed to hold numerical vertices, see sorting in # 1
                            # mixing alphanumerically would be a problem for the sorting part
    for i in range(start, start + count):
        g['v'].append(i)

#adds the nodes start, start+1, start+2,….start+count-1 to the graph
#as well as every possible edge between the new nodes
def add_nodes_connected(g, start, count): 
    new_nodes_start_idx = len(g['v'])
    for i in range(start, start + count):
        current_node_idx = len(g['v'])
        g['v'].append(i) # current node at index = current_node_idx
        for vertex_idx in range(new_nodes_start_idx,current_node_idx):
            g['e'].append((g['v'][current_node_idx],g['v'][vertex_idx]))

# example for 1
print('---- test example for 1 ----')
g = {'e': [('a','b'), ('a','c')], 'v': ['a','b','c']}
#print(g)
print_all_nodes(g)

# example for 2 
print('---- test example for 2 ----')
g = {'e': [(1,2), (1,3)], 'v': [1,2,3]} 
print_all_nodes(g)
add_nodes_(g,10,5)
print_all_nodes(g)
print(g)
# not connected

# example for 3 (compare to output from last print statement)
print('---- test example for 3 ----')
g = {'e': [(1,2), (1,3)], 'v': [1,2,3]} 
print(g)
# edge cases work fine:
#add_nodes_connected(g,10,1)
#add_nodes_connected(g,10,2)
add_nodes_connected(g,10,3)
print(g)