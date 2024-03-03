from util import get_data

data = get_data(__file__)

n, m = map(int, data.split())

def mortal_fib(n, m):
    # n = number of months
    # m = number of months the rabbits live
    ages = [0] * m
    ages[-1] = 1

    for i in range(n):
        ages = [sum(ages[1:])] + ages[:-1]

    return sum(ages)

print(mortal_fib(n, m))