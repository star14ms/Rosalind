
def get_data(file_suffix):
    suffix = file_suffix.rstrip('.py').split('/')[-1].split('_')[-1].lower()
    with open('data/rosalind_' + suffix + '.txt', 'r') as f:
        return f.read().strip()