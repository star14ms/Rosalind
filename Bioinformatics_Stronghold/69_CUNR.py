from util import get_data, factorial, factorial_div

data = get_data(__file__)
# data = '''5'''
n = int(data)

# total number of distinct unrooted binary trees having n labeled leaves.
# def choose(n, k):
#     return factorial_div(n, k) / factorial(n - k)

# def count_unrooted_binary_trees(n):
#   result = 0
#   for i in range(1, n//2+1):
#     result += choose(n, i) % 1_000_000

#   return result

# distinct_unrooted_binary_trees = count_unrooted_binary_trees(n)
# print(distinct_unrooted_binary_trees % 1_000_000)


def count_unrooted_binary_trees(n):
  if n == 2:
    return 1
  return count_unrooted_binary_trees(n-1) * (2 * (n-1) - 3) % 1_000_000

print(count_unrooted_binary_trees(n))

# Example with 5 leaves
# 1. 1-2-3-4-5

# 1. 1-2-3-4  5
# 2. 1-2-3-5  4
# 3. 1-2-4-5  3
# 4. 1-3-4-5  2
# 5. 2-3-4-5  1

# 1. 1-2-3    4-5
# 2. 1-2-4    3-5
# 3. 1-2-5    3-4
# 4. 1-3-4    2-5
# 5. 1-3-5    2-4
# 6. 1-4-5    2-3
# 7. 1-2      3-4-5
# 8. 1-3      2-4-5
# 9. 1-4      2-3-5
# 10. 1-5      2-3-4
