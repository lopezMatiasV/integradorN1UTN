#Librerias
import random
import timeit

#Crear lista
def createList(cant):
    lista = [random.randint(1, 1000) for _ in range(cant)]
    return lista

#Ordenar lista
def orderList (list):
    return sorted(list)

#Buscar item (busqueda lineal)
def searchItem (list, item):
    for i in range(len(list)):
        if list[i] == item:
            return i
    return -1
#Test de tiempo
""" print("Busqueda lineal")
startTime = timeit.default_timer()
searchItem(createList(10), random.choice(listNumbers))
endTime = timeit.default_timer()
print(f"Tiempo de ejecucion 10 items: ", endTime - startTime)
print("****************************************")
startTime = timeit.default_timer()
searchItem(createList(100), random.choice(listNumbers))
endTime = timeit.default_timer()
print(f"Tiempo de ejecucion 100 items: ", endTime - startTime) """


#Busqueda binaria
def searchBinary(list, item):
    newList = orderList(list)
    #print(f"Lista ordenada: ", newList)
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

#Test tiempo
""" print("Busqueda binaria")
startTime = timeit.default_timer()
searchBinary(createList(10), random.choice(listNumbers))
endTime = timeit.default_timer()
print(f"Tiempo de ejecucion 10 items: ", endTime - startTime)
print("****************************************")
startTime = timeit.default_timer()
searchBinary(createList(1000), random.choice(listNumbers))
endTime = timeit.default_timer()
print(f"Tiempo de ejecucion 1000 items: ", endTime - startTime) """

