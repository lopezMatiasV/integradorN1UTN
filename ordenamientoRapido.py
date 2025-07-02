from tpIntegrador import createList
import random
import timeit
#Creamos los elementos a usar
list_10 = createList(10)
list_100 = createList(100)
num1 = random.choice(list_10)
num2 = random.choice(list_100)

#Ordenamiento rapido
def quickSort(list):
    if len(list) <= 1:
        return list
    else:
        pivot = list[0]
        less = [x for x in list[1:] if x <= pivot]
        greater = [x for x in list[1:] if x > pivot]
        return quickSort(less) + [pivot] + quickSort(greater)

#Test de tiempo
print("****************************************")
print("Ordenamiento rápido")
print("****************************************")
#Lista de 10 elementos
print(f"Lista de 10 elementos desordenada: ", list_10)
print("****************************************")
startTime = timeit.default_timer()
result = quickSort(list_10)
endTime = timeit.default_timer()
print(f"Lista de 10 elementos ordenada:", result)
print("****************************************")
print(f"Tiempo de ejecucion 10 items: ", endTime - startTime)

#Lista de 100 elementos
print("****************************************")
print(f"Lista de 100 elementos desordenada: ", list_100)
print("****************************************")
startTime = timeit.default_timer()
result2 = quickSort(list_100)
endTime = timeit.default_timer()
print(f"Lista de 100 elementos ordenada", result2)
print("****************************************")
print(f"Tiempo de ejecucion 100 items: ", endTime - startTime)