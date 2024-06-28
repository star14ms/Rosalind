from util import get_data
from Bio import Entrez

data = get_data(__file__)
# data = '''Anthoxanthum
# 2003/7/25
# 2005/12/27'''

genus, date1, date2 = data.split('\n')

Entrez.email = "your_name@your_mail_server.com"
handle = Entrez.esearch(db="nucleotide", term=f'{genus} AND "{date1}"[PDAT] : "{date2}"[PDAT]')
record = Entrez.read(handle)

print(record["Count"])
