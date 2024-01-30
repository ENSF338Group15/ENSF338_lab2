# 1. The code calculates the fibononocci number in the nth position
# 2. This is a divide-and-conquer alogorithm as it splits the problem by
#    recursively calling func until n is 0 or 1 and merges each subproblem
# 3. Time Complexity: O(2^n)
# 5. Time complexity when optimized: O(n)


def func(n):
    if n == 0 or n == 1:
        return n
    else:
        return func(n-1) + func(n-2)

#4
def func_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n == 0 or n == 1:
        return n
    else:
         memo[n] = func_memo(n-1, memo) + func_memo(n-2, memo)
         return memo[n]
    
n = int(input())
print(func_memo(n))
