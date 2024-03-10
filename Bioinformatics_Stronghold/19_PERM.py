from util import get_data, get_output_path

number = get_data(__file__)
number = int(number)

def perm(n):
    if n == 1:
        return [[1]]
    else:
        perms = []
        for p in perm(n-1):
            for i in range(n):
                perms.append(p[:i] + [n] + p[i:])
        return perms
  

with open(get_output_path(__file__), 'w') as f:
    f.write(str(len(perm(number))) + '\n')
    for p in perm(number):
        f.write(' '.join(map(str, p)) + '\n')
