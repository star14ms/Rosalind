from util import get_data, get_output_path

data = get_data('63_LREP.py')
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

dna, k, *edges = data.split('\n')
k = int(k)
edges = [edge.split() for edge in edges]
edges = [(edge[0], edge[1], int(edge[2])-1, int(edge[3])) for edge in edges]


# The longest substing of dna that is repeated at least k times in suffix tree of edges
def longest_repeated_substring(dna, k):
  n = len(dna)
  suffixes = [dna[i:] for i in range(n)]
  suffixes.sort()
  lrs = ''
  for i in range(n - 1):
    length = 0
    while suffixes[i][length] == suffixes[i + 1][length]:
      length += 1
    if length > len(lrs):
      for j in range(len(dna) - length + 1):
        count = 0
        if dna[j:j + length] == suffixes[i][:length]:
          count += 1
      if count >= k:
          lrs = dna[j:j + length]
      lrs = suffixes[i][:length]
  return lrs

print(longest_repeated_substring(dna, k))


# give every possible substring of trie based on edges
def get_substrings(edges):
  substrings = {}
  for edge in edges.copy():
    node1, node2, start, length = edge
    previous_edge = list(filter(lambda edge: edge[1] == node1, substrings.keys()))

    if len(previous_edge) > 0:
      substrings[(previous_edge[0][0], node2)] = substrings[previous_edge[0]] + dna[start:start+length]
      # del substrings[previous_edge[0]]
    else:
      substrings[(node1, node2)] = dna[start:start+length]
    # del edges[edges.index(edge)]
    
    print(len(substrings), len(edges), end='\r')
  return list(substrings.values())


substrings = get_substrings(edges)
print(substrings)
substrings = list(filter(lambda substring: substring[-1] == '$', substrings))
print(substrings)

longest_substring = ''
for i, substring in enumerate(substrings):
  substring = substring[:-1]
  print(len(longest_substring), i, len(substrings), end='\r')

  if len(substring) < len(longest_substring):
    continue

  count = 0
  for i in range(len(dna) - len(substring) + 1):
    if dna[i:i+len(substring)] == substring:
      count += 1

  if count >= k and len(substring) > len(longest_substring):
    longest_substring = substring
  
print()
print(longest_substring)


# # give every possible substring of trie based on edges
# def count_substrings(edges):
#   count_of_subtrings = {}
#   for edge in edges:
#     _, _, start, length = edge

#     if count_of_subtrings.get((start, length)) is None:
#       count_of_subtrings[(start, length)] = 0
#     else:
#       count_of_subtrings[(start, length)] += 1
    
#   return count_of_subtrings


# count_of_substrings = count_substrings(edges)
# print(count_of_substrings)
# repeated_substrings = filter(lambda x: x[1] >= k, count_of_substrings.items())
# longest_substring = max(repeated_substrings, key=lambda x: x[0][1])

# print(dna[longest_substring[0][0]:longest_substring[0][0]+longest_substring[0][1]])
