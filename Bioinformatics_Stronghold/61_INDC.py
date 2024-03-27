from util import get_data, get_output_path
from math import comb, log10
from decimal import Decimal, ROUND_HALF_UP

data = get_data(__file__)
# data = '''5'''
number = int(data)


def calculate_log_probabilities(n):
    probabilities = []
    for k in range(2*n + 1):
        # Calculate the probability of sharing at least k chromosomes
        probability_sum = sum(comb(2*n, i) * (0.5 ** (2*n)) for i in range(k, 2*n + 1))
        # Take the common logarithm of the probability sum
        log_probability = log10(probability_sum)
        log_probability = Decimal(log_probability).quantize(Decimal('0.000'), rounding=ROUND_HALF_UP)
        probabilities.append(log_probability)
    return probabilities[1:]


# Calculate and print the probabilities
probabilities = calculate_log_probabilities(number)
print(len(probabilities))

for i in range(len(probabilities)):
    print('%.3f' % probabilities[i], end=' ')

with open(get_output_path(__file__), 'w') as f:
    f.write(' '.join(map(str, probabilities)))
