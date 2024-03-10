from util import get_data, get_output_path

data = get_data(__file__)

numbers = list(map(int, data.split('\n')[1].split()))

def three_way_partition(numbers):
    pivot = numbers[0]
    left = []
    right = []
    equal = []
    for number in numbers[1:]:
        if number < pivot:
            left.append(number)
        elif number > pivot:
            right.append(number)
        else:
            equal.append(number)
    return left + [pivot] + equal + right
  
sorted_numbers = three_way_partition(numbers)

with open(get_output_path(__file__), 'w') as f:
    f.write(' '.join(map(str, sorted_numbers)) + '\n')