from util import get_data

data = get_data(__file__)
# data = '''2

# 2 4
# 1 2
# -1 2
# 1 -2
# -1 -2

# 3 4
# 1 2
# 2 3
# -1 -2
# -2 -3'''
data = data.split('\n\n')[1:]
clauses_set = list(map(lambda x: list(map(lambda y: list(map(int, y.split())), x.split('\n'))), data))


def get_mentioned(clauses, n_vars):
    mentioned = [0] * (n_vars + 1)
    for a, b in clauses:
        mentioned[abs(a)] += 1
        mentioned[abs(b)] += 1
    return mentioned

def get_2SAT(clauses, n_vars):
    solved = False
    dist = [None] * (n_vars + 1)

    mentioned = get_mentioned(clauses, n_vars)
    for i in range(1, n_vars + 1):
        if mentioned[i] == 0:
            dist[i] = False

    priority = sorted(range(1, n_vars + 1), key=lambda x: mentioned[x], reverse=True)
    queue = [(dist, clauses, priority)]

    while queue:
        _dist, _clauses, _priority = queue.pop(-1)
        print(f'queue: {len(queue)} | n clauses {len(_clauses)} | N left: {_dist.count(None)-1}     ', end='\r')

        result = _get_2SAT(_dist[:], _clauses[:], _priority[:], offset_bool=True)
        if result[0]:
            if None not in result[0][1:]:
                dist = result[0]
                solved = True
                break
            queue.append(result)

            if result[0].count(None) == _dist.count(None) - 1:
                continue

        result = _get_2SAT(_dist, _clauses, _priority, offset_bool=False)
        if result[0]:
            if None not in result[0][1:]:
                dist = result[0]
                solved = True
                break
            queue.append(result)
            
    if not solved:
        print(' '*64, end='\r')
        print(0)
        return False

    print(' '*64, end='\r')
    print(1)
    return list(map(lambda x: x if dist[x] else -x, range(1, len(dist))))


def _get_2SAT(dist, clauses, priority, offset_bool=True):
    index_None = priority.pop(0)
    dist[index_None] = offset_bool

    for i in range(1, len(dist)+1):
        for a, b in filter(lambda clause: i in clause or -i in clause, clauses):
            if (dist[i] is False and i == a) or (dist[i] is True and i == -a):
                if dist[abs(b)] is None:
                    dist[abs(b)] = True if b > 0 else False
                    priority.remove(abs(b))
            elif (dist[i] is False and i == b) or (dist[i] is True and i == -b):
                if dist[abs(a)] is None:
                    dist[abs(a)] = True if a > 0 else False
                    priority.remove(abs(a))

        for i in range(len(clauses) - 1, -1, -1):
            a, b = clauses[i]
            if dist[abs(a)] != None and dist[abs(b)] != None:
                if (dist[abs(a)] is False and a > 0) or (dist[abs(a)] is True and a < 0):
                    if (dist[abs(b)] is False and b > 0) or (dist[abs(b)] is True and b < 0):
                        return False, None, None
                clauses.remove([a, b])

    return dist, clauses, priority


from time import perf_counter
results = []
start = perf_counter()
for clauses in clauses_set:
    n_vars, n_clauses = clauses.pop(0)

    dist = get_2SAT(clauses, n_vars)
    if dist:
        result = str(1) + ' ' + ' '.join(map(str, dist))
        results.append(result)
    else:
        results.append('0')

end = perf_counter()
print((end - start) // 60, 'minutes', f'{(end - start) % 60:f} seconds')


with open('Algorithmic_Heights/output/32_2SAT.txt', 'w') as f:
    for result in results:
        f.write(result + '\n')