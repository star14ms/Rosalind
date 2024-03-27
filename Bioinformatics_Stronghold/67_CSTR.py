from util import get_data, get_output_path

data = get_data(__file__)
# data = '''ATGCTACC
# CGTTTACC
# ATTCGACC
# AGTCTCCC
# CGTCTATC'''

dnas = data.split('\n')


def generate_character_table(dna_strings):
    # Initialize the character table
    character_table = []
    
    # The length of the DNA strings
    string_length = len(dna_strings[0])
    
    # Iterate over each position of the strings
    for pos in range(string_length):
        # Find the unique symbols at this position across all strings
        symbols = {string[pos] for string in dna_strings}
        
        # Proceed only if there are at most two unique symbols (at most two possible choices)
        if len(symbols) == 2:
            # Create a mapping of the symbols to '0' or '1'
            symbol_to_binary = {symbol: str(idx) for idx, symbol in enumerate(symbols)}
            
            # Generate the binary representation for this SNP position for all strings
            binary_representation = ''.join(symbol_to_binary[string[pos]] for string in dna_strings)
            
            # Add this representation to the character table
            character_table.append(binary_representation)
    
    return character_table


# Generate and print the character table
character_table = generate_character_table(dnas)

with open(get_output_path(__file__), 'w') as f:
    for row in character_table:
        if row.count('0') > 1 and row.count('1') > 1:
            print(row)
            f.write(row + '\n')
