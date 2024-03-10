from util import get_data

data = get_data(__file__)

_, numbers, top_n = data.split('\n')
numbers = list(map(int, numbers.split()))

sorted_numbers = sorted(numbers)
print(' '.join(map(str, sorted_numbers[:int(top_n)])))

with open('Algorithmic_Heights/output/25_PS.txt', 'w') as output_data:
    output_data.write(' '.join(map(str, sorted_numbers[:int(top_n)])) + '\n')