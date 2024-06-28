from util import get_data, get_output_path
from math import comb, log10


data = get_data(__file__)
# data = '''4 3
# 0 1 2'''

data = data.split('\n')
N, m = list(map(int, data[0].split()))

n_recessive_list = list(map(int, data[1].split()))
total_alle = 2 * N

probability_matrix = [[0] * m for _ in range(m)]
# print(probability_matrix)
# print(n_recessive_list)

for i, n_recessive in enumerate(n_recessive_list):
    probabilities = [
      comb(total_alle, current_count) * \
        (n_recessive/total_alle)**current_count * ((total_alle-n_recessive)/total_alle)**(total_alle-current_count) \
          for current_count in range(total_alle + 1)
    ]

    probability_matrix[0][i] = log10(probabilities[0]) # no copies of the recessive allele

    for j in range(1, m):
        new_probabilities = [0] * (total_alle + 1)
        for recessive_count in range(total_alle + 1):
            current_prob = probabilities[recessive_count]
            for new_count in range(total_alle + 1):
                new_probabilities[new_count] += current_prob * comb(total_alle, new_count) * \
                  (recessive_count/total_alle)**new_count * ((total_alle-recessive_count)/total_alle)**(total_alle-new_count)

        probabilities = new_probabilities
        probability_matrix[j][i] = log10(probabilities[0])


with open(get_output_path(__file__), 'w') as outFile:
    for row in probability_matrix:
        print(' '.join(map(str, row)))
        print(' '.join(map(str, row)), file=outFile)
