"""
Ejercicio de ordenamiento por mezcla utilizando colas: Escribe una función que implemente el algoritmo de ordenamiento 
por mezcla utilizando dos colas. La función debe tomar una lista de números desordenados, y dividirla en dos sub-listas 
de tamaño aproximadamente igual. Luego, debe ordenar cada sub-lista utilizando la misma función recursivamente, 
y finalmente mezclar las dos colas resultantes en una sola cola ordenada.

"""


from typing import List
from queue import Queue

def merge_sort_queue(numbers: List[int]) -> Queue:
    if len(numbers) <= 1:
        return Queue(numbers)
    else:
        mid = len(numbers) // 2
        left_queue = merge_sort_queue(numbers[:mid])
        right_queue = merge_sort_queue(numbers[mid:])
        return merge_queue(left_queue, right_queue)

def merge_queue(queue1: Queue, queue2: Queue) -> Queue:
    merged_queue = Queue()
    while not queue1.empty() and not queue2.empty():
        if queue1.queue[0] < queue2.queue[0]:
            merged_queue.put(queue1.get())
        else:
            merged_queue.put(queue2.get())
    while not queue1.empty():
        merged_queue.put(queue1.get())
    while not queue2.empty():
        merged_queue.put(queue2.get())
    return merged_queue

numbers = [4, 3, 2, 1, 5, 6, 8, 7]
sorted_queue = merge_sort_queue(numbers)
sorted_numbers = []
while not sorted_queue.empty():
    sorted_numbers.append(sorted_queue.get())
print(sorted_numbers)  # Output: [1, 2, 3, 4, 5, 6, 7, 8]

