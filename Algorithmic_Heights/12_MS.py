from util import get_data

data = get_data(__file__)

numbers = list(map(int, data.split('\n')[1].split()))

print(numbers)

def merge_sort(numbers):
    if len(numbers) == 1:
        return numbers
    mid = len(numbers) // 2
    left = merge_sort(numbers[:mid])
    right = merge_sort(numbers[mid:])
    return merge(left, right)
  
def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
  
sorted_numbers = merge_sort(numbers)
print(sorted_numbers)

with open('Algorithmic_Heights/output/12_MS.txt', 'w') as f:
    f.write(' '.join(map(str, sorted_numbers)) + '\n')
