import random
from copy import copy
import networkx as nx



# a, b, c, d, e, f, g, h = range(8)
# N = [
# 	{b, c, d, e, f}, # a
# 	{c, e}, # b
# 	{d}, # c
# 	{e}, # d
# 	{f}, # e
# 	{c, g, h}, # f
# 	{f, h}, # g
# 	{f, g} # h
# ]


def gen_graphs(max_verts=15, max_edges=105, max_pinned_edges_with_one_vert=5, direct_graph=True):
    try:
        all_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o"]
        ready_letts_for_graph = all_letters[:max_verts]
        n = list()
        if direct_graph:
            
            # a, b, c, d, e, f, g, h, i, j, k, l, m, n, o - max count
            edge_count = 0
            counter = 0
            while True:
                for i in range(max_verts):
                    edges = random.randint(0, max_pinned_edges_with_one_vert)
                    edge_count += edges
                    edges_list = list()
                    temp = copy(ready_letts_for_graph)
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
            points_dict = {0:"a", 1:"b", 2:"c", 3:"d", 4:"e", 5:"f", 6:"g", 7:"h", 8:"i", 9:"j", 10:"k", 11:"l", 12:"m", 13:"n", 14:"o"}
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
                    if ready_letts_for_graph[i] in n[j]:
                        n[i].append(ready_letts_for_graph[j])
    except:
        pass
    if direct_graph:
        return n, "Направленный"
    else:
        return n, "Ненаправленный"
    
        
        

