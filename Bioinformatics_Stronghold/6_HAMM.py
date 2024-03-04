from util import get_data

data = get_data('data/rosalind_hamm.txt')

s, t = data.split('\n')
hamming_distance = 0

for i in range(len(s)):
    hamming_distance += s[i] != t[i]

print(hamming_distance)