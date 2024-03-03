from util import get_data

data = get_data('data/rosalind_iprb.txt')

k, m, n = map(int, data.split())

total = k + m + n
p = k / total # homozygous dominant XX
q = m / total # heterozygous XX'
r = n / total # homozygous recessive X'X'

# probability of dominant offspring
prob = 1 - r*((n-1) / (total-1)) - r*(m / (total-1))*0.5*2 - q*((m-1) / (total-1))*0.25
print(prob)