from util import get_data, get_output_path, rna_to_protein_strings


if __name__ == "__main__":
    rna = get_data(__file__)
    # rna ='''AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA'''

    string = rna_to_protein_strings(rna, shifts=False, include_reverse_complement=False)

    with open(get_output_path(__file__), "w") as f:
        print(string)
        print(string, file=f)
