from util import get_data

data = get_data('40_MMCH.py')
# data = '''>Rosalind_92
# AUGCUUC'''
rna_string = data.split('\n', 1)[1].replace('\n', '')


c = {'':0, 'A':0, 'C':0, 'G':0, 'U':0, 'AA':0, 'AC':0, 'AG':0, 'AU':1, 'CA':0, 'CC':0, 
    'CG':1, 'CU':0, 'GA':0, 'GC':1, 'GG':0, 'GU':0, 'UA':1, 'UC':0, 'UG':0, 'UU':0}

lengths_longest_pair = {'':0, 'A':0, 'C':0, 'G':0, 'U':0, 'AA':0, 'AC':0, 'AG':0, 'AU':1, 'CA':0, 'CC':0, 
    'CG':1, 'CU':0, 'GA':0, 'GC':1, 'GG':0, 'GU':0, 'UA':1, 'UC':0, 'UG':0, 'UU':0}

def catalan(s):
    if s not in c:
        pairing_lengths = []
        for i in range(0, len(s)-1):
            for k in range(i+1, len(s)):
                middle = c[s[i]+s[k]]
                if middle > 0:
                    left, length_longest = catalan(s[i+1:k] + s[k+1:])
                    pairing_lengths.append((max(left, 1), 1 + length_longest))
                    # print(s[i]+s[k], i, k, pairing_lengths)

        if len(pairing_lengths) == 0:
            c[s] = 0
            lengths_longest_pair[s] = 0
        else:
            length_longest_pair = max(pairing_lengths, key=lambda x: x[1])[1]
            n_possible_pairs = sum([n_pair for n_pair, length in pairing_lengths if length == length_longest_pair])
            c[s] = n_possible_pairs
            lengths_longest_pair[s] = length_longest_pair

    return c[s], lengths_longest_pair[s]

n_possible_pairs, lengths_longest_pair = catalan(rna_string)
print(n_possible_pairs % 10**6, lengths_longest_pair)


# def catalan(s):
#     if s not in c:
#         pairing_lengths = []
#         for i in range(0, len(s)-1):
#             for k in range(i+1, len(s)):
#                 middle = c[s[i]+s[k]]

#                 if middle > 0:
#                     left, longest_pair_l = catalan(s[:i])
#                     right, longest_pair_r = catalan(s[k+1:])
#                     pairing_lengths.append((max(left, 1) * middle * max(right, 1), longest_pair_l + 1 + longest_pair_r))

#         if len(pairing_lengths) == 0:
#             c[s] = 0
#             lengths_longest_pair[s] = 0
#         else:
#             length_longest_pair = max(pairing_lengths, key=lambda x: x[1])[1]
#             n_possible_pairs = sum([n_pair for n_pair, length in pairing_lengths if length == length_longest_pair])
#             c[s] = n_possible_pairs
#             lengths_longest_pair[s] = length_longest_pair

#     return c[s], lengths_longest_pair[s]

# n_possible_pairs, lengths_longest_pair = catalan(rna_string)
# print(n_possible_pairs % 10**6, lengths_longest_pair)



# print(c)

# def catalan(s):
#     func = lambda k: (catalan(s[1:k]), c[s[0]+s[k]], catalan(s[k+1:]))

#     if s not in c:
#         c[s] = sum([
#             max(l, 1) * max(m, 1) * max(r, 1) \
#                 for l, m, r in map(func, range(1, len(s), 1)) if l > 0 or m > 0 or r > 0
#         ])
#     return c[s]