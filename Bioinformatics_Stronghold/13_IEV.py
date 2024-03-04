from util import get_data

data = get_data(__file__)

a, b, c, d, e, f = map(int, data.split(' '))
# n: number of couples
# a: AA-AA
# b: AA-Aa
# c: AA-aa
# d: Aa-Aa
# e: Aa-aa
# f: aa-aa

a = a
b = b
c = c
d = d * 0.75
e = e * 0.5
f = f * 0

print(2*(a + b + c + d + e + f))
