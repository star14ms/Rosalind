### hard
from util import get_data, get_output_path

SUFF = __import__('75_SUFF')
get_suffix_tree = SUFF.get_suffix_tree


if __name__ == '__main__':
    dna = get_data(__file__)
    # dna = 'TAGTTAGCGAGA'
    # dna = '''TAGAGATAGAATGGGTCCAGAGTTTTGTAATTTCCATGGGTCCAGAGTTTTGTAATTTATTATATAGAGATAGAATGGGTCCAGAGTTTTGTAATTTCCATGGGTCCAGAGTTTTGTAATTTAT'''

    suffix_tree = get_suffix_tree(dna + '$')

    def get_maximum_repeats(suffix_tree, prefix=''):
        maximum_repeats_all = []
        n_substring = 0
        for char in suffix_tree.copy():
            child_suffix_tree = suffix_tree[char]
            new_prefix = prefix + char

            while len(child_suffix_tree) == 1:
                char = list(child_suffix_tree.keys())[0]
                new_prefix += char
                child_suffix_tree = child_suffix_tree[char]
                
            if len(child_suffix_tree) > 1:
                maximum_repeats, n_substring_new = get_maximum_repeats(child_suffix_tree, new_prefix)
                n_substring += n_substring_new
                maximum_repeats_all.extend(maximum_repeats)
            elif len(child_suffix_tree) == 0:
                n_substring += 1

        if len(suffix_tree) > 1 and len(prefix) >= 20: # prefix becomes maximum repeat if no more branches
            maximum_repeats_all.append((prefix, n_substring))

        return maximum_repeats_all, n_substring

    maximum_repeats, n_substring = get_maximum_repeats(suffix_tree)
    
    for i in range(len(maximum_repeats)-1, -1, -1):
        for j in range(len(maximum_repeats)-1, -1, -1):
            if i != j and \
                maximum_repeats[i][0] in maximum_repeats[j][0] and \
                maximum_repeats[i][1] == maximum_repeats[j][1]:
                maximum_repeats.remove(maximum_repeats[i])
                break
    
    with open(get_output_path(__file__), 'w') as f:
        for maximum_repeat in maximum_repeats:
            print(maximum_repeat[0])
            f.write(maximum_repeat[0] + '\n')
