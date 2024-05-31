# complement to _13_BA1M.py
from util import get_data
# from itertools import product


def pattern_to_number(pattern):
    # Too Slow
    # for i, pattern2 in enumerate(product("ACGT", repeat=len(pattern))):
    #     pattern2 = ''.join(pattern2)
    #     if pattern == pattern2:
    #         return i

    weights = ['ACGT'.index(nucleotide) for nucleotide in pattern]

    number = 0
    for i, order in enumerate(weights[::-1]):
        number += order * 4 ** i
        
    return number

if __name__ == "__main__":
    pattern = get_data(__file__)
    # pattern ='''AGT'''
    
    number = pattern_to_number(pattern)
    print(number)
