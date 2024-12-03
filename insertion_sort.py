def insertion_sort(arr):
    """
    Implementa o algoritmo de ordenação Insertion Sort.

    Args:
        arr: A lista a ser ordenada.

    Returns:
        None. A lista original é modificada in-place.
    """
    comparisons = 0

    for i in range(1, len(arr)):
        # Valor a ser inserido na posição correta
        key = arr[i]

        # Move os elementos maiores que o key para uma posição à frente
        j = i - 1
        comparisons += 1
        while j >= 0 and arr[j] > key:
            comparisons += 1
            arr[j + 1] = arr[j]
            j -= 1

        # Insere o elemento key na posição correta
        arr[j + 1] = key
    return comparisons

# Lendo os dados do arquivo JSON
import json

with open('temperaturas.json', 'r') as f:
  data = json.load(f)

# Ordenando os dados
comparisons = insertion_sort(data['ordered'])
print("Comparações para dados ordenados:", comparisons) # Comparações para dados ordenados: 49

comparisons = insertion_sort(data['reversed'])
print("Comparações para dados inversamente ordenados:", comparisons) # Comparações para dados inversamente ordenados: 1218

comparisons = insertion_sort(data['random'])
print("Comparações para dados aleatórios:", comparisons) # Comparações para dados aleatórios: 643
