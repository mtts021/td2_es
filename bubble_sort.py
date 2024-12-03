def bubble_sort(arr):
    """
    Implementa o algoritmo de ordenação Bubble Sort.

    Args:
        arr: A lista a ser ordenada.

    Returns:
        None. A lista original é modificada in-place.
    """

    n = len(arr)
    comparisons = 0

    # Percorre a lista inteira n-1 vezes
    # A cada iteração, o maior elemento "afunda" para sua posição correta
    for i in range(n):
        # Last i elements are already in place
        # Os últimos i elementos já estão em suas posições corretas
        swapped = False
        for j in range(0, n-i-1):
            comparisons += 1
        # Compara elementos adjacentes e troca se estiverem na ordem errada
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return comparisons

# Lendo os dados do arquivo JSON
import json

with open('temperaturas.json', 'r') as f:
  data = json.load(f)

# Ordenando os dados
comparisons = bubble_sort(data['ordered'])
print("Comparações para dados ordenados:", comparisons) # Comparações para dados ordenados: 49

comparisons = bubble_sort(data['reversed'])
print("Comparações para dados inversamente ordenados:", comparisons) # Comparações para dados inversamente ordenados: 1225

comparisons = bubble_sort(data['random'])
print("Comparações para dados aleatórios:", comparisons) # Comparações para dados aleatórios: 1219