
def recSelectionSort(lista, i, j):
    if i == j:
        return i
    

    k = recSelectionSort(lista, i + 1, j)


    if(lista[i]<lista[k]):
        return i
    else:
        return k 
    
def selectionSort(lista, n, index = 0):
    

    if index == n:
        return -1
    
    k = recSelectionSort(lista, index, n-1)

    if k != index:
        lista[k], lista[index] = lista[index], lista[k]

    selectionSort(lista, n, index + 1)

lista = [1,2,3,4,5,5,4,3,2,1]
listaN = len(lista)

selectionSort(lista, listaN)

print(lista)