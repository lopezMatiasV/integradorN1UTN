from tpIntegrador import createList
import random
import timeit
#Creamos los elementos a usar
list_10 = createList(10)
list_100 = createList(100)
num1 = random.choice(list_10)
num2 = random.choice(list_100)

#Ordenamiento por mezcla (Merge Sort)
def mergeSort(list):
    if len(list) > 1:
        medium = len(list) // 2
        left = list[:medium]
        right = list[medium:]
        mergeSort(left)
        mergeSort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                list[k] = left[i]
                i += 1
            else:
                list[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            list[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            list[k] = right[j]
            j += 1
            k += 1
    return list

#Test de tiempo
print("****************************************")
print("Ordenamiento por mezcla")
print("****************************************")
#Lista de 10 elementos
print(f"Lista de 10 elementos desordenada: ", list_10)
print("****************************************")
startTime = timeit.default_timer()
result = mergeSort(list_10)
endTime = timeit.default_timer()
print(f"Lista de 10 elementos ordenada:", result)
print("****************************************")
print(f"Tiempo de ejecucion 10 items: ", endTime - startTime)

#Lista de 100 elementos
print("****************************************")
print(f"Lista de 100 elementos desordenada: ", list_100)
print("****************************************")
startTime = timeit.default_timer()
result2 = mergeSort(list_100)
endTime = timeit.default_timer()
print(f"Lista de 100 elementos ordenada", result2)
print("****************************************")
print(f"Tiempo de ejecucion 100 items: ", endTime - startTime)