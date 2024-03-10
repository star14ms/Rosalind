from util import get_data, get_output_path

data = get_data(__file__)

arrays = data.split('\n')[1:]
arrays = [list(map(int, array.split())) for array in arrays]

def two_sum(array):
  for i in range(len(array)):
      for j in range(i + 1, len(array)):
          if array[i] + array[j] == 0:
              return (i + 1, j + 1)
  
  return -1


two_sum_list = []
for array in arrays:
  two_sum_list.append(two_sum(array))
  

with open(get_output_path(__file__), 'w') as f:
  for two_sum_indexs in two_sum_list:
    # print(*two_sum_indexs)
    if two_sum_indexs == -1:
      f.write(str(two_sum_indexs) + '\n')
    else:
      f.write(' '.join(map(str, two_sum_indexs)) + '\n')
