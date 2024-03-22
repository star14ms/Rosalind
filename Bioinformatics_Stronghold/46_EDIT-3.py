from util import get_data

# data = get_data('46_EDIT.py')
data = '''>Rosalind_39
PLEASANTLY
>Rosalind_11
MEANLY'''

data = data.split('>')[1:]
s1, s2 = [x.split('\n', 1)[1].replace('\n', '') for x in data]


def get_edit_distance(s1_cursor, s2_cursor, shift):
  if (s1_cursor, s2_cursor) in cache:
    return max(0, cache[(s1_cursor, s2_cursor)] - shift)

  if s1_cursor >= len(s1):
    edit_distance = len(s2) - s2_cursor
    cache.update({(s1_cursor, s2_cursor): edit_distance})
    return edit_distance

  if s2_cursor >= len(s2):
    edit_distance = len(s1) - s1_cursor
    cache.update({(s1_cursor, s2_cursor): edit_distance})
    return edit_distance

  edit_distances = set()
  
  # Assuming s1[s1_cursor] and s2[s2_cursor] are the same
  if s1[s1_cursor] == s2[s2_cursor]:
    edit_distance = get_edit_distance(s1_cursor+1, s2_cursor+1, 0)
    cache.update({(s1_cursor, s2_cursor): edit_distance})
    return edit_distance

  # Assumming Deletion
  edit_distances.add(1 + get_edit_distance(s1_cursor+1, s2_cursor, shift+1))
  # Assumming Insertion
  edit_distances.add(1 + get_edit_distance(s1_cursor, s2_cursor+1, shift+1))
  # Assumming Substitution
  edit_distances.add(1 + get_edit_distance(s1_cursor+1, s2_cursor+1, shift+1))

  min_edit_distance = min(edit_distances)
  cache.update({(s1_cursor, s2_cursor): min_edit_distance})
  return min_edit_distance


cache = {}
min_edit_distance = get_edit_distance(0, 0, 0)

# x = filter(lambda x: x[0] == len(s1) or x[1] == len(s2), cache.keys())
# for a in x: # cache.keys()
#   print(a, cache[a])

print(len(s1), len(s2))
print(min_edit_distance)