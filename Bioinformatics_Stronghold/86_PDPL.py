from util import get_data, get_output_path
from multiset import Multiset
import sys


# reverse opperation
def get_difference_mutiset(query_set):
    multiset = Multiset()

    for space in range(1, len(query_set)):
        for i in range(len(query_set) - space):
            multiset.add(abs(query_set[i] - query_set[i + space]))
            
    return multiset


def find_query_set(multiset, query_set=[]):
    global multiset_origin
    find_query_set.cache += 1

    if query_set == []:
        return find_query_set(multiset[:-1], [0, multiset[-1]])
    elif len(query_set) * (len(query_set) - 1) / 2 == len(multiset_origin):
        if sorted(list(get_difference_mutiset(query_set))) == multiset_origin:
            return query_set
        return False
    elif len(multiset) == 0:
        return False

    possible_distance_from_first = True
    possible_distance_from_last = True
    for query in query_set:
        if abs(multiset[-1] - query) not in multiset_origin:
            possible_distance_from_first = False
        if abs(query_set[-1] - multiset[-1] - query) not in multiset_origin:
            possible_distance_from_last = False

    # if biggest distance is from the frist element
    if possible_distance_from_first:
        new_query_set = query_set.copy()
        new_query_set.append(multiset[-1])
        result = find_query_set(multiset[:-1], sorted(new_query_set))
        if result:
            return result

    # if biggest distance is from the last element
    if possible_distance_from_last:
        new_query_set = query_set.copy()
        new_query_set.append(query_set[-1] - multiset[-1])
        result = find_query_set(multiset[:-1], sorted(new_query_set))
        if result:
            return result

    result = find_query_set(multiset[:-1], query_set)
    if result:
        return result
    return False


if __name__ == '__main__':
    data = get_data(__file__)
    # data = '''2 2 3 3 4 5 6 7 8 10'''
    # data = '''1 2 3 3 4 5 5 7 9 9 6 12 10 14 15'''

    multiset = sorted(list(map(int, data.split())))
    multiset_origin = multiset.copy()

    find_query_set.cache = 0

    sys.setrecursionlimit(1500)
    query_sets = find_query_set(multiset)
    query_sets_complement = [query_sets[-1] - query for query in reversed(query_sets)]
    print(*query_sets)
    print(*query_sets_complement)

    print(find_query_set.cache)

    with open(get_output_path(__file__), 'w') as file:
        file.write(' '.join(map(str, query_sets_complement)))
