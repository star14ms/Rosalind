from util import get_data

data = get_data(__file__)

a, b = data.split(' ')

sum = 0
for i in range(int(a), int(b)+1):
    if i % 2 == 1:
        sum += i

print(sum)