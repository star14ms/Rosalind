### hard
import numpy as np
from scipy.cluster.hierarchy import average, to_tree
from scipy.spatial.distance import pdist, squareform
from util import get_data, get_output_path

from _56_CTBL import solve_newick_problem


data = get_data(__file__)

# data = '''cat dog elephant mouse rabbit rat
# 011101
# 001101
# 001100'''

# data = '''
# A B C D E
# 00000
# 00110
# 01000
# 01110
# 01111'''

labels = data.strip().split('\n')[0].split()
data = [list(row) for row in data.strip().split('\n')[1:]]
data = np.array(data, dtype=int)

# Calculate the pairwise distance matrix
dist_matrix = pdist(data.T, metric='hamming')
dist_square_matrix = squareform(dist_matrix)


# Perform UPGMA clustering
Z = average(dist_square_matrix)

# Convert clustering result to Newick format
def to_newick(node, parent_dist, leaf_names):
    if node.is_leaf():
        return "%s" % leaf_names[node.id]
    else:
        left = to_newick(node.get_left(), node.dist, leaf_names)
        right = to_newick(node.get_right(), node.dist, leaf_names)
        return "(%s,%s)" % (left, right)

# Build the tree
tree = to_tree(Z, rd=False)
newick_tree = to_newick(tree, tree.dist, labels) + ';'

print(newick_tree)

with open(get_output_path(__file__), 'w') as f:
  f.write(newick_tree + '\n')

solve_newick_problem(newick_tree)
