### ChatGPT (https://chatgpt.com/share/26ebbd20-0d6e-44e9-b754-aaafd24b350e)
from scipy.stats import binom
from util import get_data


# data = get_data(__file__)
data = '''4 6 2 1'''

# in a population of N diploid individuals initially possessing m copies of a dominant allele, 
# we will observe after g generations at least k copies of a recessive allele.
N, initial_dominant, generations, k = map(int, data.split())
total_alleles = 2 * N
initial_recessive = total_alleles - initial_dominant

# Calculate the probability of at least k recessive alleles after g generations
# Start with the initial probability of a recessive allele
p_recessive = initial_recessive / total_alleles

# We need to calculate the probability of having at least 1 recessive allele across generations
# For generation 1, we calculate this directly
# For generation 2, we need to use the results from generation 1
# Initialize the distribution of probabilities for recessive alleles
probabilities = [binom.pmf(x, total_alleles, p_recessive) for x in range(total_alleles + 1)]

print(probabilities)
print(sum(probabilities))

# Iterate through each generation after the first
for _ in range(1, generations):
    new_probabilities = [0] * (total_alleles + 1)
    for recessive_count in range(total_alleles + 1):
        current_prob = probabilities[recessive_count]
        # Update probabilities based on the current state
        for new_count in range(total_alleles + 1):
            new_probabilities[new_count] += current_prob * binom.pmf(new_count, total_alleles, recessive_count / total_alleles)
    probabilities = new_probabilities

# Calculate the probability of having at least k recessive alleles
probability_at_least_k = sum(probabilities[k:])

print(round(probability_at_least_k, 3))
