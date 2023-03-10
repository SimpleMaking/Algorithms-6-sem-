import random
from copy import copy


def genGraphs(max_verts=100, max_edges=4950, max_pinned_edges_with_one_vert=20):
    try:
        all_verts = list()
        for i in range(max_verts):
            all_verts.append(i) 
        n = list()
 
        edge_count = 0
        counter = 0
        while True:
            for i in range(max_verts):
                edges = random.randint(0, max_pinned_edges_with_one_vert)
                edge_count += edges
                edges_list = list()
                temp = copy(all_verts)
                temp.pop(counter)
                temp_list = temp
                for j in range(edges):
                    edge = random.choice(temp_list)
                    while True:
                        if not edge in edges_list:
                            edges_list.append(edge)
                            break
                        else:
                            edge = random.choice(temp_list)
                                
                n.append(edges_list)
                counter += 1
                    
            if edge_count > max_edges:
                n = list()
                edge_count = 0
                counter = 0
            else:
                break
            
    except:
        pass
    return n
