from tpIntegrador import createList
import random
import timeit
#Creamos los elementos a usar
list_10 = createList(10)
list_100 = createList(100)
num1 = random.choice(list_10)
num2 = random.choice(list_100)

#Ordenamiento por inserción
def insertionSort(list):
    for i in range(1, len(list)):
        key = list[i]
        j = i - 1
        while j >= 0 and key < list[j]:
            list[j+1] = list[j]
            j -= 1
        list[j+1] = key
    return list

#Test de tiempo
print("****************************************")
print("Ordenamiento por inserción")
print("****************************************")
#Lista de 10 elementos
print(f"Lista de 10 elementos desordenada: ", list_10)
print("****************************************")
startTime = timeit.default_timer()
result = insertionSort(list_10)
endTime = timeit.default_timer()
print(f"Lista de 10 elementos ordenada:", result)
print("****************************************")
print(f"Tiempo de ejecucion 10 items: ", endTime - startTime)

#Lista de 100 elementos
print("****************************************")
print(f"Lista de 100 elementos desordenada: ", list_100)
print("****************************************")
startTime = timeit.default_timer()
result2 = insertionSort(list_100)
endTime = timeit.default_timer()
print(f"Lista de 100 elementos ordenada", result2)
print("****************************************")
print(f"Tiempo de ejecucion 100 items: ", endTime - startTime)