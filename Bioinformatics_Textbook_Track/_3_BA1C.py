from util import get_data, get_output_path, reverse_complement


if __name__ == "__main__":
    data = get_data(__file__)
    # data ='''AAAACCCGGT'''

    seq_reverse_complement = reverse_complement(data)

    with open(get_output_path(__file__), "w") as f:
        print(seq_reverse_complement)
        print(seq_reverse_complement, file=f)
