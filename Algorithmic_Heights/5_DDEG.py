from util import get_data, get_degrees_array

data = get_data(__file__)
edges = list(map(lambda x: list(map(int, x.split(' ')), ), data.split('\n')[1:]))


def double_degree_array(edges):
    degrees = get_degrees_array(edges)
    degrees = list(degrees.values())
    result = [0] * len(degrees)
    for i in range(len(degrees)):
        for j in range(len(edges)):
            if i + 1 == edges[j][0]:
                result[i] += degrees[edges[j][1] - 1]
            elif i + 1 == edges[j][1]:
                result[i] += degrees[edges[j][0] - 1]
    return result


double_degrees = double_degree_array(edges)
print(*double_degrees)

with open('Algorithmic_Heights/output/5_DDEG.txt', 'w') as output_data:
  output_data.write(' '.join(map(str, double_degrees)) + '\n')