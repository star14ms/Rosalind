from util import get_data, get_output_path
import re

data = get_data(__file__)
# data = '''cat dog elephant ostrich mouse rabbit robot
# 01xxx00
# x11xx00
# 111x00x'''

species = data.split('\n')[0].split()
character_matrix = data.split('\n')[1:]
quartets = []

f = open(get_output_path(__file__), 'w')

for row in character_matrix:
    if row.count('1') >= 2 and row.count('0') >= 2:
        idxs_1 = list(map(lambda x: x.span()[0], re.finditer(r'1', row)))
        idxs_0 = list(map(lambda x: x.span()[0], re.finditer(r'0', row)))
        
        for i in range(len(idxs_1)):
            for j in range(i+1, len(idxs_1)):
                for k in range(len(idxs_0)):
                    for l in range(k+1, len(idxs_0)):
                        quartet = {idxs_1[i], idxs_1[j], idxs_0[k], idxs_0[l]}
                        if quartet not in quartets:
                            print(
                              f'{{{species[idxs_1[i]]}, {species[idxs_1[j]]}}} {{{species[idxs_0[k]]}, {species[idxs_0[l]]}}}'
                            )
                            f.write(
                              f'{{{species[idxs_1[i]]}, {species[idxs_1[j]]}}} {{{species[idxs_0[k]]}, {species[idxs_0[l]]}}}\n'
                            )

                            quartets.append({idxs_1[i], idxs_1[j], idxs_0[k], idxs_0[l]})

f.close()
