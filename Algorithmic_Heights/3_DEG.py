from util import get_data, get_output_path, get_degrees_array

data = get_data(__file__)

edges = data.split('\n')[1:]
edges = list(map(lambda x: list(map(int, x.split(' '))), edges))

degrees = get_degrees_array(edges)
print(degrees)

with open(get_output_path(__file__), 'w') as output_data:
  output_data.write(' '.join(map(str, degrees.values())) + '\n')
