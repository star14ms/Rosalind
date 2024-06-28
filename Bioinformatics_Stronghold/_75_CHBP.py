##################################################
# Character-Based Phylogeny
#
# http://rosalind.info/problems/CHBP/
# 
# Given: A list of n species (n <=q 80) and an n-column
#  character table C in which the jth column denotes
#  the jth species.
# 
# Return: An unrooted binary tree in Newick format
#  that models C.
#
# AUTHOR : dohlee
##################################################

# Your imports here
from util import get_data, get_output_path
import numpy as np


# Your codes here
def merge_two_nodes(characterTable, nodeNames, i, j):
	"""Merge two nodes."""
	assert i < j
	nodeNames[i] = '(%s,%s)' % (nodeNames[i], nodeNames[j])
	nodeNames.pop(j)

	for row in characterTable:
		row.pop(j)

	if len(characterTable) > 1:
		toRemove = [i for i, row in enumerate(characterTable) if row.count('1') == 1 or row.count('0') == 1]
		for i in toRemove:
			del characterTable[i]

def select_nodes_to_merge(characterTable):
	"""When characters of two nodes are consistent for all rows
	in character table, they are ready to be merged.
	"""
	for i in range(len(characterTable[0])):
		for j in range(i+1, len(characterTable[0])):
			if all(row[i] == row[j] for row in characterTable):
				return i, j

	return None, None

def reconstruct_tree(characterTable, nodeNames):
	"""Reconstruct unrooted binary tree from character table by
	iteratively merging two nodes.
	"""
	i, j = select_nodes_to_merge(characterTable)

	while not (i is None and j is None):
		merge_two_nodes(characterTable, nodeNames, i, j)
		i, j = select_nodes_to_merge(characterTable)
		print(i, j)

	return '(%s)' % ','.join(nodeNames)


if __name__ == '__main__':
    # Load the data.
		data = get_data(__file__)
		nodeNames = data.strip().split('\n')[0].split()
		characterTable = [list(row) for row in data.strip().split('\n')[1:]]
		# characterTable = np.array(characterTable, dtype=int)
  
		tree = reconstruct_tree(characterTable, nodeNames)

		# Print output
		with open(get_output_path(__file__), 'w') as f:
				print(tree)
				f.write(tree + '\n')
