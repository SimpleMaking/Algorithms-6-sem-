from main import gen_graphs
import copy
import random
import time
import matplotlib.pyplot as plt


class Graph:
    
    def __init__(self, max_verts=15, max_edges=105, max_pinned_edges_with_one_vert=5, direct_graph=False):
        self.__graph, self.__direction = gen_graphs(max_verts=max_verts, max_edges=max_edges, max_pinned_edges_with_one_vert=max_pinned_edges_with_one_vert, direct_graph=direct_graph)
        self.__verts = list()
        for i in range(max_verts):
            self.__verts.append(i) 
        self.__graph_for_alg = dict()
        self.__queue = list()
        # self.__level = dict()
        # for i in range(max_verts):
        #     self.__level[self.__verts[i]] = -1
        counter = 0
        for verts_list in self.__graph:
            self.__graph_for_alg[self.__verts[counter]] = verts_list
            counter += 1
        self.__ways = list()
    
    def getAdjaMatrix(self) -> list:
        self.__AdjaMatrix = list()
        for verts_list in self.__graph:
            curr_vert = list()
            for vert in self.__verts:
                if vert in verts_list:
                    curr_vert.append(1)
                else:
                    curr_vert.append(0)
            self.__AdjaMatrix.append(curr_vert)
        return self.__AdjaMatrix
    
    def getIncidenceMatrix(self) -> list:
        IncidMatrix = self.getAdjaMatrix()
        counter = 0
        for i in range(len(IncidMatrix)):
            IncidMatrix[i].pop(counter)
            counter += 1 

        j_itter = 0
        for i in range(len(self.__verts)):
            counter = 1
            for j in range(j_itter, len(IncidMatrix[0])):
                if IncidMatrix[i][j] == 1:
                    IncidMatrix[i + counter][j_itter] = -1
                counter += 1
            counter = 1
            j_itter += 1
        self.__IncidenceMatrix = IncidMatrix
        return self.__IncidenceMatrix
        
    def getAdjaList(self) -> list:
        return self.__graph 
    
    def getEdgesList(self) -> list:
        self.__EdgesList = list()
        if self.__direction == "Направленный":
            counter = 0
            for verts_list in self.__graph:
                for vert in verts_list:
                    self.__EdgesList.append(f"{self.__verts[counter]}-{vert}")
                counter += 1
        else:
            counter = 0
            for verts_list in self.__graph:
                for vert in verts_list:
                    temp = f'{vert}-{self.__verts[counter]}'
                    if temp not in self.__EdgesList:
                        self.__EdgesList.append(f'{self.__verts[counter]}-{vert}')
                counter += 1
        return self.__EdgesList       
            
    def depthFirstSearch(self, start, end, visited, path):
         # Пометить текущий узел как посещенный и сохранить в path
        visited[list(self.__graph_for_alg.keys()).index(start)] = True
        path.append(start)

        # Если текущая вершина совпадает с точкой назначения, то
        if start == end:
            obj = copy.copy(path)
            self.__ways.append(obj)
        else:
            # Если текущая вершина не является пунктом назначения
            # Повторить для всех вершин, смежных с этой вершиной
            for i in self.__graph_for_alg[start]:
                if visited[list(self.__graph_for_alg.keys()).index(i)] == False:
                    self.depthFirstSearch(i, end, visited, path)

        # Удалить текущую вершину из path[] и пометить ее как непосещенную
        path.pop()
        visited[list(self.__graph_for_alg.keys()).index(start)] = False 

    def breadthFirstSearch(self, visited, start, end, path):
        visited.append(start)
        self.__queue.append(start)
        while self.__queue:
            s = self.__queue.pop(0)
            
            if s == end:
                return path
        
            for neighbour in self.__graph_for_alg[s]:
                if neighbour not in visited:
                    path[neighbour] = path[s] + 1
                    visited.append(neighbour)
                    self.__queue.append(neighbour)
        return dict()
    
    def get_ways(self):
        return self.__ways


def main(): 
    max_letters = list()
    for i in range(20):
            max_letters.append(i)   
    verts_count = 11
    edges_count = verts_count * (verts_count - 1) / 2
    verts = list(); times_d = list(); times_b = list()
    for i in range(1, 11):
          
        if verts_count == 20:  
            verts.append(verts_count)      
            p = Graph(20, 190, 4, True)
            start = time.time() * 1000
            p.depthFirstSearch(random.choice(max_letters), random.choice(max_letters), [False]*20, [])
            end = float(time.time() * 1000) - start
            times_d.append(end)
            ways = p.get_ways()
            print(f"количество вершин: {verts_count}")
            print(f"тест {i}: поиск в глубину")
            if len(ways) < 1:
                print("невозможно найти путь")
            else:
                ways_ = list()
                for way in ways:
                    ways_.append(len(way))
                res = min(ways_) - 1 
                if res:
                    print(f"минимальный путь: {res}")
                else:
                    print("невозможно найти путь")
                print(f"время выполнения: {end}")
            
            start_vert = random.choice(max_letters[:verts_count])
            end_init = random.choice(max_letters[:verts_count])
            start = time.time() * 1000
            values = p.breadthFirstSearch([], start=start_vert, end=end_init, path={start_vert:0})
            time.sleep(0.0001)
            end = float(time.time() * 1000) - start - 0.0001
            times_b.append(end)
            print(f"тест {i}: поиск в ширину")
            try:
                if values[end_init]:
                    print(f"минимальный путь: {values[end_init]}")
                else:
                    print("невозможно найти путь")
            except KeyError:
                print("невозможно найти путь")
            print(f"время выполнения: {end}\n")
            
        else:
            verts.append(verts_count) 
            p = Graph(verts_count, edges_count, 3, False)
            start = time.time() * 1000
            p.depthFirstSearch(random.choice(max_letters[:verts_count]), random.choice(max_letters[:verts_count]), [False]*verts_count, [])
            end = float(time.time() * 1000) - start
            times_d.append(end)
            ways = p.get_ways()
            print(f"количество вершин: {verts_count}")
            print(f"тест {i}: поиск в глубину")
            if len(ways) < 1:
                print("невозможно найти путь")
            else:
                ways_ = list()
                for way in ways:
                    ways_.append(len(way))
                res = min(ways_) - 1 
                if res:
                    print(f"минимальный путь: {res}")
                else:
                    print("невозможно найти путь")
                print(f"время выполнения: {end}")
                
            start_vert = random.choice(max_letters[:verts_count])
            end_init = random.choice(max_letters[:verts_count])
            start = time.time() * 1000
            values = p.breadthFirstSearch([], start=start_vert, end=end_init, path={start_vert:0})
            time.sleep(0.0001)
            end = float(time.time() * 1000) - start - 0.0001
            times_b.append(end)
            print(f"тест {i}: поиск в ширину")
            try:
                if values[end_init]:
                    print(f"минимальный путь: {values[end_init]}")
                else:
                    print("невозможно найти путь")
            except KeyError:
                print("невозможно найти путь")
            print(f"время выполнения: {end}\n")
        
        if verts_count != 20:
            verts_count += 1
            edges_count = verts_count * (verts_count - 1) / 2
    
    plt.grid(True)
    plt.title("Поиск путей в графах")
    plt.xlabel("Количество точек")
    plt.ylabel("время выполнения алгоритма")
    plt.plot(verts, times_d, '-', label="Поиск в глубину")
    plt.plot(verts, times_b, '--', label="Поиск в ширину")
    plt.legend()
    plt.show()    
    
    
main()           
    
