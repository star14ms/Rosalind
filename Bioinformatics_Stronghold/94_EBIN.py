from util import get_data


data = get_data(__file__)
# data = '''17
# 0.1 0.2 0.3'''

data = data.split('\n')
n_alleles = int(data[0])
allele_frequency = list(map(float, data[1].split()))

allele_frequency_next = [round(n_alleles * frequency, 3) for frequency in allele_frequency]
print(*allele_frequency_next)