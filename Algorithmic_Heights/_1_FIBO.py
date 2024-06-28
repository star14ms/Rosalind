from util import get_data

data = get_data(__file__)

n = int(data)

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
      
print(fib(n))