from util import get_data

data = get_data(__file__)

sorted_array, random_array = data.split('\n')[2:]

sorted_array = list(map(int, sorted_array.split()))
random_array = list(map(int, random_array.split()))

def binary_search(arr, x):
    l, r = 0, len(arr) - 1
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] == x:
            return mid + 1
        elif arr[mid] < x:
            l = mid + 1
        else:
            r = mid - 1
    return -1
  
  
index_array = [binary_search(sorted_array, x) for x in random_array]
  
print(' '.join(map(str, index_array)))

with open('Algorithmic_Heights/output/2_BINS.txt', 'w') as f:
    f.write(' '.join(str(binary_search(sorted_array, x)) for x in random_array))