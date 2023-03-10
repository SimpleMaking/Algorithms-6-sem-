import random
from copy import copy
import networkx as nx



# a, b, c, d, e, f, g, h = range(8)
# N = [
# 	{1, 2, 3, 4, 5}, # 0
# 	{2, 4}, # 1
# 	{3}, # 2
# 	{4}, # 3
# 	{5}, # 4
# 	{2, 6, 7}, # 5
# 	{5, 7}, # 6
# 	{5, 6} # 7
# ]


def gen_graphs(max_verts=20, max_edges=190, max_pinned_edges_with_one_vert=4, direct_graph=False):
    try:
        all_verts = list()
        for i in range(max_verts):
            all_verts.append(i) 
        n = list()
        if direct_graph:
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
        
        else:    
            G = nx.barabasi_albert_graph(n=max_verts, m=max_pinned_edges_with_one_vert, initial_graph=None)
            edges_ = list(G.edges)
            points_dict = dict()
            for i in range(max_verts):
                points_dict[i] = i
                
            vert_list = list(); temp = edges_[0][0]
            for tup in edges_:
                if temp == tup[0]:
                    vert_list.append(points_dict[tup[1]])
                else:
                    n.append(vert_list)
                    if abs(temp - tup[0]) > 1:
                        n.append(list())
                    vert_list = list()
                    vert_list.append(points_dict[tup[1]])  
                temp = tup[0]
                
            n.append(vert_list)
            while len(n) < max_verts:
                n.append(list())  

            for i in range(1, len(n)):
                for j in range(0, i):
                    if all_verts[i] in n[j]:
                        n[i].append(all_verts[j])
    except:
        pass
    if direct_graph:
        return n, "Направленный"
    else:
        return n, "Ненаправленный"
    
     
        

