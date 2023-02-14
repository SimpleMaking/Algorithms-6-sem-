import matplotlib.pyplot as plt

def func():

    min_graph = list()
    max_graph = list()
    avg_graph = list()
    points_x = list()

    with open("output.txt", "r") as file:
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

def func_matplot_print():
  
    points_x, min_graph, max_graph, avg_graph = func()
    

    plt.grid(True)
    plt.title("Лучший, худший и средний случаи")
    plt.xlabel("N")
    plt.ylabel("Время в милисекундах")
    plt.plot(points_x, min_graph, '-', label="Лучший случай")
    plt.plot(points_x, max_graph, '--', label="Худший случай")
    plt.plot(points_x, avg_graph, '-.', label="Среднее время") 
    plt.legend()
    plt.show()    

func_matplot_print()