from util import get_data, get_output_path

data = get_data(__file__)
# data = '''ATAGA
# ATC
# GAT'''
dnas = data.split('\n')

trie = {}
n_node = 1

for dna in dnas:
  cursor = 1

  for base in dna:
    if (cursor, base) not in trie:
      n_node += 1
      trie[(cursor, base)] = n_node
      cursor = n_node
    else:
      cursor = trie[(cursor, base)]


for key, value in trie.items():
  cursor, base = key
  print(cursor, value, base)


with open(get_output_path(__file__), 'w') as f:
  for key, value in trie.items():
    cursor, base = key
    f.write(f'{cursor} {value} {base}\n')