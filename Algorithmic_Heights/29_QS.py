from util import get_data

data = get_data(__file__)
numbers = list(map(int, data.split('\n')[1].split(' ')))

def quicksort(numbers):
  if len(numbers) <= 1:
    return numbers
  pivot = numbers[0]
  left = []
  right = []
  for i in range(1, len(numbers)):
    if numbers[i] < pivot:
      left.append(numbers[i])
    else:
      right.append(numbers[i])
  return quicksort(left) + [pivot] + quicksort(right)

with open('Algorithmic_Heights/output/29_QS.txt', 'w') as f:
    f.write(' '.join(map(str, quicksort(numbers))) + '\n')
