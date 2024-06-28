### hard
from util import get_data
from Bio import Phylo
from io import StringIO
import re

data = get_data(__file__)
# data = '''(cat)dog;
# dog cat

# (dog,cat);
# dog cat'''
trees = data.split('\n\n')
trees = [tree.split('\n') for tree in trees]


class TreeNode:
    def __init__(self, name=''):
        self.name = name
        self.children = []
        self.elements = set()

def parse_newick(s):
    """Parses a Newick string and returns the root of the tree."""
    stack = []
    i = 0
    root = None
    key = None
    while i < len(s):
        if s[i] == '(':
            node = TreeNode()
            if stack:
                stack[-1].children.append(node)
            stack.append(node)
            i += 1
        elif s[i] == ',' or s[i] == ')':
            # if s[i-1] != ')' and s[i-1] != '(':
            if key is not None:
                leaf = TreeNode(key)
                stack[-1].children.append(leaf)
                stack[-1].elements.add(key)
                key = None
            if s[i] == ')':
                root = stack.pop()
                if len(stack) > 0:
                    for child in root.children:
                        stack[-1].elements = stack[-1].elements.union(child.elements)
                        if child.name:
                            stack[-1].elements.add(child.name)
            i += 1
        else:
            key_length = float('inf')
            if ',' in s[i:]:
                key_length = s[i:].index(',')
            if ')' in s[i:] and key_length > s[i:].index(')'):
                key_length = s[i:].index(')')
            if key_length != float('inf'):
                key = s[i:i+key_length]
                i += key_length
            else:
                root.name = s[i:].split(';')[0]
                break
    return root

def find_distance(root, name1, name2):
    """Finds the distance between two nodes in the tree."""
    # Implement LCA and distance calculation here
    depth1 = find_depth(root, name1)
    depth2 = find_depth(root, name2)
    
    sharing_depth = 1 if name1 in root.elements and name2 in root.elements else 0
    node = root

    while True:
        for child in node.children:
            if name1 == child.name or name2 == child.name:
                print(sharing_depth)
                node = child
                break
            if name1 in child.elements and name2 in child.elements:
                sharing_depth += 1
                node = child
                break
        else:
            break

    info = (depth1, depth2, sharing_depth, depth1 + depth2 - 2*sharing_depth + 2)

    if (depth1 == 0 or depth2 == 0):
        return abs(depth1 - depth2), info
    elif (depth1 != depth2 and (depth1 == sharing_depth or depth2 == sharing_depth)):
        return depth1 + depth2 - 2*sharing_depth, info
    else:
        return depth1 + depth2 - 2*sharing_depth + 2, info

def find_depth(node, name, depth=0):
    """Finds the depth of a node in the tree."""
    # Implement depth calculation here
    if node.name == name:
        return depth
    for child in node.children:
        if name == child.name:
            return depth + 1
        if name in child.elements:
            return find_depth(child, name, depth+1)


def get_distance(newick_string, key1, key2):
    index_key1 = newick_string.index(key1)
    index_key2 = newick_string.index(key2)

    if index_key1 < index_key2:
        newick_string = newick_string[index_key1:index_key2+len(key2)]
    else:
        newick_string = newick_string[index_key2:index_key1+len(key1)]
    newick_string = key1 + re.sub(r'[a-zA-Z_;]', '', newick_string) + key2

    previous_length = None
    while not previous_length or len(newick_string) != previous_length:
        previous_length = len(newick_string)
        newick_string = re.sub(r'\([,]*?\)', '', newick_string)

    state = ')' in newick_string, '(' in newick_string, ',' in newick_string

    if state == (True, False, False):
        distance = newick_string.count(')')
    elif state == (False, True, False):
        distance = newick_string.count('(')
    elif state == (False, False, True):
        distance = 2
    else:
        distance = newick_string.count(')') + newick_string.count('(') + 2
        
    return distance


distances = []

for newick_string, keys in trees:
    key1, key2 = keys.split()
    root = parse_newick(newick_string)
    distance, info = find_distance(root, key1, key2)
    distances.append(distance)


    tree = Phylo.read(StringIO(newick_string), "newick")

    # # # We can visualise the tree
    # # print(tree)

    # # # We can count terminals in the tree
    # # print(tree.count_terminals())

    len_trace = len(tree.trace(key1, key2))
    n_common_ancestor = len(tree.get_path(tree.common_ancestor(key1, key2)))

    if len(tree.get_path(key1)) == n_common_ancestor or len(tree.get_path(key2)) == n_common_ancestor:
        len_trace = abs(len(tree.get_path(key1)) - len(tree.get_path(key2)))
        
    # if len(tree.get_path(key1)) != len(tree.get_path(key2)) and (
    #     len(tree.get_path(key1)) == n_common_ancestor or len(tree.get_path(key2)) == n_common_ancestor):
    #     print(*info[:-1], distance)
    #     print(len(tree.get_path(key1)), len(tree.get_path(key2)), n_common_ancestor, len_trace)

    if len_trace != distance:
        print(*info[:-1], distance)
        print(len(tree.get_path(key1)), len(tree.get_path(key2)), n_common_ancestor, len_trace)

    # distance2 = get_distance(newick_string, key1, key2)
    # if distance != distance2:
    #     print(*info[:-1], distance, distance2)
    
    get_distance(newick_string, key1, key2)
    

print(' '.join(map(str, distances)))
