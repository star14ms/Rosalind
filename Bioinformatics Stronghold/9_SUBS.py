from util import get_data

data = get_data(__file__)

s, sub = data.split('\n')

indices = []

for i in range(len(s)):
    if s[i:].startswith(sub):
        indices.append(i + 1)

print(*indices)