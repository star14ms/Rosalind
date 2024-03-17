import os

def get_data(file_suffix):
    current_directory = os.path.realpath(__file__).split('/')[-2]
    suffix = file_suffix.rstrip('.py').split('/')[-1].split('_')[-1].lower()
    file_path = f'data/{current_directory}/rosalind_{suffix}.txt'
    with open(file_path, 'r') as f:
        return f.read().strip()
    

def get_output_path(file_suffix):
    current_directory = os.path.realpath(__file__).split('/')[-2]
    suffix = file_suffix.rstrip('.py').split('/')[-1]
    file_path = f'./{current_directory}/output/{suffix}.txt'
    return file_path


def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def get_degrees_array(edges):
    degrees = {}
    for a, b in edges:
        if degrees.get(a) == None:
            degrees[a] = 1
        else:
            degrees[a] += 1
    
        if degrees.get(b) == None:
            degrees[b] = 1
        else:
            degrees[b] += 1
        
    return dict(sorted(degrees.items()))


def get_edges_with_2_degree(edges):
    degrees = get_degrees_array(edges)

    edges_new = edges[:]
    for k, v in degrees.items():
        if degrees[k] == 1:
            for edge in filter(lambda x: x[0] == k or x[1] == k, edges):
                edges_new.remove(edge)

    return edges_new
