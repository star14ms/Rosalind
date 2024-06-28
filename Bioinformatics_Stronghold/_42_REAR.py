### hard
from util import get_data
import numpy as np

data = get_data(__file__)
# data = '''1 2 3 4 5 6 7 8 9 10
# 3 1 5 2 7 4 9 6 10 8

# 3 10 8 2 5 4 7 1 6 9
# 5 2 3 1 7 4 10 8 6 9

# 8 6 7 9 4 1 3 10 2 5
# 8 2 7 6 9 1 5 3 10 4

# 3 9 10 4 1 8 6 7 5 2
# 2 9 8 5 1 7 3 4 6 10

# 1 2 3 4 5 6 7 8 9 10
# 1 2 3 4 5 6 7 8 9 10

# 9 1 3 2 8 5 4 10 7 6
# 9 3 5 8 1 10 7 4 2 6'''
data = data.split('\n\n')
pairs = list(map(lambda x: list(map(lambda y: list(map(int, y.split())), x.split('\n'))), data))


def get_l_r_ends(pair1, pair2):
    r_end = len(pair1)-1
    while pair1[r_end] == pair2[r_end]:
        r_end -= 1

    l_end = 0
    while pair1[l_end] == pair2[l_end]:
        l_end += 1
            
    return l_end, r_end


def get_reversal_results(pair1, pair2):
    results = set()
    # protect_set = set()

    l_end, r_end = get_l_r_ends(pair1, pair2)
    len_lr = r_end-l_end+1

    for window_size in range(len_lr, 1, -1):
        for i in range(l_end, r_end-window_size+2):
            temp = pair2.copy()
            temp[i:i+window_size] = temp[i:i+window_size][::-1]
            
            if np.array_equal(pair1, temp):
                return [(1, i, window_size)]

            # check l_end and r_end is shortened
            new_l_end, new_r_end = get_l_r_ends(pair1, temp)

            priority = (r_end - l_end + 1) - (new_r_end - new_l_end + 1)
            if priority > 0:
                results.add((priority, i, window_size))

            diff_p_distance = np.where(pair1 == pair2, 0, 1).sum() - np.where(pair1 == temp, 0, 1).sum()

            if diff_p_distance > 1:
                results.add((1, i, window_size))

            # check if N in a row are reversed
            for group_size in range(2, r_end-l_end+1):
                for j in range(l_end, r_end-group_size+2):
                    if np.array_equal(temp[j:j+group_size], pair1[j:j+group_size]):
                        for k in range(len(temp)):
                            if set(temp[l_end:j]) != set(pair1[l_end:j]) or \
                                set(temp[j+group_size:r_end+1]) != set(pair1[j+group_size:r_end+1]):
                                # print('protect', temp[j:j+group_size], pair1[j:j+group_size])
                                # protect_set = protect_set.union(range(i+i+window_size-(j+group_size), i+i+window_size-(j+group_size)+group_size))
                                break
                        else:
                            results.add((group_size, i, window_size))

                    if np.array_equal(temp[j:j+group_size][::-1], pair1[j:j+group_size]):
                        for k in range(len(temp)): # check if two groups should interact each other but isolated
                            if set(temp[l_end:j]) != set(pair1[l_end:j]) or \
                                set(temp[j+group_size:r_end+1]) != set(pair1[j+group_size:r_end+1]):
                                break
                        else:
                            results.add((group_size-1, i, window_size))

    # for result in results.copy():
    #     if set(range(result[1], result[1]+result[2])) & protect_set:
    #         results.remove(result)

    # highest priority
    results = [result for result in results if result[0] == max(results, key=lambda x: x[0])[0]]

    return results


reversal_distances = []

for pair1, pair2 in pairs:
    pair1 = np.array(pair1)
    pair2 = np.array(pair2)
    queue = [(pair1, pair2, 0)]
    minimum_reversal_distance = float('inf')

    if np.array_equal(pair1, pair2):
        reversal_distances.append(0)
        continue

    while queue:
        pair1, pair2, reversal_distance = queue.pop()

        results = get_reversal_results(pair1, pair2)

        for _, i, window_size in results:
            temp = pair2.copy()
            temp[i:i+window_size] = temp[i:i+window_size][::-1]

            if np.array_equal(pair1, temp):
                minimum_reversal_distance = min(minimum_reversal_distance, reversal_distance+1)
                # for i in range(len(queue)-1, -1, -1):
                #     if queue[i][2] >= minimum_reversal_distance:
                #         queue.pop(i)
            else:
                if minimum_reversal_distance > reversal_distance+1:
                    queue.append((pair1, temp, reversal_distance+1))

    reversal_distances.append(minimum_reversal_distance)

print(*reversal_distances)
