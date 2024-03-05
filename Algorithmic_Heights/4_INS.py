from util import get_data

data = get_data(__file__)

numbers = list(map(int, data.split('\n')[1].split(' ')))

def insertion_sort(numbers):
  n_move = 0
  for i in range(1, len(numbers)):
    j = i
    while j > 0 and numbers[j - 1] > numbers[j]:
      n_move += 1
      numbers[j - 1], numbers[j] = numbers[j], numbers[j - 1]
      j -= 1
  return numbers, n_move

numbers, n_move = insertion_sort(numbers)
print(*numbers)
print(n_move)