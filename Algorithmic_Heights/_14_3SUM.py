### hard
from util import get_data, get_output_path

data = get_data(__file__)

arrays = list(map(lambda x: list(map(int, x.split())), data.split('\n')[1:]))

# def get_3sum(array):
#     for i in range(len(array)):
#         for j in range(i + 1, len(array)):
#             for k in range(j + 1, len(array)):
#                 if array[i] + array[j] + array[k] == 0:
#                     return [array[i], array[j], array[k]]
#     return -1

# more efficient solution
# def get_3sum(array):
#     print(len(array))
#     for i in range(len(array)):
#         for j in range(i + 1, len(array)):
#             if -(array[i] + array[j]) in array[j + 1:]:
#                 return [array[i], array[j], -(array[i] + array[j])]
#     return -1

# more efficient solution using two pointers
def get_3sum(array):
    array_len = len(array)
    for i in range(array_len - 2):
        left = i + 1
        right = array_len - 1
        while left < right:
            if array[i] + array[left] + array[right] == 0:
                print(array[i], array[left], array[right])
                return array[i], array[left], array[right]
            elif array[i] + array[left] + array[right] < 0:
                left += 1
            else:
                right -= 1

    print(-1)
    return -1


sorted_arrays = tuple(map(lambda x: sorted(x), arrays))
threesum_list = tuple(map(get_3sum, sorted_arrays))

threesum_indexs = []
for array, threesum in zip(arrays, threesum_list):
  if threesum == -1:
    threesum_indexs.append(-1)
  else:
    threesum_indexs.append(sorted([
      array.index(threesum[0])+1, 
      array.index(threesum[1])+1, 
      array.index(threesum[2])+1
    ]))

with open(get_output_path(__file__), 'w') as f:
  for threesum in threesum_indexs:
    if threesum == -1:
      f.write('-1\n')
    else:
      f.write(' '.join(map(str, threesum)) + '\n')
