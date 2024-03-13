from util import get_data
from Bio.Seq import Seq

data = get_data(__file__)

my_seq = Seq(data)

print(my_seq.count('A'), my_seq.count('C'), my_seq.count('G'), my_seq.count('T'))

print(my_seq.complement())
print(my_seq.reverse_complement())
# print(my_seq.translate())
# print(my_seq.transcribe())