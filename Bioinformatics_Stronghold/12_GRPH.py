from util import get_data

data = get_data(__file__)

dnas = data.split('>')[1:]

f = open('output/12_GRPH.txt', 'w')

for dna in dnas:
    dna = dna.split('\n')
    dna_id = dna[0]
    dna = ''.join(dna[1:])

    for dna2 in dnas:
        dna2 = dna2.split('\n')
        dna2_id = dna2[0]
        dna2 = ''.join(dna2[1:])
        if dna_id != dna2_id:
            if dna[-3:] == dna2[:3]:
                f.write(dna_id + ' ' + dna2_id + '\n')
                print(dna_id + ' ' + dna2_id)

f.close()