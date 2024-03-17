from util import get_data, get_output_path

# data = get_data(__file__)
data = '''>Rosalind_23
AACCTTGG
>Rosalind_64
ACACTGTGA'''
data = data.split('>')[1:]
dna1, dna2 = [x.split('\n', 1)[1].replace('\n', '') for x in data]

print(len(dna1), len(dna2))

# find the longest common subsequences
m = [[0] * (1 + len(dna2)) for i in range(1 + len(dna1))]
longest, x_longest = 0, 0
for x in range(1, 1 + len(dna1)):
    for y in range(1, 1 + len(dna2)):
        if dna1[x - 1] == dna2[y - 1]:
            m[x][y] = m[x - 1][y - 1] + 1
            if m[x][y] > longest:
                longest = m[x][y]
                x_longest = x
        else:
            m[x][y] = max(m[x - 1][y], m[x][y - 1])

print(m)
print(longest, x_longest)
print(dna1[x_longest - longest: x_longest])

# using dynamic programming, we can find the longest common subsequence
# when searching, both pointers should be in similar position to make longest common subsequence
# if the pointers are not in similar position, the pointer should be moved to the next position

# when deciding the next common subsequence,
# first, decide the searching base of one of the pointers
# second, move the other pointer to find the longest common subsequence
# third, searching each of next base (so total 4 bases) are searched
# fourth, choose the base, sum of each distance from the latest common subsequence should be the shortest

start_index = 0
index1 = start_index
index2 = 0
substring_list = []
queue = [('', index1, index2)]

while queue:
  # print(len(queue), len(queue[-1][0]))
  substring, index1, index2 = queue.pop(-1 if len(queue) > 100 else 0)
  cache = {}
  shortest_distance = float('inf')

  for base in ['A', 'C', 'T', 'G']:
    if base in dna1[index1:] and base in dna2[index2:]:
      distance = dna1.index(base, index1) + dna2.index(base, index2)
      cache[base] = distance
      if distance < shortest_distance:
        shortest_distance = distance

  if not cache:
    if len(substring_list) == 0 or len(substring) == len(substring_list[-1]):
      substring_list.append(substring)
    elif len(substring) > len(substring_list[-1]):
      substring_list = [substring]
      index1, index2 = 0, 0

      for i in range(len(substring)):
        char = substring[i]
        index1 = dna1.index(char, index1) + 1
        index2 = dna2.index(char, index2) + 1
        
        for j in range(len(queue)-1, -1, -1):
          substring_queue, index1_queue, index2_queue = queue[j]
          # print(len(substring_queue), len(substring[:i+1]), index1_queue, index1, index2_queue, index2)
          if len(substring_queue) < len(substring[:i+1]) and index1_queue > index1 and index2_queue > index2:
            queue.pop(i)
      
      # input(len(substring))
    continue

  # check if there are more than one base that has the same distance
  for base in cache:
    if cache[base] == shortest_distance:
      substring_new = substring + base
      index1_new = dna1.index(base, index1) + 1
      index2_new = dna2.index(base, index2) + 1

      for i in range(len(queue)):
        substring_queue, index1_queue, index2_queue = queue[i]
        if len(substring_list) != 0 and len(substring_queue) < len(substring_new) and \
          index1_queue > index1_new and index2_new > index1_queue:
          break
      else:
        queue.append((
          substring + base, 
          dna1.index(base, index1) + 1, 
          dna2.index(base, index2) + 1
        ))

print(substring_list)