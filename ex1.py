# 1. The code calculates the Fibonacci number in the nth position
# 2. This is a divide-and-conquer algorithm as it splits the problem by
# #  recursively calling func until n is 0 or 1 and merges each subproblem
# 3. Time Complexity: O(2^n)
# 5. Time Complexity when optimized: O(n)

import timeit
import matplotlib.pyplot as plt


def func(n):
    if n == 0 or n == 1:
        return n
    else:
        return func(n - 1) + func(n - 2)


# 4.
def func_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n == 0 or n == 1:
        return n
    else:
        memo[n] = func_memo(n - 1, memo) + func_memo(n - 2, memo)
        return memo[n]

# n = int(input())
# print(func_memo(n))

# 6.
exec_time = []
for n in range(36):
    original_time = timeit.timeit(f'func({n})', number=1, globals=globals())
    improved_time = timeit.timeit(f'func_memo({n})', number=1, globals=globals())
    exec_time.append([original_time, improved_time])
    # print(f'Original time: {original_time}; Improved time: {improved_time}')
plt.plot(range(36), [i[0] for i in exec_time], label='Original')
plt.plot(range(36), [i[1] for i in exec_time], label='Improved')
plt.xlabel('n')
plt.ylabel('Execution time')
plt.legend()
plt.show()
