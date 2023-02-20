import matplotlib.pyplot as plt
import math

def func(filename):

    min_graph = list()
    max_graph = list()
    avg_graph = list()
    points_x = list()

    with open(filename, "r") as file:
        list_of_data = file.readlines()
        for i in range(len(list_of_data)):
            if list_of_data[i][len(list_of_data[i]) - 1] == "\n" or list_of_data[i][len(list_of_data[i]) - 1] == " ":
                list_of_data[i] = list_of_data[i][0:len(list_of_data[i]) - 1].strip()

        list_of_data.remove('N min max avg')
        for str in list_of_data:
            str = str.split()
            points_x.append(int(str[0]))
            min_graph.append(float(str[1]))
            max_graph.append(float(str[2]))
            avg_graph.append(float(str[3]))
            

    return points_x, min_graph, max_graph, avg_graph

def func_matplot_print(graph_name, filename):
  
    points_x, min_graph, max_graph, avg_graph = func(filename)
    c = 0.1
    addit_graph = list()
    for value in points_x:
        addit_graph.append(c * value * math.log(value))

    plt.grid(True)
    plt.title(graph_name)
    plt.xlabel("N")
    plt.ylabel("Колличество вызовов рекурсивной функции")
    plt.plot(points_x, min_graph, '-', label="Лучший случай")
    plt.plot(points_x, max_graph, '--', label="Худший случай")
    plt.plot(points_x, avg_graph, '-.', label="Среднее время") 
    plt.plot(points_x, addit_graph, '-*', label="c * n * log(n)") 
    plt.legend()
    plt.show()    

func_matplot_print("график для отсортированного изначально", "output_1.txt")
func_matplot_print("график для массива из одинаковых элементов", "output_2.txt")
func_matplot_print("график для массива с максимальным количеством сравнений при выборе среднего элемента в качестве опорного", "output_3.txt")
func_matplot_print("график для массива из случайных элементов", "output_4.txt")