from util import get_data, get_output_path


def build_complete_cycles(k_mers, prefix=''):
    if prefix == '':
        return build_complete_cycles(k_mers[1:], k_mers[0])
    elif len(k_mers) == 0:
        is_cycle = prefix[:k] == prefix[-k:]
        return [prefix[:-k]] if is_cycle else []

    cycles = set()
    for i, k_mer in enumerate(k_mers):
        if prefix[-k:] == k_mer[:k]:
            cycles = cycles.union(
              build_complete_cycles(k_mers[:i] + k_mers[i+1:], prefix + k_mer[-1])
            )
    
    return cycles


if __name__ == '__main__':
    data = get_data(__file__)
    # data = '''CAG
    # AGT
    # GTT
    # TTT
    # TTG
    # TGG
    # GGC
    # GCG
    # CGT
    # GTT
    # TTC
    # TCA
    # CAA
    # AAT
    # ATT
    # TTC
    # TCA'''

    k_mers = data.split('\n')
    k = len(k_mers[0]) - 1

    cycles = build_complete_cycles(k_mers)

    with open(get_output_path(__file__), 'w') as f:
        print(*cycles, sep='\n')
        print(*cycles, sep='\n', file=f)

    print(len(cycles))
