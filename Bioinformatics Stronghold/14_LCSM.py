from util import get_data

data = get_data(__file__)

data = data.split('>')[1:]
data = [x.split('\n', 1) for x in data]
data = [x[1].replace('\n', '') for x in data]

def lcs(s1, s2):
    m = [[0] * (1 + len(s2)) for i in range(1 + len(s1))]
    longest, x_longest = 0, 0
    for x in range(1, 1 + len(s1)):
        for y in range(1, 1 + len(s2)):
            if s1[x - 1] == s2[y - 1]:
                m[x][y] = m[x - 1][y - 1] + 1
                if m[x][y] > longest:
                    longest = m[x][y]
                    x_longest = x
            else:
                m[x][y] = 0
    return s1[x_longest - longest: x_longest]

# new_data = []

# while len(new_data) > 2 or len(new_data) == 0:
#   new_data = []
#   for i in range(len(data)):
#     for j in range(len(data)):
#       if i <= j:
#         break
#       new_data.append(lcs(data[i], data[j]))
#       print(i, j, len(data))
#   data = new_data if new_data else data
#   print(len(data))

# print(new_data)

lgc_str = data[0]

for i in range(len(data)):
  for j in range(len(data)):
    if i <= j:
      break
    lgc_str = lcs(lgc_str, data[j])
    print(i, j, len(data))

print(lgc_str)

# lcs = longest common substring
# how about with 3 strings?
# lcs(s1, s2, s3) = lcs(lcs(s1, s2), s3)

# is it possible to do this with a list of strings?
# lcs([s1, s2, s3, s4]) = lcs(lcs(lcs(s1, s2), s3), s4)

# what if the lcs of three strings is second logest of first two strings?
# lcs(s1, s2, s3) = lcs(s1, s2) and lcs(s1, s3) and lcs(s2, s3)