from util import get_data


def pattern_count(text, pattern):
    count = 0
    pattern_length = len(pattern)
    for i in range(len(text) - pattern_length + 1):
        if text[i:i+pattern_length] == pattern:
            count += 1
    return count


if __name__ == "__main__":
    data = get_data(__file__)
    # Sample dataset
#     data ='''GCGCG
# GCG'''

    text, pattern = data.splitlines()

    # Calculate and print the result
    count = pattern_count(text, pattern)
    print(count)
