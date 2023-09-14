import time
import random
import sys
from memory_profiler import memory_usage

def heapify(arr, N, i):
    largest = i  # Inicializa o maior como raiz
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2

    if l < N and arr[largest] < arr[l]:
        largest = l

    if r < N and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Troca
        heapify(arr, N, largest)

def heapSort(arr):
    N = len(arr)

    for i in range(N // 2 - 1, -1, -1):
        heapify(arr, N, i)

    for i in range(N - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Troca
        heapify(arr, i, 0)

if __name__ == '__main__':
    total_time = 0.0
    total_memory = 0.0
    num_executions = 5

    for _ in range(num_executions):
        arr = [random.randint(1, 1000000) for _ in range(1000000)]  # Array de 100.000 números inteiros aleatórios

        # Medir o tempo
        start_time = time.time()
        heapSort(arr.copy())  
        end_time = time.time()
        execution_time = end_time - start_time
        total_time += execution_time

        # Medir o consumo de memória
        memory_usage_result = memory_usage((heapSort, (arr.copy(),)))  # Usar uma cópia para evitar alterações no array original
        max_memory = max(memory_usage_result)
        total_memory += max_memory

        print(f"Execução {_ + 1}: Tempo de execução: {execution_time:.6f} segundos, Consumo de memória: {max_memory:.2f} MB")

    average_time = total_time / num_executions
    average_memory = total_memory / num_executions
    print(f"Tempo médio de execução das {num_executions} execuções: {average_time:.6f} segundos")
    print(f"Consumo médio de memória das {num_executions} execuções: {average_memory:.2f} MB")
