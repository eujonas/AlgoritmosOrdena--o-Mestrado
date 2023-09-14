import time
import random
from memory_profiler import memory_usage

def shellSort(arr, n):
    gap = n // 2

    while gap > 0:
        j = gap
        while j < n:
            i = j - gap

            while i >= 0:
                if arr[i + gap] > arr[i]:
                    break
                else:
                    arr[i + gap], arr[i] = arr[i], arr[i + gap]

                i = i - gap
            j += 1
        gap = gap // 2

if __name__ == '__main__':
    total_time = 0.0
    total_memory = 0.0
    num_executions = 1

    for _ in range(num_executions):
        arr = [random.randint(1, 1000000) for _ in range(1000000)]  # Array de 100.000 números inteiros aleatórios

        # Medir o tempo
        start_time = time.time()
        shellSort(arr.copy(), len(arr))  # Usar uma cópia para evitar alterações no array original
        end_time = time.time()
        execution_time = end_time - start_time
        total_time += execution_time

        # Medir o consumo de memória
        memory_usage_result = memory_usage((shellSort, (arr.copy(), len(arr))))  # Usar uma cópia para evitar alterações no array original
        max_memory = max(memory_usage_result)
        total_memory += max_memory

        print(f"Execução {_ + 1}: Tempo de execução: {execution_time:.6f} segundos, Consumo de memória: {max_memory:.2f} MB")

    average_time = total_time / num_executions
    average_memory = total_memory / num_executions
    print(f"Tempo médio de execução das {num_executions} execuções: {average_time:.6f} segundos")
    print(f"Consumo médio de memória das {num_executions} execuções: {average_memory:.2f} MB")
