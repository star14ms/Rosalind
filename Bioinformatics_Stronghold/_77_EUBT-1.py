from util import get_data, get_output_path


data = get_data(__file__)
data = 'dog cat mouse elephant'

species = data.split()

# possible unrooted binary trees = (2n-5)!! = (2*4-5)!! = 3!! = 3*1 = 3
# possible rooted binary trees = (2n-3)!! = (2*4-3)!! = 5!! = 5*3*1 = 15


newick_tree = f',{species.pop(0)});'


def build_tree(choices, tree):
  if len(choices) == 2:
    return ['(' * (tree.count(')') + 1) + f'{choices[0]},{choices[1]})' + tree]
  
  trees = []

  for i in range(len(choices)):
    trees.extend(build_tree(choices[:i] + choices[i+1:], f',{choices[i]})' + tree))
    
  return trees


print(*build_tree(species, newick_tree), sep='\n')

with open(get_output_path(__file__), 'w') as output_data:
  output_data.write('\n'.join(build_tree(species, newick_tree)) + '\n')
