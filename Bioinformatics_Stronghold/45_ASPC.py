from util import get_data, factorial, factorial_div

data = get_data(__file__)
# data = '6 3'
n, m = list(map(int, data.split()))


n_total_subsets = 0
for k in range(m, n+1):
  n_total_subsets += factorial_div(n, n-k) // factorial(k)

print(n_total_subsets % 1_000_000)