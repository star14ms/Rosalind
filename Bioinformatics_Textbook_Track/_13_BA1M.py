# complement to _12_BA1L.py
from util import get_data


def number_to_pattern(number, k):
    pattern = ''

    for i in range(k-1, -1, -1):
      if 1 * 4 ** i > number:
        number = number - 0 * 4 ** i
        pattern += 'A'
      elif 2 * 4 ** i > number:
        number = number - 1 * 4 ** i
        pattern += 'C'
      elif 3 * 4 ** i > number:
        number = number - 2 * 4 ** i
        pattern += 'G'
      elif 4 * 4 ** i > number:
        number = number - 3 * 4 ** i
        pattern += 'T'

    return pattern


if __name__ == "__main__":
    data = get_data(__file__)
#     data ='''45
# 4'''

    number, k = data.split()

    pattern = number_to_pattern(int(number), int(k))
    print(pattern)
