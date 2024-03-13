from util import get_data, get_output_path
from Bio import Entrez, SeqIO

ids = get_data(__file__)
# ids = '''JX205496.1 JX469991.1'''

Entrez.email = "your_name@your_mail_server.com"
handle = Entrez.efetch(db="nucleotide", id=ids, rettype="fasta")
records = list(SeqIO.parse(handle, "fasta"))
# fastas = list(map(lambda x: str(x.seq), records))

for i, record in enumerate(records):
  with open(get_output_path(f'5_NEED{i+1}', 'fasta'), 'w') as f:
    fasta = record.format("fasta")
    f.write(fasta)

# cd ./Bioinformatics_Armory/output/
# needle -endweight true -endopen 10 -endextend 1 5_NEED1.fasta 5_NEED2.fasta
# cd ../..