from util import get_data, get_output_path
import re


def get_quartets(character_matrix, taxon):
    quartets = []
    quartets_str = []
  
    for row in character_matrix:
        if row.count('1') >= 2 and row.count('0') >= 2:
            idxs_1 = list(map(lambda x: x.span()[0], re.finditer(r'1', row)))
            idxs_0 = list(map(lambda x: x.span()[0], re.finditer(r'0', row)))
            
            for i in range(len(idxs_1)):
                for j in range(i+1, len(idxs_1)):
                    for k in range(len(idxs_0)):
                        for l in range(k+1, len(idxs_0)):
                            quartet = ({idxs_1[i], idxs_1[j]}, {idxs_0[k], idxs_0[l]})

                            if quartet not in quartets and quartet[::-1] not in quartets:
                                quartets.append(quartet)

                                quartets_str.append((
                                  set([taxon[idxs_1[i]], taxon[idxs_1[j]]]), 
                                  set([taxon[idxs_0[k]], taxon[idxs_0[l]]]),
                                ))
                                
    return quartets, quartets_str


if __name__ == '__main__':
    data = get_data(__file__)
    # data = '''cat dog elephant ostrich mouse rabbit robot
    # 01xxx00
    # x11xx00
    # 111x00x'''

    taxon = data.split('\n')[0].split()
    character_matrix = data.split('\n')[1:]
    quartets, quartets_str = get_quartets(character_matrix, taxon)

    with open(get_output_path(__file__), 'w') as f:
        for quartet_str in quartets_str:
            print(str(quartet_str)[1:-1].replace("'", '').replace('}, {', '} {'))
            print(str(quartet_str)[1:-1].replace("'", '').replace('}, {', '} {'), file=f)
