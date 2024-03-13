from util import get_data, get_output_path
from Bio import Entrez, SeqIO

ids = get_data(__file__)

Entrez.email = "your_name@your_mail_server.com"
handle = Entrez.efetch(db="nucleotide", id=ids, rettype="fasta")
records = list(SeqIO.parse(handle, "fasta"))

longest_seq = min(records, key=lambda x: len(x.seq))
index = filter(lambda x: longest_seq.id == records[x].id, range(len(records))).__next__()
fasta = records[index].format("fasta")

print(fasta)

with open(get_output_path(__file__), 'w') as f:
  f.write(fasta)
