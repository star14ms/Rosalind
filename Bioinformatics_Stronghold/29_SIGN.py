from util import get_data

data = get_data(__file__)

n = int(data)

def get_signed_permutations(n, array=[]):
    if len(array) == n:
        return [array]
    else:
      permutations = []
      for i in range(1, n+1):
        if i not in array and -i not in array:
          permutations += get_signed_permutations(n, array + [i])
          permutations += get_signed_permutations(n, array + [-i])
      return permutations


permutations = get_signed_permutations(n)

with open('output/29_SIGN.txt', 'w') as f:
  f.write(str(len(permutations)) + '\n')
  for permutation in permutations:
    f.write(' '.join(map(str, permutation)) + '\n')
