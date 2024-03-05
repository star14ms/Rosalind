
def get_data(file_suffix):
    suffix = file_suffix.rstrip('.py').split('/')[-1].split('_')[-1].lower()
    with open('data/rosalind_' + suffix + '.txt', 'r') as f:
        return f.read().strip()


def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


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
