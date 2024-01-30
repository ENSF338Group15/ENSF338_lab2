import timeit
import random
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

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
    vector = sorted(random.sample(range(1, vector_size + 1), vector_size))
    target = random.choice(vector)

    # Measure the time it takes to find the element using timeit
    time_taken = timeit.timeit(lambda: search_function(vector, target), number=100)

    return time_taken / 100  # Compute the average time taken per iteration

def fit_function_linear(x, a, b):
    return a * x + b

def fit_function_logarithmic(x, a, b):
    return a * np.log(x) + b

vector_sizes = [1000, 2000, 4000, 8000, 16000, 32000]

linear_search_times = []
binary_search_times = []

for size in vector_sizes:
    linear_avg_time = measure_performance(linear_search, size)
    binary_avg_time = measure_performance(binary_search, size)

    linear_search_times.append(linear_avg_time)
    binary_search_times.append(binary_avg_time)

# Fitting the data with linear and logarithmic functions
linear_fit_params, _ = curve_fit(fit_function_linear, vector_sizes, linear_search_times)
binary_fit_params, _ = curve_fit(fit_function_logarithmic, vector_sizes, binary_search_times)

# Plotting the results
plt.plot(vector_sizes, linear_search_times, 'o', label='Linear Search')
plt.plot(vector_sizes, binary_search_times, 'o', label='Binary Search')

# Plotting the fitted functions
x_values = np.linspace(min(vector_sizes), max(vector_sizes), 100)
plt.plot(x_values, fit_function_linear(x_values, *linear_fit_params), label='Linear Fit')
plt.plot(x_values, fit_function_logarithmic(x_values, *binary_fit_params), label='Logarithmic Fit')

plt.xlabel('Vector Size')
plt.ylabel('Average Time (seconds)')
plt.title('Performance of Linear and Binary Search with Fits')
plt.legend()
plt.show()

'''
Answer to exercise 5, question 4:
the type of function is a linear interpolating function represented by a straight line with the equation 
y = ax + b, where a is the slope of the line and b is the y-intercept. The second type of function is a 
logarithmic function represented by the equation y = a * log(x) + b where a determines the function scaling
and b is the vertical shift. As the time complexity of the algorithm is indicated to be linear, and resebles
a straight line, as seen in our output, then the relationship is correctly determined to be linear. Binary
search commonly exhibits a logarithmic time complexity, the logarithmic fit indicates a decreasing rate
of time as input size decreases, therefore the correct relationship is determined to be logarithmic. Our results
allign exactly as expected.
'''
