from util import get_data, get_output_path

data = get_data(__file__)
# data = '''10
# {1, 2, 3, 4, 5}
# {2, 8, 5, 10}'''

n, set1, set2 = data.split('\n')
set1 = set(map(int, set1[1:-1].split(', ')))
set2 = set(map(int, set2[1:-1].split(', ')))

# A ∪ B
print(set1 | set2) # or set1.union(set2)
# A ∩ B
print(set1 & set2) # or set1.intersection(set2)
# A − B
print(set1 - set2) # or set1.difference(set2)
# B − A
print(set2 - set1) # or set2.difference(set1)
# Ac
print(set(range(1, int(n)+1)) - set1) # or set(range(1, int(n)+1)).difference(set1)
# Bc
print(set(range(1, int(n)+1)) - set2) # or set(range(1, int(n)+1)).difference(set2)


with open(get_output_path(__file__), 'w') as f:
  f.write(str(set1 | set2) + '\n')
  f.write(str(set1 & set2) + '\n')
  f.write(str(set1 - set2) + '\n')
  f.write(str(set2 - set1) + '\n')
  f.write(str(set(range(1, int(n)+1)) - set1) + '\n')
  f.write(str(set(range(1, int(n)+1)) - set2) + '\n')
