import time
import random
from memory_profiler import memory_usage

def countingSort(arr, exp1):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(0, n):
        index = arr[i] // exp1
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = arr[i] // exp1
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    i = 0
    for i in range(0, len(arr)):
        arr[i] = output[i]

def radixSort(arr):
    max1 = max(arr)
    exp = 1
    while max1 // exp > 0:
        countingSort(arr, exp)
        exp *= 10

if __name__ == "__main__":
    total_time = 0.0
    total_memory = 0.0
    num_executions = 5

    for _ in range(num_executions):
        arr = [random.randint(1, 11000) for _ in range(11000)]  # Array de 10.000 elementos aleatórios

        # Medir o tempo
        start_time = time.time()
        radixSort(arr.copy())  # Usar uma cópia para evitar alterações no array original
        end_time = time.time()
        execution_time = end_time - start_time
        total_time += execution_time

        # Medir o consumo de memória
        memory_usage_result = memory_usage((radixSort, (arr.copy(),)))  # Usar uma cópia para evitar alterações no array original
        max_memory = max(memory_usage_result)
        total_memory += max_memory

        print(f"Execução {_ + 1}: Tempo de execução: {execution_time:.6f} segundos, Consumo de memória: {max_memory:.2f} MB")

    average_time = total_time / num_executions
    average_memory = total_memory / num_executions
    print(f"Tempo médio de execução das {num_executions} execuções: {average_time:.6f} segundos")
    print(f"Consumo médio de memória das {num_executions} execuções: {average_memory:.2f} MB")
