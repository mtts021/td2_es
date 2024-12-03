def binary_search(the_array, item, start, end):
    if start == end:
        if the_array[start] > item:
            return start
        else:
            return start + 1
    if start > end:
        return start

    mid = round((start + end)/ 2)

    if the_array[mid] < item:
        return binary_search(the_array, item, mid + 1, end)

    elif the_array[mid] > item:
        return binary_search(the_array, item, start, mid - 1)

    else:
        return mid

"""
Insertion sort utilizada pelo timsort se o tamanho do array ou da "run" é pequeno.
"""
def insertion_sort(the_array):
    l = len(the_array)
    for index in range(1, l):
        value = the_array[index]
        pos = binary_search(the_array, value, 0, index - 1)
        the_array = the_array[:pos] + [value] + the_array[pos:index] + the_array[index+1:]
    return the_array

def merge(left, right):
    """Recebe duas listas ordenadas e retorna uma única lista ordenada comparando os elementos um de cada vez.
    [1, 2, 3, 4, 5, 6]
    """
    if not left:
        return right
    if not right:
        return left
    if left[0] < right[0]:
        return [left[0]] + merge(left[1:], right)
    return [right[0]] + merge(left, right[1:])

def timsort(the_array):
    runs, sorted_runs = [], []
    length = len(the_array)
    new_run = [the_array[0]]
    comparisons = 0

    # Para cada i no intervalo de 1 até o tamanho do array
    for i in range(1, length):
        comparisons += 1
        #se i está no final da lista
        if i == length - 1:
            new_run.append(the_array[i])
            runs.append(new_run)
            break
        # se o i-ésimo elemento do array for menor que o anterior
        if the_array[i] < the_array[i-1]:
            # se new_run estiver definido como None (nulo)
            if not new_run:
                runs.append([the_array[i]])
                new_run.append(the_array[i])
            else:
                runs.append(new_run)
                new_run = []
        # senão se for igual ou maior que
        else:
            new_run.append(the_array[i])

    # para cada item em runs, adicione o item usando insertion sort
    for item in runs:
        comparisons += 1
        sorted_runs.append(insertion_sort(item))
    
    # para cada run em sorted_runs, mescle-as
    sorted_array = []
    for run in sorted_runs:
        comparisons += 0
        sorted_array = merge(sorted_array, run)

    # print(sorted_array)
    return comparisons

import json

with open('temperaturas_200.json', 'r') as f:
  data = json.load(f)

# Ordenando os dados
comparisons = timsort(data['ordered'])
print("Comparações para dados ordenados:", comparisons) # Comparações para dados ordenados: 50

comparisons = timsort(data['reversed'])
print("Comparações para dados inversamente ordenados:", comparisons) # Comparações para dados inversamente ordenados: 68

comparisons = timsort(data['random'])
print("Comparações para dados aleatórios:", comparisons) # Comparações para dados aleatórios: 73
