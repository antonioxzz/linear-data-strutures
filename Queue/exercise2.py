"""
Ejercicio de ordenamiento por mezcla utilizando colas: Escribe una función que implemente el algoritmo de ordenamiento 
por mezcla utilizando dos colas. La función debe tomar una lista de números desordenados, y dividirla en dos sub-listas 
de tamaño aproximadamente igual. Luego, debe ordenar cada sub-lista utilizando la misma función recursivamente, 
y finalmente mezclar las dos colas resultantes en una sola cola ordenada.

"""


from typing import List

def merge_sort(numbers: List[int]) -> List[int]:
    if len(numbers) <= 1:
        return numbers
    else:
        mid = len(numbers) // 2
        left = merge_sort(numbers[:mid])
        right = merge_sort(numbers[mid:])
        return merge(left, right)

def merge(left: List[int], right: List[int]) -> List[int]:
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

numbers = [4, 3, 2, 1, 5, 6, 8, 7]
sorted_numbers = merge_sort(numbers)
print(sorted_numbers)  # Output: [1, 2, 3, 4, 5, 6, 7, 8]


