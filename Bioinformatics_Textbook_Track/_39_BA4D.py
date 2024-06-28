### https://github.com/andreyrozumnyi/rosalind/blob/master/Chapter%204/BA4D.py
from util import get_data, get_output_path
# from constant import INTEGER_MASS_TABLE


# def n_peptides_equal_to_parent_mass(mass):
#     if mass in n_peptides_equal_to_parent_mass.mass:
#         return n_peptides_equal_to_parent_mass.mass[mass]

#     n_peptides = 0
#     for value in INTEGER_MASS_TABLE.values():
#         if value == mass:
#             n_peptides += 1
#         elif value < mass:
#             n_peptides += n_peptides_equal_to_parent_mass(mass - value)
#         else:
#             continue
    
#     n_peptides_equal_to_parent_mass.mass[mass] = n_peptides
#     return n_peptides


keys = [57, 71, 87, 97, 99, 101, 103, 113, 114, 115, 128, 129, 131, 137, 147, 156, 163, 186]
def calc_varinats(m):
    ways = [0]*(m + 1)
    index = m
    ways[m] = 1
    while index > 0:
        for key in keys:
            ways[index-key] += ways[index]

        index -= 1
        while ways[index] == 0:
            index -= 1

    return ways[0]


if __name__ == "__main__":
    mass = get_data(__file__)
    # mass ='''1024'''

    # n_peptides_equal_to_parent_mass.mass = {}
    # n_peptides = n_peptides_equal_to_parent_mass(int(mass))
    # print(n_peptides_equal_to_parent_mass.mass)
    # print(n_peptides)
    
    n_peptides = calc_varinats(int(mass))

    print(n_peptides)
        