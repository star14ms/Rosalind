from util import get_data
from math import comb
from scipy.stats import binom


if __name__ == '__main__':
    # data = get_data(__file__)
    data = '''4 6 2 1'''
    
    # in a population of N diploid individuals initially possessing m copies of a dominant allele, 
    # we will observe after g generations at least k copies of a recessive allele.
    N, m, g, k = map(int, data.split())

    p_dominant = m / (2*N)
    p_recessive = 1 - p_dominant

    # The probability that an individual has at least one recessive allele next generation
    # 1 - probability that an individual has no recessive allele next generation
    # if k == 1:
    #     print(1 - prob_dominant**N)

    prob_at_least_k_recessive = 0

    probabilities = [0] * (2*N + 1)
    for n_recessive in range(2*N + 1):
        probabilities[n_recessive] = comb(2*N, n_recessive) * (p_recessive**n_recessive * p_dominant**(2*N-n_recessive))
    # probabilities = [binom.pmf(x, 2*N, p_recessive) for x in range(2*N + 1)]

    for _ in range(1, g):
        new_probabilities = [0] * (2*N + 1)
        
        for n_recessive in range(2*N + 1):
            prob_current = probabilities[n_recessive]

            p_recessive_new = n_recessive / (2*N)
            p_dominant_new = 1 - p_recessive_new

            for n_recessive_new in range(2*N + 1):
                new_probabilities[n_recessive_new] += prob_current * \
                    comb(2*N, n_recessive_new) * (p_recessive_new**n_recessive_new * p_dominant_new**(2*N-n_recessive_new))
                    # binom.pmf(n_recessive_new, 2*N, p_recessive_new)

        probabilities = new_probabilities

    print(sum(probabilities[k:]))
    

        
        
        
    
    
    
    

