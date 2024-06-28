from util import get_data
from Bio import Phylo
from io import StringIO

data = get_data(__file__)
# data = '''(dog:42,cat:33);
# cat dog

# ((dog:4,cat:3):74,robot:98,elephant:58);
# dog elephant'''
data = [d.split('\n') for d in data.split('\n\n')]

distances = []

for newick, species in data:
  tree = Phylo.read(StringIO(newick), "newick")
  specie1, specie2 = species.split()
  
  # distance = sum(node.branch_length for node in tree.trace(specie1, specie2) if node.branch_length is not None)
  # distance += tree.find_any(specie1).branch_length

  distance = tree.distance(specie1, specie2)
  distances.append(int(distance))

print(' '.join(map(str, distances)))
