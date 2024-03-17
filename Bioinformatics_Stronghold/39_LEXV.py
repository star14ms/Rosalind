from util import get_data, get_output_path

data = get_data(__file__)
# data ='''D N A
# 3'''
alphabets, n = data.split('\n')
alphabets = alphabets.split()


def lexicographic_order(alphabets, n, prefix=''):
  strings = []
  for alphabet in alphabets:
    print(prefix+alphabet)
    strings.append(prefix+alphabet)
    if n > 1:
      strings += lexicographic_order(alphabets, n-1, prefix+alphabet)
      
  return strings


strings = lexicographic_order(alphabets, int(n))


with open(get_output_path(__file__), 'w') as f:
  for string in strings:
    f.write(string + '\n')
  