from util import get_data, get_output_path
import numpy as np

data = get_data(__file__)
# data = '''
# cat dog elephant mouse rabbit rat
# 011101
# 001101
# 001100'''

# data = '''
# cat dog elephant mouse rabbit rat robot
# 0111011
# 0011010
# 0011001'''


species = data.strip().split('\n')[0].split()
character_table = [list(row) for row in data.strip().split('\n')[1:]]
character_table = np.array(character_table, dtype=int)

species_initial = species.copy()
character_table_initial = character_table.copy()
n_characteristics = character_table.shape[0]


def get_similar_scores(current_vector, character_table):
  current_vector = np.expand_dims(current_vector, axis=1)
  current_vector = np.broadcast_to(current_vector, character_table.shape)
  similarity_matrix = np.where(character_table == current_vector, 0, 1)
  distance_matrix = similarity_matrix.sum(axis=0)
  
  return distance_matrix


newick_str = ''
queue = [np.ones(character_table.shape[0], dtype=int)]

while queue and character_table.shape[1] > 0:
  current_vector = queue.pop()
  distance_matrix = get_similar_scores(current_vector, character_table)
  neighbors = np.where(distance_matrix == distance_matrix.min())[0].tolist()
  
  if len(neighbors) == 0:
    continue

  groups = [(neighbors[0],)]
  for neighbor in neighbors[1:]:
    neighbor_character = character_table[:, neighbor]
    
    for i in range(len(groups)):
      group_character = character_table[:, groups[i][0]]
      if (neighbor_character == group_character).all(): # twins
        groups[i] += (neighbor,)
        break
    else:
      groups.append((neighbor,))

  # build newick string
  new_newick_str = ''
  for twins in groups:
    part_newick_str = ','.join([species[index] for index in twins])
    # if len(groups) > 1:
    #   part_newick_str = '(' + part_newick_str + ')'
    new_newick_str += part_newick_str + ',' if twins != groups[-1] else part_newick_str

  current_specie = ''
  for i in range(character_table_initial.shape[1]):
    if (character_table_initial[:, i] == current_vector).all():
      current_specie += species_initial[i] + ','
  current_specie = current_specie[:-1]
  
  # print(species, current_specie, groups, character_table)

  if newick_str == '':
    newick_str = '(' + new_newick_str + ')'
  else:
    newick_str = '(' + newick_str + ',' + new_newick_str + ')'

  # next species to search neighbors
  for twins in groups:
    queue.append(character_table[:, twins[0]])

  # remove asigned columns
  character_table = np.delete(character_table, neighbors, axis=1)
  
  for neighbor in sorted(neighbors, reverse=True):
    species.pop(neighbor)

newick_str += ';'
print(newick_str)

CTBL = __import__('56_CTBL')
CTBL.solve_newick_problem(newick_str)

with open(get_output_path(__file__), 'w') as f:
  f.write(newick_str + '\n')
