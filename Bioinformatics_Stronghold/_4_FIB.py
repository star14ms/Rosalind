from util import get_data

data = get_data(__file__)

n, k = map(int, data.split())

def rabbit_pairs(n, k):
    if n == 1 or n == 2:
        return 1
    return rabbit_pairs(n-1, k) + k * rabbit_pairs(n-2, k)

print(rabbit_pairs(n, k))
