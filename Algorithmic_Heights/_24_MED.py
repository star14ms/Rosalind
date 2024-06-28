from util import get_data

data = get_data(__file__)

_, numbers, nth = data.split('\n')
numbers = list(map(int, numbers.split()))

sorted_numbers = sorted(numbers)
print(sorted_numbers[int(nth) - 1])