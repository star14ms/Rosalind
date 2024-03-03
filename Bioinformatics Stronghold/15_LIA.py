from util import get_data

data = get_data(__file__)

# K: number of generations, N: number of AaBb organisms at the K-th generation
# at least N AaBb organisms in the K-th generation
k, n = map(int, data.split(' ')) 

# 1/4: AaBb, 3/4: not AaBb
def prob(k, n):
    prob = 1
    for i in range(n):
        # probability of i number of organisms is not AaBb
        prob -= choose(2**k, i) * ((1/4)**i * (3/4)**(2**k - i))
    return prob

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

def choose(n, k):
    return factorial(n) / (factorial(k) * factorial(n - k))

print(prob(k, n))

# 0th generation
# AaBb-AaBb

# 1st generation
# AABB: 1/4 AaBB: 1/4 AABb: 1/4 AaBb: 1/4
# AaBB: 1/4 aaBB: 1/4 AaBb: 1/4 aaBb: 1/4
# AABb: 1/4 AaBb: 1/4 AAbb: 1/4 Aabb: 1/4
# AaBb: 1/4 aaBb: 1/4 Aabb: 1/4 aabb: 1/4
