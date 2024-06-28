from util import get_data, get_output_path


def reconstruct_string_from_kmers(k_mers):
    string = k_mers[0]
    for k_mer in k_mers[1:]:
        string += k_mer[-1]

    return string


if __name__ == "__main__":
    data = get_data(__file__)
#     data ='''ACCGA
# CCGAA
# CGAAG
# GAAGC
# AAGCT'''

    kmers = data.split('\n')
    string = reconstruct_string_from_kmers(kmers)

    with open(get_output_path(__file__), "w") as f:
        print(string)
        print(string, file=f)
