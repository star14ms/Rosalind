from util import get_data, get_output_path

data = get_data(__file__)

def gc_content(dna):
    return (dna.count('G') + dna.count('C')) / len(dna) * 100

# fasta format
data = data.split('\n')
dna = ''

# f = open('data/rosalind_gc_output.txt', 'w')

# for line in data:
#     if line.startswith('>'):
#         if dna:
#             gc = gc_content(dna)
#             f.write(f'{id}\n{gc}\n')
#         id = line[1:]
#         dna = ''
#     else:
#         dna += line

# gc = gc_content(dna)
  
# f.close()

max_gc = 0
max_id = ''

for line in data:
    if line.startswith('>'):
        if dna:
            gc = gc_content(dna)
            if gc > max_gc:
                max_gc = gc
                max_id = id
        id = line[1:]
        dna = ''
    else:
        dna += line

gc = gc_content(dna)

with open(get_output_path(__file__), 'w') as f:
    f.write(f'{max_id}\n{max_gc}\n')