from util import get_data

data = get_data(__file__)

symbols, length = data.split('\n')
symbols = symbols.split()

def get_permutations(symbols, length):
    if length == 1:
        return symbols
    else:
        return [i + j for i in symbols for j in get_permutations(symbols, length-1)]

perms = get_permutations(symbols, int(length))

with open('output/23_LEXF.txt', 'w') as f:
    f.write('\n'.join(perms))