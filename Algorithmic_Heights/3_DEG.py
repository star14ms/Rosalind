from util import get_data, get_degrees_array

data = get_data(__file__)

edges = data.split('\n')[1:]
edges = list(map(lambda x: list(map(int, x.split(' '))), edges))

degrees = get_degrees_array(edges)
print(degrees)

with open('Algorithmic_Heights/output/3_DEG.txt', 'w') as output_data:
  output_data.write(' '.join(map(str, degrees.values())) + '\n')
