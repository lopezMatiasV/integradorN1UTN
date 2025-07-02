from tpIntegrador import searchBinary, orderList, createList
import random
import timeit
#Creamos los elementos a usar
list_10 = createList(10)
list_100 = createList(100)
num1 = random.choice(list_10)
num2 = random.choice(list_100)

#Busqueda binaria
def searchBinary(list, item):
    newList = orderList(list)
    print(f"Lista ordenada: ", newList)
    start = 0
    fin = len(newList) - 1
    while start <= fin:
        medio = (start + fin) // 2
        if newList[medio] == item:
            return medio
        elif newList[medio] < item:
            start = medio + 1
        else:
            fin = medio - 1
    return -1

#Test de tiempo
print("****************************************")
print("Busqueda binaria")
print("****************************************")
#Lista de 10 elementos
print(f"Lista de 10 Elementos: ", list_10)
startTime = timeit.default_timer()
result = searchBinary(list_10, num1)
endTime = timeit.default_timer()
print(f"Numero buscado:", num1,", Ubicado en la posición:", result)
print(f"Tiempo de ejecucion 10 items: ", endTime - startTime)

#Lista de 100 elementos
print("****************************************")
print(f"Lista de 100 Elementos: ", list_100)
startTime = timeit.default_timer()
result2 =searchBinary(list_100, num2)
endTime = timeit.default_timer()
print(f"Numero buscado:", num2,", Ubicado en la posición:", result2)
print(f"Tiempo de ejecucion 100 items: ", endTime - startTime)