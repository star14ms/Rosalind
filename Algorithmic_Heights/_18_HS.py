from util import get_data, get_output_path

data = get_data(__file__)
numbers = list(map(int, data.split('\n')[1].split()))

def heap_sort(arr):
    def sift_down(start, end):
        root = start
        while True:
            child = 2 * root + 1
            if child > end:
                break
            if child + 1 <= end and arr[child] < arr[child + 1]:
                child += 1
            if arr[root] < arr[child]:
                arr[root], arr[child] = arr[child], arr[root]
                root = child
            else:
                break

    for start in range((len(arr) - 2) // 2, -1, -1):
        sift_down(start, len(arr) - 1)

    for end in range(len(arr) - 1, 0, -1):
        arr[end], arr[0] = arr[0], arr[end]
        sift_down(0, end - 1)
    return arr
  
print(' '.join(map(str, heap_sort(numbers))))
      
with open(get_output_path(__file__), 'w') as f:
  f.write(' '.join(map(str, heap_sort(numbers))) + '\n')