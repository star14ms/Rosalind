from util import get_data, get_output_path

data = get_data(__file__)
data = '''ATAAATG$'''

s = data.strip()

def get_suffixes(s):
    """Return all suffixes of the given string."""
    return [s[i:] for i in range(len(s))]
  
def get_suffix_tree(s):
    """Return the suffix tree of the given string."""
    suffixes = get_suffixes(s)
    suffix_tree = {}
    for suffix in suffixes:
        current = suffix_tree
        for char in suffix:
            if char not in current:
                current[char] = {}
            current = current[char]
    return suffix_tree


def print_substrings_of_suffix_tree(suffix_tree, prefix=''):
    """Print all substrings of the given suffix tree."""
    for char in suffix_tree.copy():
        if len(suffix_tree[char]) != 1:
            with open(get_output_path(__file__), 'a') as f:
                f.write(prefix + char + '\n')
                print(prefix + char)
        print_substrings_of_suffix_tree(suffix_tree[char], prefix + char if len(suffix_tree[char]) == 1 else '') 


if __name__ == '__main__':
    suffix_tree = get_suffix_tree(s)

    with open(get_output_path(__file__), 'w') as f:
        pass

    print_substrings_of_suffix_tree(suffix_tree)
