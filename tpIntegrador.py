#Librerias
import random

#Crear lista
def createList(cant):
    lista = [random.randint(1, 1000) for _ in range(cant)]
    return lista

#Ordenar lista
def orderList (list):
    return sorted(list)

#Buscar item (busqueda lineal)
def searchLineal (list, item):
    for i in range(len(list)):
        if list[i] == item:
            return i
    return -1

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

#Ordenamiento por burbuja (Bubble Sort)
def bubleSort(list):
    for i in range(len(list)):
        for j in range(0, len(list) - i - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
    return list

#Ordenamiento por insercion
def insertionSort(list):
    for i in range(1, len(list)):
        key = list[i]
        j = i - 1
        while j >= 0 and key < list[j]:
            list[j+1] = list[j]
            j -= 1
        list[j+1] = key

#Ordenamiento de seleccion
def selectionSort(list):
    n = len(list)
    for i in range(n):
        minIndex = i
        for j in range(i+1, n):
            if list[j]< list[minIndex]:
                minIndex = j
        list[i], list[minIndex] = list[minIndex], list[i]

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

#Ordenamiento rapido
def quickSort(list):
    if len(list) <= 1:
        return list
    else:
        pivot = list[0]
        less = [x for x in list[1:] if x <= pivot]
        greater = [x for x in list[1:] if x > pivot]
        return quickSort(less) + [pivot] + quickSort(greater)
