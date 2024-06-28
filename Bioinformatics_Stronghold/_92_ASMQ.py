from util import get_data


data = get_data(__file__)
# data = '''GATTACA
# TACTACTAC
# ATTGAT
# GAAGA'''


lengths = sorted([len(line) for line in data.split('\n')], reverse=True)
total_contig_length = sum(lengths)

N50, N75 = None, None
for i in range(len(lengths)):
    if N50 is None and sum(lengths[:i+1]) >= total_contig_length * 0.5:
        N50 = lengths[i]
    if N75 is None and sum(lengths[:i+1]) >= total_contig_length * 0.75:
        N75 = lengths[i]
        
print(N50, N75)
