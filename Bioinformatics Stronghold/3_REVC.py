from util import get_data

data = get_data('data/rosalind_revc.txt')

new_data = ''
for char in data[::-1]:
    if char == 'A':
        new_data += 'T'
    elif char == 'T':
        new_data += 'A'
    elif char == 'C':
        new_data += 'G'
    elif char == 'G':
        new_data += 'C'

print(new_data)