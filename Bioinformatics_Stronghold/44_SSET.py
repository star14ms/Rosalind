from util import get_data, factorial, factorial_div

data = get_data(__file__)
# data = '3'
n = int(data)

# ø 1 2 3 4 ...
n_total_subsets = 1
for i in range(1, n+1):
  n_total_subsets += factorial_div(n, n-i) // factorial(i)

print(n_total_subsets % 1_000_000)
print((2 ** n) % 1_000_000)