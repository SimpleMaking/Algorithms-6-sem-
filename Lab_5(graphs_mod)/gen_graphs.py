import networkx as nx

def genGraphs(max_verts=100, max_edges=4950, max_pinned_edges_with_one_vert=20):
    try:
        all_verts = list()
        for i in range(max_verts):
            all_verts.append(i) 
        n = list()
        G = nx.watts_strogatz_graph(n=max_verts, k=max_pinned_edges_with_one_vert, p=0.01)
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
    return n
