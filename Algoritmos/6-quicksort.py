import time
import random
import sys
from memory_profiler import memory_usage

# Aumentar o limite de recursão
sys.setrecursionlimit(10**7)

def partition(array, low, high):
    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            array[i], array[j] = array[j], array[i]

    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1

def quicksort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quicksort(array, low, pi - 1)
        quicksort(array, pi + 1, high)

if __name__ == '__main__':
    total_time = 0.0
    total_memory = 0.0
    num_executions = 1

    for _ in range(num_executions):
        arr = [random.randint(1, 1000000) for _ in range(1000000)]  # Array de 100.000 números inteiros aleatórios

        # Medir o tempo
        start_time = time.time()
        quicksort(arr.copy(), 0, len(arr) - 1)  # Usar uma cópia para evitar alterações no array original
        end_time = time.time()
        execution_time = end_time - start_time
        total_time += execution_time

        # Medir o consumo de memória
        memory_usage_result = memory_usage((quicksort, (arr.copy(), 0, len(arr) - 1)))  # Usar uma cópia para evitar alterações no array original
        max_memory = max(memory_usage_result)
        total_memory += max_memory

        print(f"Execução {_ + 1}: Tempo de execução: {execution_time:.6f} segundos, Consumo de memória: {max_memory:.2f} MB")

    average_time = total_time / num_executions
    average_memory = total_memory / num_executions
    print(f"Tempo médio de execução das {num_executions} execuções: {average_time:.6f} segundos")
    print(f"Consumo médio de memória das {num_executions} execuções: {average_memory:.2f} MB")
