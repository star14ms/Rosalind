### ChatGPT (https://chatgpt.com/share/2f9a010f-d9e0-4d27-a257-e82972f289ed)
from util import get_data, get_output_path
from Bio import Phylo, SeqIO
from io import StringIO


# data = get_data(__file__)
data = '''(((ostrich,cat)rat,(duck,fly)mouse)dog,(elephant,pikachu)hamster)robot;
>ostrich
AC
>cat
CA
>duck
T-
>fly
GC
>elephant
-T
>pikachu
AA'''


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

def dp_assign_sequences(node):
    """Dynamic programming to assign sequences to internal nodes optimally."""
    if node.is_terminal():
        return [node.data['sequence']]
    
    child_sequences = []
    for child in node.clades:
        child_sequences.extend(dp_assign_sequences(child))
    length = len(child_sequences[0]) if child_sequences else 0
    optimal_sequence_bases = []

    for i in range(length):
        # Choose the most common base at each position
        bases = [seq[i] for seq in child_sequences if seq]
        most_common = max(set(bases), key=bases.count)
        most_commons = set([base for base in bases if bases.count(base) == bases.count(most_common)])
        optimal_sequence_bases.append(most_commons)
        
        for child in node.clades:
            if isinstance(child.data['sequence'], str):
                continue
            for seq in filter(lambda seq: seq[i] not in most_commons, child.data['sequence']):
                if len(child.data['sequence']) > 1:
                    # print(f"Removing {seq} from {child.name}")
                    child.data['sequence'].remove(seq)
        
    def possible_optimal_sequences(optimal_sequence_bases, i=0, previous_sequence=''):
        if i == len(optimal_sequence_bases):
            return [previous_sequence]

        optimal_sequecnces = []
        for base in optimal_sequence_bases[i]:
            optimal_sequecnces.extend(possible_optimal_sequences(optimal_sequence_bases, i+1, previous_sequence + base))
            
        return optimal_sequecnces

    node.data['sequence'] = [''.join(optimal_sequence) \
        for optimal_sequence in possible_optimal_sequences(optimal_sequence_bases)
    ]
    print(node.name, node.data['sequence'])
    return node.data['sequence']

# Calculate the total Hamming distance after assigning sequences
def calculate_total_distance(tree):
    total_distance = 0
    for node in tree.get_nonterminals(order='postorder'):  # Nonterminal nodes
        for child in node.clades:
            if isinstance(child.data['sequence'], str):
                child.data['sequence'] = [child.data['sequence']]
            if isinstance(node.data['sequence'], str):
                node.data['sequence'] = [node.data['sequence']]

            if child.data['sequence'] and node.data['sequence']:
                minimum_distance = float('inf')
                best_child_sequence = None
                best_node_sequence = None
                for child_sequence in child.data['sequence']:
                    for node_sequence in node.data['sequence']:
                        distance = hamming_distance(child_sequence, node_sequence)
                        if distance < minimum_distance:
                            minimum_distance = distance
                            best_child_sequence = child_sequence
                            best_node_sequence = node_sequence
                
                child.data['sequence'] = best_child_sequence
                node.data['sequence'] = best_node_sequence

                distance = hamming_distance( child.data['sequence'], node.data['sequence'])
                total_distance += distance
                # print(f"Node: {node}, Child: {child}, Distance: {distance}")
                # print(f"{node.data['sequence']}")
                # print(f"{child.data['sequence']}")
    return total_distance

# Initialize node data with parent
init_node_data_with_parents(tree)

# Assign sequences using dynamic programming
dp_assign_sequences(tree.root)

# Calculate total Hamming distance
total_distance = calculate_total_distance(tree)


with open(get_output_path(__file__), 'w') as output_data:
    print(total_distance)
    output_data.write(f"{total_distance}\n")

    for clade in tree.get_nonterminals(order='preorder'):
        if clade.data['sequence']:
            print(f">{clade.name}\n{clade.data['sequence']}")
            output_data.write(f">{clade.name}\n{clade.data['sequence']}\n")
