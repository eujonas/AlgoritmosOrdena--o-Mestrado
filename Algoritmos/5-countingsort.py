import time
import random
from memory_profiler import memory_usage

def countingSort(arr):
    # Encontre o valor máximo no array para determinar o tamanho da matriz de contagem
    max_val = max(arr)
    count = [0] * (max_val + 1)
    output = [0] * len(arr)

    for num in arr:
        count[num] += 1

    i = 0
    for num in range(max_val + 1):
        while count[num] > 0:
            output[i] = num
            i += 1
            count[num] -= 1

    return output

if __name__ == '__main__':
    total_time = 0.0
    total_memory = 0.0
    num_executions = 5

    for _ in range(num_executions):
        arr = [random.randint(1, 10000000) for _ in range(10000000)]  # Array de 10.000 números inteiros aleatórios

        # Medir o tempo
        start_time = time.time()
        result = countingSort(arr.copy())  # Usar uma cópia para evitar alterações no array original
        end_time = time.time()
        execution_time = end_time - start_time
        total_time += execution_time

        # Medir o consumo de memória
        memory_usage_result = memory_usage((countingSort, (arr.copy(),)))  # Usar uma cópia para evitar alterações no array original
        max_memory = max(memory_usage_result)
        total_memory += max_memory

        print(f"Execução {_ + 1}: Tempo de execução: {execution_time:.6f} segundos, Consumo de memória: {max_memory:.2f} MB")

    average_time = total_time / num_executions
    average_memory = total_memory / num_executions
    print(f"Tempo médio de execução das {num_executions} execuções: {average_time:.6f} segundos")
    print(f"Consumo médio de memória das {num_executions} execuções: {average_memory:.2f} MB")
