from util import get_data

data = get_data(__file__)

lines = data.split('\n')

for i in range(1, len(lines), 2):
    print(lines[i])