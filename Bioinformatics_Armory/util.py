import os


def get_filepath(file_suffix):
    current_directory = os.path.realpath(__file__).split('/')[-2]
    suffix = file_suffix.rstrip('.py').split('/')[-1].split('_')[-1].lower()
    file_path = f'data/{current_directory}/rosalind_{suffix}.txt'
    return file_path


def get_data(file_suffix):
    file_path = get_filepath(file_suffix)
    with open(file_path, 'r') as f:
        return f.read().strip()


def get_output_path(file_suffix, ext='txt'):
    current_directory = os.path.realpath(__file__).split('/')[-2]
    suffix = file_suffix.rstrip('.py').split('/')[-1]
    file_path = f'./{current_directory}/output/{suffix}.{ext}'
    return file_path
