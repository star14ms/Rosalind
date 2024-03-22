from util import get_data
import numpy as np

data = get_data(__file__)
# data = '''1 2 3 4 5 6 7 8 9 10
# 1 8 9 3 2 7 6 5 4 10'''
pair1, pair2 = data.split('\n')
pair1, pair2 = list(map(int, pair1.split())), list(map(int, pair2.split()))


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


def get_minimum_reversal_distances(pair1, pair2):
    if np.array_equal(pair1, pair2):
      return 0, []

    queue = [(pair1, pair2, 0, [])]
    minimum_reversal_distance = float('inf')

    while queue:
        pair1, pair2, reversal_distance, reversals = queue.pop()

        results = get_reversal_results(pair1, pair2)

        for _, i, window_size in results:
            temp = pair2.copy()
            temp[i:i+window_size] = temp[i:i+window_size][::-1]

            if np.array_equal(pair1, temp):
                minimum_reversal_distance = min(minimum_reversal_distance, reversal_distance+1)
                minimum_reversals = reversals + [(i+1, i+window_size)]
                # for i in range(len(queue)-1, -1, -1):
                #     if queue[i][2] >= minimum_reversal_distance:
                #         queue.pop(i)
            else:
                if minimum_reversal_distance > reversal_distance+1:
                    queue.append((pair1, temp, reversal_distance+1, reversals+[(i+1, i+window_size)]))

    return minimum_reversal_distance, minimum_reversals


pair1 = np.array(pair1)
pair2 = np.array(pair2)

minimum_reversal_distance, reversals = get_minimum_reversal_distances(pair1, pair2)

print(minimum_reversal_distance)
for reversal in reversed(reversals):
    print(*reversal)
