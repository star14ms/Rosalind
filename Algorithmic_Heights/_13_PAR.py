from util import get_data, get_output_path

data = get_data(__file__)

numbers = list(map(int, data.split('\n')[1].split()))

def two_way_partition(numbers):
    pivot = numbers[0]
    left = []
    right = []
    for number in numbers[1:]:
        if number < pivot:
            left.append(number)
        else:
            right.append(number)
    return left + [pivot] + right
  
sorted_numbers = two_way_partition(numbers)
print(sorted_numbers)
print(numbers[0])

with open(get_output_path(__file__), 'w') as f:
    f.write(' '.join(map(str, sorted_numbers)) + '\n')