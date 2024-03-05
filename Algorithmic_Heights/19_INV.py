from util import get_data

data = get_data(__file__)

numbers = list(map(int, data.split('\n')[1].split()))

def count_n_inversions(arr):
    n = len(arr)
    if n <= 1:
        return arr, 0
    else:
        a, x = count_n_inversions(arr[:n // 2])
        b, y = count_n_inversions(arr[n // 2:])
        c, z = count_n_inversions_merge(a, b)
        return c, x + y + z
      
def count_n_inversions_merge(a, b):
    c = []
    i = j = inversions = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
            inversions += len(a) - i
    c += a[i:]
    c += b[j:]
    return c, inversions

print(count_n_inversions(numbers)[1])