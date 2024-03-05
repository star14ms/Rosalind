from util import get_data

data = get_data(__file__)

numbers = list(map(int, data.split('\n')[1].split()))

def build_max_heap(numbers):
    heap = []
    for number in numbers:
        heap.append(number)
        i = len(heap) - 1
        while i > 0:
            parent = (i - 1) // 2
            if heap[i] > heap[parent]:
                heap[i], heap[parent] = heap[parent], heap[i]
                i = parent
            else:
                break
    return heap

heap = build_max_heap(numbers)
print(heap)

with open('Algorithmic_Heights/output/11_HEA.txt', 'w') as f:
    f.write(' '.join(map(str, heap)) + '\n')