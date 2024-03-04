from util import get_data, reverse_complement

data = get_data(__file__)

dna1 = ''.join(data.split('\n')[1:])
dna2 = reverse_complement(dna1)


for i in range(len(dna1)):
    for length in range(2, 7):
        if i + length > len(dna1):
            break
      
        reverse_palindrome = dna1[i:i+length] == dna2[-i-length*2:-i-length]

        if reverse_palindrome:
            print(i+1, length*2)
