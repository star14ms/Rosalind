### hard
from util import get_data, get_output_path
from itertools import combinations


data = get_data(__file__)
# data = 'A B C D E F G'
# data = 'dog cat mouse elephant'

leaves = data.split()


def generate_partitions(leaves):
    partitions = []
    n = len(leaves)
    for i in range(1, n//2 + 1):
        for left in combinations(leaves, i):
            right = tuple(t for t in leaves if t not in left)
            if (right, left) not in partitions:
                partitions.append((left, right))
    return partitions

# devide into two groups and list all possible combinations
def build_all_possible_binary_trees(leaves: list):
    if len(leaves) == 1:
        return [f'{leaves[0]}']
    elif len(leaves) == 2:
        return [f'({leaves[0]},{leaves[1]})']
    
    trees = []
    partitions = generate_partitions(leaves)
    for left, right in partitions:
        left_trees = build_all_possible_binary_trees(left)
        right_trees = build_all_possible_binary_trees(right)
        
        for left_tree in left_trees:
            for right_tree in right_trees:
                trees.append(f'({left_tree},{right_tree})')
        
    return trees


outer_tree = leaves.pop(0) + ');'
inner_trees = build_all_possible_binary_trees(leaves)
trees = [f'({inner_tree},{outer_tree}' for inner_tree in inner_trees]
print(*trees, sep='\n')
print(len(trees))

with open(get_output_path(__file__), 'w') as output_data:
  output_data.write('\n'.join(trees) + '\n')
