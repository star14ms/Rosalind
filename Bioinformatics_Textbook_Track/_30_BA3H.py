from util import get_data, get_output_path


def reconstruct_string_from_k_mer(k_mers):
    k = len(k_mers[0])
    string = k_mers[0]
    
    while len(k_mers) > 1:
        k_mer = k_mers.pop(0)
        
        if string[:k-1] == k_mer[1:]:
            string = k_mer[0] + string
        elif string[-(k-1):] == k_mer[:-1]:
            string = string + k_mer[-1]
        else:
            k_mers.append(k_mer)

    return string


if __name__ == "__main__":
    data = get_data(__file__)
#     data ='''4
# CTTA
# ACCA
# TACC
# GGCT
# GCTT
# TTAC'''

    k, k_mers = data.split('\n', 1)
    k_mers = k_mers.split('\n')
    
    text = reconstruct_string_from_k_mer(k_mers)

    with open(get_output_path(__file__), "w") as f:
        print(text)
        print(text, file=f)
