import random
import time

comp = 0
def insertionSort(arr):
    comp = 0
    for i in range(1, len(arr)):
        j = i-1
        comp += 1
        while j >= 0 and arr[i] < arr[j]:
            comp += 1
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = arr[i]

    return comp

n = 10

arr_random = [random.randint(1, 100) for _ in range(n**4)]
arr_sorted = sorted(arr_random)
arr_reversed = arr_sorted[::-1]

start_t = time.perf_counter()
comp = insertionSort(arr_reversed)
end_t = time.perf_counter()

elapsed_t = (end_t - start_t)*(10**6)
print(f'Time: {elapsed_t} microsecond')
print("Comparison: ", comp)

