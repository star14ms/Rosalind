def count_base_pairs(rna):
    # Count the occurrences of each base in the RNA string
    base_counts = {'A': rna.count('A'), 'U': rna.count('U'), 'C': rna.count('C'), 'G': rna.count('G')}
    
    # Calculate possible pairings for AU and CG
    au_pairs = min(base_counts['A'], base_counts['U'])
    cg_pairs = min(base_counts['C'], base_counts['G'])
    
    return base_counts['A'], base_counts['U'], base_counts['C'], base_counts['G'], au_pairs, cg_pairs

def factorial_div(n, k):
    """Calculate n! / k! which simplifies the calculation avoiding large numbers."""
    result = 1
    for i in range(k + 1, n + 1):
        result *= i
    return result

def max_matchings(a, u, c, g):
    # Calculate the matchings for AU and CG considering the maximum possible pairings
    au_matchings = factorial_div(max(a, u), abs(a-u))
    cg_matchings = factorial_div(max(c, g), abs(c-g))

    return au_matchings * cg_matchings

from util import get_data

data = get_data(__file__)
# data = '''>Rosalind_92
# AUGCUUC'''s
rna = data.split('\n', 1)[1].replace('\n', '')
a, u, c, g, au_pairs, cg_pairs = count_base_pairs(rna)

# Recalculating with the corrected approach
max_matchings_result = max_matchings(a, u, c, g)
print(max_matchings_result)
