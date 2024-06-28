from util import get_data, get_output_path


def convolution_of_spectrum(spectrum):
    convolution_elements = [spectrum[j] - spectrum[i] \
        for i in range(len(spectrum)-1) \
            for j in range(i+1, len(spectrum)) if spectrum[j] - spectrum[i] > 0]

    return sorted(sorted(convolution_elements), key=convolution_elements.count, reverse=True)


if __name__ == "__main__":
    data = get_data(__file__)
    # data ='''0 137 186 323'''

    spectrum = sorted(list(map(int, data.split())))
    # print(len(spectrum))
    # print(*spectrum)

    elements = convolution_of_spectrum(spectrum)
    
    with open(get_output_path(__file__), "w") as f:
        print(*elements)
        print(*elements, file=f)
    # print(len(elements))
    # print(sum(range(len(spectrum)-1)))
