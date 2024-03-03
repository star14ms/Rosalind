from util import get_data

data = get_data(__file__)

seq, indexs = data.split('\n')
a, b, c, d = map(int, indexs.split(' '))

print(seq[a:b+1], seq[c:d+1])
