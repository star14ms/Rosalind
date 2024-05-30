from util import get_data, get_output_path, align_with_emboss


'A-ACG-TA'
'| ||  ||'
'ACAC-CTA'


data = get_data('84_MGAP.py')
# data = '''>Rosalind_92
# AACGTA
# >Rosalind_47Z
# ACACCTA
# '''

data = data.split('>')[1:]
s1, s2 = [x.split('\n', 1)[1].replace('\n', '') for x in data]

score, substring1, substring2 = align_with_emboss(
  s1, s2,
  gapopen=1, gapextend=1, endweight=True, endopen=1, endextend=1,
)

n_gap = substring1.count('-') + substring2.count('-') 

missmatching = 0
for i in range(len(substring1)):
  if substring1[i] != substring2[i]:
    missmatching += 1

print(missmatching + n_gap)
print(n_gap)
