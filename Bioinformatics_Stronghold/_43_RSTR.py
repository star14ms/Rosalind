from util import get_data

data = get_data(__file__)
# data = '''90000 0.6
# ATAGCCGA'''
data = data.split('\n')
n, gc_content = map(float, data[0].split())
seq = data[1]

g_or_c = gc_content/2
a_or_t = (1-gc_content)/2

prob = 1
for base in seq:
    if base == 'G' or base == 'C':
        prob *= g_or_c
    else:
        prob *= a_or_t

prob_c = 1 - prob
prob_c_n_times = prob_c ** n
prob_at_least_one_in_n_times = 1 - prob_c_n_times

print('%.3f' % prob_at_least_one_in_n_times)
