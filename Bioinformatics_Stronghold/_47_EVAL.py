from util import get_data
from decimal import Decimal, ROUND_HALF_UP

data = get_data(__file__)
# data = '''10
# AG
# 0.25 0.5 0.75'''

length, dna, gc_array = data.split('\n')
length, gc_array = int(length), list(map(float, gc_array.split()))
expected_numbers = []

for gc_content in gc_array:
  g_or_c = gc_content / 2
  a_or_t = (1 - gc_content) / 2
  possibility = 1
  
  for base in dna:
    if base in 'GC':
      possibility *= g_or_c
    else:
      possibility *= a_or_t
      
  expected_number = possibility * (length - len(dna) + 1)

  print(expected_number, end=' ')

  # Convert the number to a Decimal and round it
  expected_number = Decimal(expected_number).quantize(Decimal('0.000'), rounding=ROUND_HALF_UP)
  expected_numbers.append(expected_number)

print()
print(' '.join(map(str, expected_numbers)))