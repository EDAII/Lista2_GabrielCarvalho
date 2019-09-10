def selection_sort(array, param):

    for i in range(len(array)): 
        
        low = i 
        for j in range(i+1, len(array)): 
            if array[low][param] > array[j][param]: 
                low = j 
                  
        array[i], array[low] = array[low], array[i]
    
    return array

def insertion_sort(array, param): 
  
    for i in range(1, len(array)): 
  
        key = array[i]
        j = i-1
        while (j >=0 and key[param] < array[j][param]): 
                array[j+1] = array[j]
                j -= 1
        array[j+1] = key 

    return array 

def bubble_sort(array, param):
    n = len(array)
 
    for i in range(n):

        for j in range(0, n-i-1):

            if array[j][param] > array[j+1][param] :
                array[j], array[j+1] = array[j+1], array[j]
            
    return array
