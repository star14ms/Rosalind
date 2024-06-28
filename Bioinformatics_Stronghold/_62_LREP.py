### hard
from util import get_data, get_output_path

data = get_data(__file__)
# data = '''CATACATAC$
# 2
# node1 node2 1 1
# node1 node7 2 1
# node1 node14 3 3
# node1 node17 10 1
# node2 node3 2 4
# node2 node6 10 1
# node3 node4 6 5
# node3 node5 10 1
# node7 node8 3 3
# node7 node11 5 1
# node8 node9 6 5
# node8 node10 10 1
# node11 node12 6 5
# node11 node13 10 1
# node14 node15 6 5
# node14 node16 10 1'''

s, k, *edges = data.split('\n')
k = int(k)
edges = [edge.split() for edge in edges]
edges = [(edge[0], edge[1], int(edge[2]), int(edge[3])) for edge in edges]


# Step 1: Construct the Suffix Tree
tree = {}
for parent, child, start, length in edges:
    if parent not in tree:
        tree[parent] = []
    # Subtract 1 from start because the problem statement seems to use 1-based indexing
    tree[parent].append((child, s[start-1:start-1+length]))

def count_leaves(node):
    """Count the number of leaf nodes reachable from the given node."""
    if node not in tree:  # If a leaf node
        return 1
    return sum(count_leaves(child) for child, _ in tree[node])

def find_longest_repeating(node, current_path=""):
    """Find the longest repeating substring by traversing the tree."""
    if node not in tree:  # Leaf node, base case
        return "", 0
    
    longest_substring, max_length = "", 0
    for child, substring in tree[node]:
        # Count the number of leaves (occurrences) for the current node
        leaf_count = count_leaves(child)
        if leaf_count >= k:
            # Continue searching from this child
            new_path = current_path + substring
            current_substring, current_length = find_longest_repeating(child, new_path)
            if current_length > max_length:
                longest_substring, max_length = current_substring, current_length
            elif current_length == max_length and current_substring < longest_substring:
                longest_substring, max_length = current_substring, current_length
        if len(current_path + substring) > max_length and leaf_count >= k:
            longest_substring, max_length = current_path + substring, len(current_path + substring)

    return longest_substring, max_length

# Execute the adjusted logic to find the longest repeating substring
longest_repeating, _ = find_longest_repeating("node1")

print(longest_repeating)
