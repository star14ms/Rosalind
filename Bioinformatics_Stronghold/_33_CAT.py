def count_matchings(rna):
    # Create a cache for memoization
    memo = {}

    # Define a helper function to check valid pairings
    def can_pair(x, y):
        return (x == 'A' and y == 'U') or (x == 'U' and y == 'A') or \
               (x == 'C' and y == 'G') or (x == 'G' and y == 'C')

    # Define the recursive function
    def dp(i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        if i >= j:  # No space for any pairs
            return 1
        res = 0
        for k in range(i+1, j+1, 2):  # Only pair with nucleotides at even distances
            if can_pair(rna[i], rna[k]):
                res += dp(i+1, k-1) * dp(k+1, j)  # Match and multiply the possibilities
        memo[(i, j)] = res % 1_000_000
        return memo[(i, j)]

    # Start the recursion from the full length of the RNA sequence
    return dp(0, len(rna) - 1)


from util import get_data

data = get_data(__file__)
# data ='''>Rosalind_57
# AUAU'''
# data = '''
# CGGCUGCUACGCGUAAGCCGGCUGCUACGCGUAAGC'''
rna_string = data.split('\n', 1)[1].replace('\n', '')

print(count_matchings(rna_string))


c = {'':1, 'A':0, 'C':0, 'G':0, 'U':0, 'AA':0, 'AC':0, 'AG':0, 'AU':1, 'CA':0, 'CC':0, 
    'CG':1, 'CU':0, 'GA':0, 'GC':1, 'GG':0, 'GU':0, 'UA':1, 'UC':0, 'UG':0, 'UU':0}

def catalan(s):
    if s not in c:
        c[s] = sum([catalan(s[1:k]) * c[s[0]+s[k]] * catalan(s[k+1:]) for k in range(1, len(s), 2)])
    return c[s]

print(catalan(rna_string) % 10**6)