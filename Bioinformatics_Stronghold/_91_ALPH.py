### ChatGPT + Edits (https://chatgpt.com/share/2f9a010f-d9e0-4d27-a257-e82972f289ed)
from util import get_data, get_output_path
from Bio import Phylo, SeqIO
from io import StringIO


data = get_data(__file__)
# data = '''(((ostrich,cat)rat,(duck,fly)mouse)dog,(elephant,pikachu)hamster)robot;
# >ostrich
# AC
# >cat
# CA
# >duck
# T-
# >fly
# GC
# >elephant
# -T
# >pikachu
# AA'''


newick_tree, fasta_data = data.split('\n', 1)

# Read the Newick tree
tree = Phylo.read(StringIO(newick_tree), "newick")

# Parse FASTA data
sequences = {record.id: str(record.seq) for record in SeqIO.parse(StringIO(fasta_data), "fasta")}

def hamming_distance(seq1, seq2):
    """Calculate the Hamming distance between two sequences."""
    return sum(ch1 != ch2 for ch1, ch2 in zip(seq1, seq2))

def init_node_data_with_parents(tree):
    """Initialize node data and set parent references."""
    for node in tree.find_clades():
        for child in node.clades:
            child.parent = node  # Set parent
        if node.is_terminal():
            node.data = {'sequence': sequences.get(node.name, '')}
        else:
            node.data = {'sequence': None}

def dp_assign_sequences(node, i=0):
    """Dynamic programming to assign sequences to internal nodes optimally."""
    if node.is_terminal():
        return [node.data['sequence'][i]]

    bases = []
    for child in node.clades:
        bases.extend(dp_assign_sequences(child, i))

    # Choose the most common base at each position
    most_common = max(set(bases), key=bases.count)
    optimal_bases = set([base for base in bases if bases.count(base) == bases.count(most_common)])

    for child in node.clades:
        if isinstance(child.data['sequence'], str):
            continue
        for base in filter(lambda base: base not in optimal_bases, child.data['sequence'][i].copy()):
            if len(child.data['sequence'][i]) > 1:
                child.data['sequence'][i].remove(base)
                
    if node.data['sequence'] is None:
        node.data['sequence'] = [set(optimal_bases)]
    else:
        node.data['sequence'].append(optimal_bases)

    return node.data['sequence'][i]

# Calculate the total Hamming distance after assigning sequences
def calculate_total_distance(tree):
    total_distance = 0
    for node in tree.get_nonterminals(order='preorder'):  # Nonterminal nodes
        for child in node.clades:
            if isinstance(child.data['sequence'], str):
                child.data['sequence'] = [[base] for base in child.data['sequence']]
            if isinstance(node.data['sequence'], str):
                node.data['sequence'] = [[base] for base in child.data['sequence']]

            for i in range(seq_length):
                if child.data['sequence'] and node.data['sequence']:
                    match = False
                    for child_base in child.data['sequence'][i]:
                        for node_base in node.data['sequence'][i]:
                            if child_base == node_base:
                                child.data['sequence'][i] = child_base
                                node.data['sequence'][i] = node_base
                                match = True
                                break
                        if match:
                            break
                    
                    if not match:
                        child.data['sequence'][i] = child_base
                        node.data['sequence'][i] = node_base
                        total_distance += 1
    
    return total_distance

# Initialize node data with parent
init_node_data_with_parents(tree)
seq_length = len(tree.get_terminals()[0].data['sequence'])

# Assign sequences using dynamic programming
for i in range(seq_length):
    dp_assign_sequences(tree.root, i)

# Calculate total Hamming distance
total_distance = calculate_total_distance(tree)

tree.root.data['sequence'] = ''.join([base for base in tree.root.data['sequence']])
for node in tree.get_nonterminals(order='preorder'):
    for child in node.clades:
        child.data['sequence'] = ''.join([bases for bases in child.data['sequence']])


with open(get_output_path(__file__), 'w') as output_data:
    print(total_distance)
    output_data.write(f"{total_distance}\n")

    for clade in tree.get_nonterminals(order='preorder'):
        if clade.data['sequence']:
            print(f">{clade.name}\n{clade.data['sequence']}")
            output_data.write(f">{clade.name}\n{clade.data['sequence']}\n")

print(total_distance)
