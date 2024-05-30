##################################################
# Fixing an Inconsistent Character Set
#
# http://rosalind.info/problems/CSET/
# 
# Given: An inconsistent character table C on at
#  most 100 taxa.
# 
# Return: A submatrix of C' representing a consistent
#  character table on the same taxa and formed by
#  deleting a single row of C. (If multiple solutions
#  exist, you may return any one.)
#
# AUTHOR : dohlee
##################################################

# Your imports here
from collections import Counter
from util import get_data, get_output_path

# Your codes here
def has_conflict(c1, c2):
    """Return True if two rows of character table conflict."""
    hasConflict = True
    s1 = set(i for i, c in enumerate(c1) if c == '1')
    s1c = set(i for i, c in enumerate(c1) if c == '0')
    s2 = set(i for i, c in enumerate(c2) if c == '1')
    s2c = set(i for i, c in enumerate(c2) if c == '0')

    for a in [s1, s1c]:
        for b in [s2, s2c]:
            if len(a.intersection(b)) == 0:
                hasConflict = False

    return hasConflict

if __name__ == '__main__':
    # Load the data.
    # data = get_data(__file__)
    data = '''100001
000110
111000
100111'''
    characterTable = [[char for char in row] for row in data.strip().split('\n')]
    print(characterTable)
    conflictCount = Counter()
    for i in range(len(characterTable)):
        for j in range(i+1, len(characterTable)):
            if has_conflict(characterTable[i], characterTable[j]):
                conflictCount[i] += 1
                conflictCount[j] += 1

    # Print output
    with open(get_output_path(__file__), 'w') as outFile:
        skipIndex = max(conflictCount, key=lambda x: conflictCount[x])
        print('\n'.join(map(lambda row: ''.join(row), [row for i, row in enumerate(characterTable) if i != skipIndex])), file=outFile)
