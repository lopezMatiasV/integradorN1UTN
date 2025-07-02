from tpIntegrador import createList
import random
import timeit
#Creamos los elementos a usar
list_10 = createList(10)
list_100 = createList(100)
num1 = random.choice(list_10)
num2 = random.choice(list_100)

#Ordenamiento de seleccion
def selectionSort(list):
    n = len(list)
    for i in range(n):
        minIndex = i
        for j in range(i+1, n):
            if list[j]< list[minIndex]:
                minIndex = j
        list[i], list[minIndex] = list[minIndex], list[i]
    return list

#Test de tiempo
print("****************************************")
print("Ordenamiento por selección")
print("****************************************")
#Lista de 10 elementos
print(f"Lista de 10 elementos desordenada: ", list_10)
print("****************************************")
startTime = timeit.default_timer()
result = selectionSort(list_10)
endTime = timeit.default_timer()
print(f"Lista de 10 elementos ordenada:", result)
print("****************************************")
print(f"Tiempo de ejecucion 10 items: ", endTime - startTime)

#Lista de 100 elementos
print("****************************************")
print(f"Lista de 100 elementos desordenada: ", list_100)
print("****************************************")
startTime = timeit.default_timer()
result2 = selectionSort(list_100)
endTime = timeit.default_timer()
print(f"Lista de 100 elementos ordenada", result2)
print("****************************************")
print(f"Tiempo de ejecucion 100 items: ", endTime - startTime)