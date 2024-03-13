from util import get_filepath, get_output_path
from Bio import SeqIO

fastaq = SeqIO.parse(get_filepath(__file__), "fastq")

fasta = SeqIO.write(fastaq, get_output_path(__file__), "fasta")
