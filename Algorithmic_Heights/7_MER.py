from util import get_data

data = get_data(__file__)

arrays = data.split('\n')
arr1, arr2 = list(map(int, arrays[1].split())), list(map(int, arrays[3].split()))
merged_array = arr1 + arr2
merged_array.sort()

print(merged_array)

with open('Algorithmic_Heights/output/7_MER.txt', 'w') as f:
  f.write(' '.join(map(str, merged_array)) + '\n')