### hard
from util import get_data
from constant import MONOISOTOPIC_MASS_TABLE

data = get_data(__file__)
# data = '''1988.21104821
# 610.391039105
# 738.485999105
# 766.492149105
# 863.544909105
# 867.528589105
# 992.587499105
# 995.623549105
# 1120.6824591
# 1124.6661391
# 1221.7188991
# 1249.7250491
# 1377.8200091'''

masses = list(map(float, data.split('\n')))
parent_mass = masses.pop(0)


# Function to find matches for amino acids based on mass differences
def find_amino_acid_by_mass(mass_diff, tolerance=0.01):
    for aa, mass in MONOISOTOPIC_MASS_TABLE.items():
        if abs(mass - mass_diff) <= tolerance:
            return aa
    return None


def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if start not in graph:
        return None
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath: return newpath
    return None


def construct_graph(masses, parent_mass):
    graph = {}
    for i, mass in enumerate(masses):
        for j, next_mass in enumerate(masses):
            if i != j:
                mass_diff = next_mass - mass
                aa = find_amino_acid_by_mass(mass_diff)
                if aa:
                    if mass in graph:
                        graph[mass].append(next_mass)
                    else:
                        graph[mass] = [next_mass]
    return graph


# Using the parent mass to filter out potential b-ion and y-ion pairs
# This involves considering the entire peptide mass (parent_mass) and matching it with potential b and y ions
# For a peptide of mass M, its b-ion and y-ion should sum up to M - mass of water (18.01056)
peptide_mass = parent_mass - 18.01056
filtered_masses = [mass for mass in masses if mass < peptide_mass]

# Construct a graph based on the filtered masses
graph = construct_graph(filtered_masses, peptide_mass)

# Now, find a path through the graph that represents the peptide
# Since this approach may not directly give us the peptide, let's find any valid path for demonstration
path = find_path(graph, filtered_masses[0], filtered_masses[-1])

# Convert the path back to a peptide string if possible
if path:
    peptide = ''
    for i in range(len(path) - 1):
        mass_diff = path[i+1] - path[i]
        aa = find_amino_acid_by_mass(mass_diff)
        if aa:
            peptide += aa

expected_peptide_length = len(masses) // 2 - 1
print(peptide[:expected_peptide_length])