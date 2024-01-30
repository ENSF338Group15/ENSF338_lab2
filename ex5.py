import random
import timeit

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def measure_performance(search_function, vector_size):
    # Generate a sorted vector
    sorted_vector = list(range(vector_size))

    total_time = 0
    for _ in range(1000):
        # Pick a random element in the vector
        target_element = random.choice(sorted_vector)

        # Measure the time it takes to find the element using timeit
        time_taken = timeit.timeit(lambda: search_function(sorted_vector, target_element), number=100)
        total_time += time_taken

    # Compute the average time
    average_time = total_time / 1000
    return average_time

# Vector sizes
vector_sizes = [1000, 2000, 4000, 8000, 16000, 32000]

# Measure performance for linear search
print("Linear Search:")
for size in vector_sizes:
    average_time = measure_performance(linear_search, size)
    print(f"Vector Size: {size}, Average Time: {average_time:.6f} seconds")

# Measure performance for binary search
print("\nBinary Search:")
for size in vector_sizes:
    average_time = measure_performance(binary_search, size)
    print(f"Vector Size: {size}, Average Time: {average_time:.6f} seconds")
