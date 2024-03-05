from util import get_data
from collections import Counter

data = get_data(__file__)

arrays = data.split('\n')[1:]
arrays = [list(map(int, array.split())) for array in arrays]

most_common_list = []
for array in arrays:
  top2 = Counter(array).most_common(2)

  if top2[0][1] == top2[1][1] or top2[0][1] < len(array) / 2:
    most_common_list.append(-1)
  else:
    most_common_list.append(top2[0][0])
  
print(*most_common_list)
  