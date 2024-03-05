from util import get_data

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

with open('Algorithmic_Heights/output/20_PAR3.txt', 'w') as f:
    f.write(' '.join(map(str, sorted_numbers)) + '\n')