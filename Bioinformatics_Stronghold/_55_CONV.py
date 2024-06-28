from util import get_data

data = get_data(__file__)
# data = '''186.07931 287.12699 548.20532 580.18077 681.22845 706.27446 782.27613 968.35544 968.35544
# 101.04768 158.06914 202.09536 318.09979 419.14747 463.17369'''

multiset1, multiset2 = (list(map(float, line.split())) for line in data.split('\n'))

# Minkowski difference
diff = [round(x-y, 5) for x in multiset1 for y in multiset2]

# Largest Multiplicity
max_multiplicity = max(diff.count(x) for x in diff)

print(max_multiplicity)

for x in diff:
  if diff.count(x) == max_multiplicity:
    print(x)
    break
