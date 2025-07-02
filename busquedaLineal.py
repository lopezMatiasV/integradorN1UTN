from tpIntegrador import createList
import random
import timeit

""" #Crear lista
def createList(cant):
    lista = [random.randint(1, 1000) for _ in range(cant)]
    return lista """

#Creamos los elementos a usar
list_10 = createList(10)
list_100 = createList(100)
num1 = random.choice(list_10)
num2 = random.choice(list_100)

#Buscar item (busqueda lineal)
def searchLineal (list, item):
    for i in range(len(list)):
        if list[i] == item:
            return i
    return -1

#Test de tiempo
print("****************************************")
print("Busqueda lineal")
print("****************************************")
#Lista de 10 elementos
print(f"Lista de 10 Elementos: ", list_10)
startTime = timeit.default_timer()
result = searchLineal(list_10, num1)
endTime = timeit.default_timer()
print(f"Numero buscado:", num1,", Ubicado en la posición:", result)
print(f"Tiempo de ejecucion 10 items: ", endTime - startTime)

#Lista de 100 elementos
print("****************************************")
print(f"Lista de 100 Elementos: ", list_100)
startTime = timeit.default_timer()
result2 =searchLineal(list_100, num2)
endTime = timeit.default_timer()
print(f"Numero buscado:", num2,", Ubicado en la posición:", result2)
print(f"Tiempo de ejecucion 100 items: ", endTime - startTime)