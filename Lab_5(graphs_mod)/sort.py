def sorting(edges_list, count_of_elements):
    min = edges_list[0][1]
    count = 0; k1 = 0; k2 = 0
    for k in range(count_of_elements - 1):
        if count:
            k1 = k
            k2 = k
            min = edges_list[k][1]
            
        for k1 in range(k1, count_of_elements):
            if edges_list[k1][1] < min:
                k2 = k1
                min = edges_list[k1][1]
            
        promejyt = edges_list[k]
        
        edges_list[k] = edges_list[k2]
        edges_list[k2] = promejyt
        count = count + 1	
        k1 = 0
    return edges_list