#Ordenamiento por burbuja (Bubble Sort)
def bubleSort(list):
    for i in range(len(list)):
        for j in range(0, len(list) - i - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
    return list

#Test tiempo
""" print("Ordenamiento por burbuja")
startTime = timeit.default_timer()
print(bubleSort(createList(10)))
endTime = timeit.default_timer()
print(f"Tiempo de ejecucion 10 items: ", endTime - startTime)
print("****************************************")
startTime = timeit.default_timer()
print(bubleSort(createList(1000)))
endTime = timeit.default_timer()
print(f"Tiempo de ejecucion 1000 items: ", endTime - startTime) """

#Ordenamiento por insercion
def insertionSort(list):
    for i in range(1, len(list)):
        key = list[i]
        j = i - 1
        while j >= 0 and key < list[j]:
            list[j+1] = list[j]
            j -= 1
        list[j+1] = key
    #print(list)

#Test tiempo
""" print("Ordenamiento por insercion")
startTime = timeit.default_timer()
insertionSort(createList(10))
endTime = timeit.default_timer()
print("Tiempo de ejecucion 10 items lista desordenada: ", endTime - startTime)
print("****************************************")
startTime = timeit.default_timer()
insertionSort(orderList(createList(10)))
endTime = timeit.default_timer()
print("Tiempo de ejecucion 10 items lista ordenada: ", endTime - startTime)
print("****************************************")
startTime = timeit.default_timer()
insertionSort(createList(1000))
endTime = timeit.default_timer()
print("Tiempo de ejecucion 1000 items lista desordenada: ", endTime - startTime)
print("****************************************")
startTime = timeit.default_timer()
insertionSort(orderList(createList(1000)))
endTime = timeit.default_timer()
print("Tiempo de ejecucion 1000 items lista ordenada: ", endTime - startTime) """

#Ordenamiento de seleccion
def selectionSort(list):
    n = len(list)
    for i in range(n):
        minIndex = i
        for j in range(i+1, n):
            if list[j]< list[minIndex]:
                minIndex = j
        list[i], list[minIndex] = list[minIndex], list[i]
    #print(list)

#Test tiempo
""" print("Ordenamiento por seleccion")
startTime = timeit.default_timer()
selectionSort(createList(10))
endTime = timeit.default_timer()
print("Tiempo de ejecucion 10 items lista desordenada: ", endTime - startTime)
print("****************************************")
startTime = timeit.default_timer()
selectionSort(orderList(createList(10)))
endTime = timeit.default_timer()
print("Tiempo de ejecucion 10 items lista ordenada: ", endTime - startTime)
print("****************************************")
startTime = timeit.default_timer()
selectionSort(createList(100))
endTime = timeit.default_timer()
print("Tiempo de ejecucion 1000 items lista desordenada: ", endTime - startTime)
print("****************************************")
startTime = timeit.default_timer()
selectionSort(orderList(createList(100)))
endTime = timeit.default_timer()
print("Tiempo de ejecucion 1000 items lista ordenada: ", endTime - startTime) """

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

#Test tiempo
""" print("Ordenamiento por seleccion")
startTime = timeit.default_timer()
mergeSort(createList(10))
endTime = timeit.default_timer()
print("Tiempo de ejecucion 10 items lista desordenada: ", endTime - startTime)
print("****************************************")
startTime = timeit.default_timer()
mergeSort(orderList(createList(10)))
endTime = timeit.default_timer()
print("Tiempo de ejecucion 10 items lista ordenada: ", endTime - startTime)
print("****************************************")
startTime = timeit.default_timer()
mergeSort(createList(100))
endTime = timeit.default_timer()
print("Tiempo de ejecucion 1000 items lista desordenada: ", endTime - startTime)
print("****************************************")
startTime = timeit.default_timer()
mergeSort(orderList(createList(100)))
endTime = timeit.default_timer()
print("Tiempo de ejecucion 1000 items lista ordenada: ", endTime - startTime) """

#Ordenamiento rapido
def quickSort(list):
    if len(list) <= 1:
        return list
    else:
        pivot = list[0]
        less = [x for x in list[1:] if x <= pivot]
        greater = [x for x in list[1:] if x > pivot]
        return quickSort(less) + [pivot] + quickSort(greater)

#Test tiempo
""" print("Ordenamiento rapido")
startTime = timeit.default_timer()
quickSort(createList(10))
endTime = timeit.default_timer()
print("Tiempo de ejecucion 10 items lista desordenada: ", endTime - startTime)
print("****************************************")
startTime = timeit.default_timer()
quickSort(orderList(createList(10)))
endTime = timeit.default_timer()
print("Tiempo de ejecucion 10 items lista ordenada: ", endTime - startTime)
print("****************************************")
startTime = timeit.default_timer()
quickSort(createList(100))
endTime = timeit.default_timer()
print("Tiempo de ejecucion 1000 items lista desordenada: ", endTime - startTime)
print("****************************************")
startTime = timeit.default_timer()
quickSort(orderList(createList(100)))
endTime = timeit.default_timer()
print("Tiempo de ejecucion 1000 items lista ordenada: ", endTime - startTime) """

#Listas pequeñas
#Test tiempo
""" print("Comparacion de ordenaminetos listas pequeñas")
#Burbuja
print("Ordenamiento por burbuja")
startTime = timeit.default_timer()
bubleSort(createList(10))
endTime = timeit.default_timer()
print(f"Tiempo de ejecucion 10 items: ", endTime - startTime)
print("****************************************")
#Insercion
print("Ordenamiento por insercion")
startTime = timeit.default_timer()
insertionSort(createList(10))
endTime = timeit.default_timer()
print("Tiempo de ejecucion 10 items lista desordenada: ", endTime - startTime)
print("****************************************")
startTime = timeit.default_timer()
insertionSort(orderList(createList(10)))
endTime = timeit.default_timer()
print("Tiempo de ejecucion 10 items lista ordenada: ", endTime - startTime)
print("****************************************")
#Seleccion
print("Ordenamiento por seleccion")
startTime = timeit.default_timer()
selectionSort(createList(10))
endTime = timeit.default_timer()
print("Tiempo de ejecucion 10 items lista desordenada: ", endTime - startTime)
print("****************************************")
startTime = timeit.default_timer()
selectionSort(orderList(createList(10)))
endTime = timeit.default_timer()
print("Tiempo de ejecucion 10 items lista ordenada: ", endTime - startTime)
print("****************************************")
#Mezcla
print("Ordenamiento por Mezcla")
startTime = timeit.default_timer()
mergeSort(createList(10))
endTime = timeit.default_timer()
print("Tiempo de ejecucion 10 items lista desordenada: ", endTime - startTime)
print("****************************************")
startTime = timeit.default_timer()
mergeSort(orderList(createList(10)))
endTime = timeit.default_timer()
print("Tiempo de ejecucion 10 items lista ordenada: ", endTime - startTime)
print("****************************************")
#Rapido
print("Ordenamiento rapido")
startTime = timeit.default_timer()
quickSort(createList(10))
endTime = timeit.default_timer()
print("Tiempo de ejecucion 10 items lista desordenada: ", endTime - startTime)
print("****************************************")
startTime = timeit.default_timer()
quickSort(orderList(createList(10)))
endTime = timeit.default_timer()
print("Tiempo de ejecucion 10 items lista ordenada: ", endTime - startTime)
print("****************************************") """

#Listas Grandes
#Test tiempo
""" print("Comparacion de ordenaminetos listas grandes")
#Burbuja
print("Ordenamiento por burbuja")
startTime = timeit.default_timer()
bubleSort(createList(1000))
endTime = timeit.default_timer()
print(f"Tiempo de ejecucion 1000 items: ", endTime - startTime)
print("****************************************")
#Insercion
print("Ordenamiento por insercion")
startTime = timeit.default_timer()
insertionSort(createList(1000))
endTime = timeit.default_timer()
print("Tiempo de ejecucion 1000 items lista desordenada: ", endTime - startTime)
print("****************************************")
startTime = timeit.default_timer()
insertionSort(orderList(createList(1000)))
endTime = timeit.default_timer()
print("Tiempo de ejecucion 1000 items lista ordenada: ", endTime - startTime)
print("****************************************")
#Seleccion
print("Ordenamiento por seleccion")
startTime = timeit.default_timer()
selectionSort(createList(1000))
endTime = timeit.default_timer()
print("Tiempo de ejecucion 1000 items lista desordenada: ", endTime - startTime)
print("****************************************")
startTime = timeit.default_timer()
selectionSort(orderList(createList(1000)))
endTime = timeit.default_timer()
print("Tiempo de ejecucion 1000 items lista ordenada: ", endTime - startTime)
print("****************************************")
#Mezcla
print("Ordenamiento por mezcla")
startTime = timeit.default_timer()
mergeSort(createList(1000))
endTime = timeit.default_timer()
print("Tiempo de ejecucion 1000 items lista desordenada: ", endTime - startTime)
print("****************************************")
startTime = timeit.default_timer()
mergeSort(orderList(createList(1000)))
endTime = timeit.default_timer()
print("Tiempo de ejecucion 1000 items lista ordenada: ", endTime - startTime)
print("****************************************")
#Rapido
print("Ordenamiento rapido")
startTime = timeit.default_timer()
quickSort(createList(1000))
endTime = timeit.default_timer()
print("Tiempo de ejecucion 1000 items lista desordenada: ", endTime - startTime)
print("****************************************")
startTime = timeit.default_timer()
quickSort(orderList(createList(1000)))
endTime = timeit.default_timer()
print("Tiempo de ejecucion 1000 items lista ordenada: ", endTime - startTime)
print("****************************************") """