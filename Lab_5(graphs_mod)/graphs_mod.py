from gen_graphs import genGraphs
from random import randint
import itertools as it 
from sort import sorting
from operator import itemgetter
import time 
import matplotlib.pyplot as plt

class GraphMod:
  
    def __init__(self, max_verts=100, max_edges=4950, max_pinned_edges_with_one_vert=20):
        self.__graph = genGraphs(max_verts=max_verts, max_edges=max_edges, max_pinned_edges_with_one_vert=max_pinned_edges_with_one_vert)
        self.__max_verts = max_verts
        self.__verts = list()
        for i in range(self.__max_verts):
            self.__verts.append(i) 

    def __getAdjaMatrix(self) -> list:
        self.__AdjaMatrix = list()
        for verts_list in self.__graph:
            curr_vert = list()
            for vert in self.__verts:
                if vert in verts_list:
                    curr_vert.append(21)
                else:
                    curr_vert.append(0)
            self.__AdjaMatrix.append(curr_vert)
        
        counter = 0
        for i in range(len(self.__AdjaMatrix)):
            self.__AdjaMatrix[i].pop(counter)
            counter += 1 
            
        j_itter = 0
        for i in range(len(self.__verts)):
            counter = 1
            for j in range(j_itter, len(self.__AdjaMatrix[0])):
                if self.__AdjaMatrix[i][j] == 21:
                    val_weig = randint(1, 20)
                    self.__AdjaMatrix[i][j] = val_weig
                    self.__AdjaMatrix[i + counter][j_itter] = val_weig
                counter += 1
            counter = 1
            j_itter += 1
            
        counter = 0
        for i in range(len(self.__AdjaMatrix)):
            self.__AdjaMatrix[i].insert(counter, 0)
            counter += 1 
    
    def __getEdgesList(self) -> list:
        self.__getAdjaMatrix()
        self.__EdgesList = list()
        counter = 0
        for verts_list in self.__graph:
            temp_list = list()
            for vert in verts_list:
                temp_list.append(self.__AdjaMatrix[counter][vert])
                temp_list.append(f'{self.__verts[counter]}-{vert}')
                self.__EdgesList.append(temp_list)
                temp_list = list()
            counter += 1
                    
    def DeickAlg(self): 
        self.__getEdgesList()
        print("Матрица смежности:")
        for v in self.__AdjaMatrix:
            print(v, end="\n")
        print("\n")
        iter_list = list()
        temp = list()
        counter = 0
        dif_ways = list(it.combinations(self.__verts, 2))   
        for way in dif_ways:
            if counter != way[0]:
                iter_list.append(temp)
                counter += 1
                temp = list()
            temp.append(way)   
        if temp:
            iter_list.append(temp)
 
        for cur_ways in iter_list:
            curr_vert = cur_ways[0][0]
            verts_labels = dict()
            visited_verts = dict()
            for i in range(self.__max_verts):
                if i == curr_vert:
                    verts_labels[i] = 0
                else:
                    verts_labels[i] = float("inf")
                visited_verts[i] = False

        
            while False in list(visited_verts.values()):
                
                if visited_verts[curr_vert] == False:
                    edges_list_for_search_min = list()
                    for neighboor in self.__graph[curr_vert]:
                        cur_list = list()
                        if visited_verts[neighboor] == False:
                            # находим нужное ребро
                            for elem in self.__EdgesList:
                                if f"{curr_vert}-{neighboor}" == elem[1]:
                                    cur_list.append(elem[1].split('-')[1])
                                    cur_list.append(elem[0])
                            edges_list_for_search_min.append(cur_list)
                
                    # сортируем наши пути до связанных вершин
        
                    if edges_list_for_search_min:
                        sorted_edges_list = sorting(edges_list_for_search_min, len(edges_list_for_search_min))
                        for neighbor_after_sort in sorted_edges_list:
                            if visited_verts[int(neighbor_after_sort[0])] == False:
                                if (verts_labels[curr_vert] + neighbor_after_sort[1]) < verts_labels[int(neighbor_after_sort[0])]: 
                                    verts_labels[int(neighbor_after_sort[0])] = verts_labels[curr_vert] + neighbor_after_sort[1]
                         
                    visited_verts[curr_vert] = True     
                    for_next_vert_dict = dict()
                    for vert_for_next in sorted_edges_list:
                        for_next_vert_dict[int(vert_for_next[0])] = verts_labels[int(vert_for_next[0])]
                    
                    for_next_vert_dict_sd = dict(sorted(for_next_vert_dict.items(), key=itemgetter(1)))
                
                    for vert_for_next in for_next_vert_dict_sd.items():
                        if visited_verts[int(vert_for_next[0])] == False:
                            curr_vert = vert_for_next[0]
                            break
                  
            # вывод кратчайшего пути 

            for cur_points in cur_ways:   
               
                path = list()
                path_len = 0
                path.insert(0, cur_points[1])
                curr_vert_val = cur_points[1]
        
                while (curr_vert_val != cur_points[0]):
                    
                    for neighbor in self.__graph[curr_vert_val]:
                            # находим нужное ребро
                            for elem in self.__EdgesList:
                                if f"{curr_vert_val}-{neighbor}" == elem[1]:
                                    cur_vert = elem[0]
                            if (verts_labels[curr_vert_val] - cur_vert) == verts_labels[neighbor]:
                                path.insert(0, neighbor)
                                curr_vert_val = neighbor
                                path_len += cur_vert
                                break 
                print(f"путь: {path} его длина: {path_len}")  
                       
            
        print("\n") 


def main():
    vert_count_x = list()
    lost_time_y = list()
    verts_count = [6, 10, 20, 50]
    edges_count = [15, 45, 190, 1225]
    pinned_verts = [4, 7, 17, 45]
    for i in range(len(verts_count)):
        vert_count_x.append(verts_count[i])
        p = GraphMod(verts_count[i], edges_count[i], pinned_verts[i])
        start = time.time() * 1000
        p.DeickAlg()
        time.sleep(0.0001)
        end = float(time.time() * 1000) - start - 0.0001
        lost_time_y.append(end)

    plt.grid(True)
    plt.title("Поиск путей в графах")
    plt.xlabel("Количество точек")
    plt.ylabel("время выполнения алгоритма")
    plt.plot(vert_count_x, lost_time_y, '-', label="График работы алгоритма")
    plt.legend()
    plt.show()    
    
main()