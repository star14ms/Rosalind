### hard
from util import get_data
import numpy as np

data = get_data('42_REAR.py')
# data = '''1 2 3 4 5 6 7 8 9 10
# 3 1 5 2 7 4 9 6 10 8

# 3 10 8 2 5 4 7 1 6 9
# 5 2 3 1 7 4 10 8 6 9

# 8 6 7 9 4 1 3 10 2 5
# 8 2 7 6 9 1 5 3 10 4

# 3 9 10 4 1 8 6 7 5 2
# 2 9 8 5 1 7 3 4 6 10

# 1 2 3 4 5 6 7 8 9 10
# 1 2 3 4 5 6 7 8 9 10'''
data = data.split('\n\n')
pairs = list(map(lambda x: list(map(lambda y: list(map(int, y.split())), x.split('\n'))), data))


def get_reversal_results(pair1, pair2, return_min_distance=False, min_distance_of_next_n_turn=1):
    results = []
    
    for window_size in range(len(pair1)-1, 0, -1):
        for i in range(len(pair1)-window_size+1):
            temp = pair2.copy()
            temp[i:i+window_size] = temp[i:i+window_size][::-1]
      
            isolated = False
            for j in range(len(temp)):
                if pair1[j] != temp[j] and \
                    (j < 2 or (pair1[j-1] == temp[j-1] and pair1[j-2] == temp[j-2])) and \
                    (j > len(temp)-3 or (pair1[j+1] == temp[j+1] and pair1[j+2] == temp[j+2])):
                    isolated = True
                
            p_distance = np.where(pair1 == temp, 0, 1).sum()
            
            # measure the distance of each pair from pair1
            distance = np.sum([abs(np.where(pair1 == temp[i])[0][0] - i) ** 2 for i in range(len(temp))])
            if min_distance_of_next_n_turn > 1:
                distance = get_reversal_results(pair1, temp, return_min_distance=True, min_distance_of_next_n_turn=min_distance_of_next_n_turn-1)[1]
      
            results.append([p_distance, distance, isolated, i, window_size])

    if return_min_distance:
        return min(results, key=lambda x: x[1])
    return results

reversal_distances = []

for pair1, pair2 in pairs:
    pair1 = np.array(pair1)
    pair2 = np.array(pair2)
    reversal_distance = 0
    
    while not np.array_equal(pair1, pair2):
        # for i in range(len(pair1)):
        #     if pair1[i] != pair2[i]:
        #         break
        # j = np.where(pair1 == pair2[i])[0][0]
        # pair1[i:j+1] = pair1[i:j+1][::-1]
        
        results = get_reversal_results(pair1, pair2, min_distance_of_next_n_turn=1)
        
        if len(results) == 0:
          breakpoint()
          break

        min_p_distance, _, _, _, _ = min(results, key=lambda x: x[0])
        # min_distance = min(results, key=lambda x: x[1])[1]
        # print(pair1)
        # print(pair2)
        # print()
        result_min_p_distance = [item for item in results if item[0] == min_p_distance and not item[2]]
        # result_min_distance = [item for item in results if item[1] == min_distance and not item[2]]
        # breakpoint()

        if pair1[0] == pair2[-1] or pair1[-1] == pair2[0]:
          result_min_p_distance = [(0, 0, False, 0, 10)]

        if len(result_min_p_distance) == 1:
            _, _, _, i, window_size = result_min_p_distance[0]
        elif len(result_min_p_distance) > 1:
            _, _, _, i, window_size = min(result_min_p_distance, key=lambda x: x[1])
        else:
            _, _, _, i, window_size = min(results, key=lambda x: x[1])

        pair2[i:i+window_size] = pair2[i:i+window_size][::-1]
        reversal_distance += 1

    reversal_distances.append(reversal_distance)

print(*reversal_distances)


