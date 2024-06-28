from util import get_data, get_output_path

data = get_data(__file__)

length, permutation = data.split('\n')
n = int(length)

permutation = list(map(int, permutation.split()))


def get_longest_increasing_subsequence(arr):
  n = len(arr)
  lis = [1]*n
  prev = [-1]*n
  max_len = 1
  max_index = 0

  for i in range(1, n):
    for j in range(0, i):
      if arr[i] > arr[j] and lis[i] < lis[j] + 1:
        lis[i] = lis[j] + 1
        prev[i] = j

    if lis[i] > max_len:
      max_len = lis[i]
      max_index = i

  subsequence = []
  while max_index != -1:
    subsequence.append(arr[max_index])
    max_index = prev[max_index]

  subsequence.reverse()
  return subsequence


def longest_decreasing_subsequence(arr):
  n = len(arr)
  lds = [1]*n
  prev = [-1]*n
  max_len = 1
  max_index = 0

  for i in range(1, n):
    for j in range(0, i):
      if arr[i] < arr[j] and lds[i] < lds[j] + 1:
        lds[i] = lds[j] + 1
        prev[i] = j

    if lds[i] > max_len:
      max_len = lds[i]
      max_index = i

  subsequence = []
  while max_index != -1:
    subsequence.append(arr[max_index])
    max_index = prev[max_index]

  subsequence.reverse()
  return subsequence

a = get_longest_increasing_subsequence(permutation)
b = longest_decreasing_subsequence(permutation)
print(*a)
print(*b)

with open(get_output_path(__file__), 'w') as f:
    f.write(' '.join(map(str, a)) + '\n')
    f.write(' '.join(map(str, b)) + '\n')
