from util import get_data
import re

# data = get_data('46_EDIT.py')
data = '''>Rosalind_39
PLEASANTLY
>Rosalind_11
MEANLY'''

data = data.split('>')[1:]
s1, s2 = [x.split('\n', 1)[1].replace('\n', '') for x in data]

print(len(s1), len(s2))

queue = [(0, 0, 0, 0)]
min_edit_distance = float('inf')

while queue:
  edit_distance, s1_cursor, s2_cursor, shift = queue.pop()
  # print(len(queue))

  if s1_cursor >= len(s1) or s2_cursor >= len(s2):
    if edit_distance < min_edit_distance:
      min_edit_distance = edit_distance
      for i in range(len(queue)-1, -1, -1):
        if queue[i][0] >= min_edit_distance:
          queue.pop(i)
    continue

  # assuming no any corresponding with s1[s1_cursor] in s2
  if edit_distance + 1 < min_edit_distance:
    queue.append((edit_distance+1, s1_cursor+1, s2_cursor, shift+1))

  # assuming there are correspondings with s1[s1_cursor] in s2
  temp_queue = []
  for matching in re.finditer(s1[s1_cursor], s2[s2_cursor:]):
    distance = matching.span()[0]
    if edit_distance + max(0, distance-shift) < min_edit_distance:
      temp_queue.append((edit_distance + max(0, distance-shift), s1_cursor+1, s2_cursor+distance+1, 0))

  queue.extend(reversed(temp_queue))
  # print(s1, s1[s1_cursor], shift)
  # print(s2)
  # if queue:
  #   print(queue[-1])


print(min_edit_distance)
