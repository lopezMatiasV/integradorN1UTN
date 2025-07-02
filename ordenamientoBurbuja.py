from tpIntegrador import createList
import random
import timeit
#Creamos los elementos a usar
list_10 = createList(10)
list_100 = createList(100)
num1 = random.choice(list_10)
num2 = random.choice(list_100)

#Ordenamiento por burbuja (Bubble Sort)
def bubleSort(list):
    for i in range(len(list)):
        for j in range(0, len(list) - i - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
    return list

#Test de tiempo
print("****************************************")
print("Ordenamiento por burbuja")
print("****************************************")
#Lista de 10 elementos
print(f"Lista de 10 elementos desordenada: ", list_10)
print("****************************************")
startTime = timeit.default_timer()
result = bubleSort(list_10)
endTime = timeit.default_timer()
print(f"Lista de 10 elementos ordenada:", result)
print("****************************************")
print(f"Tiempo de ejecucion 10 items: ", endTime - startTime)

#Lista de 100 elementos
print("****************************************")
print(f"Lista de 100 elementos desordenada: ", list_100)
print("****************************************")
startTime = timeit.default_timer()
result2 = bubleSort(list_100)
endTime = timeit.default_timer()
print(f"Lista de 100 elementos ordenada", result2)
print("****************************************")
print(f"Tiempo de ejecucion 100 items: ", endTime - startTime)