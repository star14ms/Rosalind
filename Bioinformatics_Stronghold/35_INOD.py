from util import get_data, get_output_path
from Bio.Seq import Seq

number = int(get_data(__file__))
# number = 6
line = 0
sum_line = 0

while number > sum_line + line + 1:
  line += 1
  print(number, line, sum_line)
  sum_line = sum_line + line
  
number - sum_line 

print(number - 2)