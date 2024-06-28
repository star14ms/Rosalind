from util import get_data, get_output_path
from Bio import Phylo
from io import StringIO
import numpy as np

newick_string = get_data("56_CTBL.py")
# newick_string = '''(dog,((elephant,mouse,(zeus),(yy)),robot),cat);'''

tree = Phylo.read(StringIO(newick_string), "newick")

# get max depth
max_depth = 0
for clade in tree.find_clades():
  if clade.name is not None:
    max_depth = max(max_depth, len(tree.get_path(clade)))
    
# get elements
elements = []
for clade in tree.find_clades():
  if clade.name:
    elements.append(clade.name)

elements.sort()

id = 0
lexicographical_ordered_ids = {}
for element in elements:
  if element:
    lexicographical_ordered_ids[element] = id
    id += 1


# incorrect solution
# def get_character_table(tree, depth=0):
#   for child in tree.root:
#     id = lexicographical_ordered_ids.get(child.name)

#     if id is not None and depth < max_depth-1:
#       for i in range(max_depth-1-depth):
#         get_character_table.cache[i][id] = 0
#     else:
#       get_character_table(child, depth+1)


def get_character_table(tree, depth=0, depths_to_fill_zero=[]):
  splited = False
  for child in tree.root:
    id = lexicographical_ordered_ids.get(child.name)
    if id is not None:
      if depth < max_depth-1:
        for i in range(max_depth-1-depth):
          get_character_table.cache[i][id] = 0

      for depth_zero in depths_to_fill_zero:
        # get_character_table.cache[depth_zero-1][id] = 0
        for j in range(depth_zero):
          get_character_table.cache[j][id] = 0
    else:
      new_depths_to_fill_zero = depths_to_fill_zero + ([(max_depth-1-depth)] if splited else [])
      get_character_table(child, depth+1, new_depths_to_fill_zero)
      splited = True


get_character_table.cache = np.ones([max_depth-1, len(elements)], dtype=int)
get_character_table(tree)

with open(get_output_path(__file__), 'w') as f:
  for row in get_character_table.cache:
    print(''.join(map(str, row)))
    f.write(''.join(map(str, row)) + '\n')

# print(get_character_table.cache.shape)
