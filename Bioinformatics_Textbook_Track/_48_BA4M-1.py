### Too Slow (../Bioinformatics_Stronghold/86_PDPL.py)
from util import get_data
import importlib.util
import sys

spec = importlib.util.spec_from_file_location("module.name", "Bioinformatics_Stronghold/86_PDPL.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
find_query_set = module.find_query_set


def get_pairwise_distances(spectrum, abs=False):
    pairwise_distances = []
    for i in range(len(spectrum)):
        for j in range(len(spectrum)):
            pairwise_distances.append(spectrum[j] - spectrum[i])
    
    return list(map(abs, sorted(pairwise_distances))) if abs else sorted(pairwise_distances)


def solve_turnpike_problem(pairwise_distances):
    # input [-10 -8 -7 -6 -5 -4 -3 -3 -2 -2 0 0 0 0 0 2 2 3 3 4 5 6 7 8 10]
    # return [0 2 4 7 10]
    
    pass
    

if __name__ == "__main__":

    data = get_data(__file__)
    # data ='''-10 -8 -7 -6 -5 -4 -3 -3 -2 -2 0 0 0 0 0 2 2 3 3 4 5 6 7 8 10'''
    
    # distances = get_pairwise_distances([0, 2, 4, 7])
    # print(distances)

    pairwise_distances = list(map(int, data.split()))
    multiset = [n for n in pairwise_distances if n > 0]
    
    find_query_set.cache = 0
    sys.setrecursionlimit(1500)
    line_segment = find_query_set(multiset)
    line_segment_complement = [line_segment[-1] - query for query in reversed(line_segment)]
    # line_segment = solve_turnpike_problem(pairwise_distances)

    print(*line_segment_complement)
