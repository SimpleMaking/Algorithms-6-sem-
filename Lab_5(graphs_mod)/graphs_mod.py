from gen_graphs import genGraphs
from random import randint
import itertools as it 


class GraphMod:
  
    def __init__(self, max_verts=100, max_edges=4950, max_pinned_edges_with_one_vert=20):
        self.__graph = genGraphs(max_verts=max_verts, max_edges=max_edges, max_pinned_edges_with_one_vert=max_pinned_edges_with_one_vert)
        self.__max_verts = max_verts
        self.__verts = list()
        # print(self.__graph)
        for i in range(max_verts):
            self.__verts.append(i) 
    
    def __getAdjaMatrix(self) -> list:                             
        self.__AdjaMatrix = list()
        for verts_list in self.__graph:
            curr_vert = list()
            for vert in self.__verts:
                if vert in verts_list:
                    curr_vert.append(randint(1, 20))
                else:
                    curr_vert.append(0)
            self.__AdjaMatrix.append(curr_vert)
    
    def __getEdgesList(self) -> list:
        self.__getAdjaMatrix()
        self.__EdgesList = list()
        counter = 0
        for verts_list in self.__graph:
            temp = list()
            for vert in verts_list:
                temp.append(self.__AdjaMatrix[counter][vert])
                temp.append(f"{self.__verts[counter]}-{vert}")
                self.__EdgesList.append(temp)  
                temp = list()
            counter += 1     
    
    def DeickAlg(self): 
        self.__getEdgesList()
        dif_ways = list(it.permutations(self.__verts, 2))   
        for cur_points in dif_ways:
            if cur_points[0] < cur_points[1]:   
                verts_labels = dict()
                visited_verts = dict()
                for i in range(self.__max_verts):
                    if i == cur_points[0]:
                        verts_labels[i] = 0
                    else:
                        verts_labels[i] = (float("inf"))
                    visited_verts[i] = False
                    
                for i in range(cur_points[0],  cur_points[1] + 1):
                    for neighboor in sorted(self.__graph[i]):
                        if visited_verts[neighboor] == False:
                            # находим нужное ребро
                            for elem in self.__EdgesList:
                                if f"{i}-{neighboor}" == elem[1]:
                                    cur_vert = elem[0]
                            if (verts_labels[i] + cur_vert) < verts_labels[neighboor]: 
                                verts_labels[neighboor] = verts_labels[i] + cur_vert
                            
                    visited_verts[i] = True
                
                # вывод кратчайшего пути 
                
                path = list()
                path.insert(0, cur_points[1])
                for i in range(cur_points[1], cur_points[0] - 1, -1):
                    for neighboor in self.__graph[i]:
                         # находим нужное ребро
                            for elem in self.__EdgesList:
                                if f"{neighboor}-{i}" == elem[1]:
                                    cur_vert = elem[0]
                            if (verts_labels[i] - cur_vert) == verts_labels[neighboor]:
                                path.insert(0, neighboor)
                print(path)
            else:
                for i in range(cur_points[1], cur_points[0] - 1, -1):
                    pass
        print("\n") 
        return dif_ways

p = GraphMod(6, 15, 3)
# g = p.__getAdjaMatrix()

print(p.DeickAlg())
# for v in g:
#     print(v, end="\n")