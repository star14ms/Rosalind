### https://github.com/danhalligan/rosalind.info/blob/main/rosalind/bioinformatics_textbook_track/ba4i.py
from util import get_data, get_output_path
from collections import defaultdict, Counter


def substrings(text, size):
    for i in range(len(text) - size + 1):
        yield text[i : i + size]


def score(theoretical, expected):
    spec, score = theoretical[:], 0
    if spec:
        for m in expected:
            if m in spec:
                score += 1
                spec.remove(m)
    return score


def cyclo_spectrum(peptide):
    spec = [0, sum(peptide)]
    for i in range(1, len(peptide)):
        for j in range(len(peptide)):
            spec += [sum((peptide[j:] + peptide[:j])[0:i])]
    return sorted(spec)


def expand(peptides, masses):
    return [p + [x] for x in masses for p in list(peptides)]


def linear_spectrum(peptide):
    spec = [0]
    for i in range(1, len(peptide) + 1):
        for x in substrings(peptide, i):
            spec.append(sum(x))
    return spec


def linear_score(peptide, spectrum):
    return score(linear_spectrum(peptide), spectrum)


def cyclo_score(peptide, spectrum):
    return score(cyclo_spectrum(peptide), spectrum)


def cut(peptides, spectrum, n):
    if len(peptides) < n:
        return peptides
    sc = [linear_score(p, spectrum) for p in peptides]
    lim = sorted(sc, reverse=True)[n - 1]
    return [p for p, sc in zip(peptides, sc) if sc >= lim]


def leaderboard_cyclopeptide_sequencing(spec, n, masses):
    lb = [[]]
    leader = []
    while len(lb):
        lb = expand(lb, masses)
        for pep in lb.copy():
            if sum(pep) == spec[-1]:
                if cyclo_score(pep, spec) > cyclo_score(leader, spec):
                    leader = pep
            elif sum(pep) > spec[-1]:
                lb.remove(pep)
        lb = cut(lb, spec, n)
    return leader


def spectrum_convolution(spec):
    dict = defaultdict(int)
    for i in range(len(spec)):
        for j in range(i + 1, len(spec)):
            m = abs(spec[i] - spec[j])
            if m > 0:
                dict[abs(spec[i] - spec[j])] += 1
    return Counter(dict).most_common()


def convolution_cyclopeptide_sequencing(m, n, spectrum):
    conv = spectrum_convolution(spectrum)
    conv = [(k, v) for k, v in conv if 57 <= k <= 200]
    masses = [k for k, v in conv if v >= conv[m - 1][1]]
    return leaderboard_cyclopeptide_sequencing(spectrum, n, masses)


if __name__ == "__main__":
    data = get_data(__file__)
#     data ='''20
# 60
# 57 57 71 99 129 137 170 186 194 208 228 265 285 299 307 323 356 364 394 422 493'''
#     data = '''20
# 373
# 853 113 585 796 924 502 423 1210 342 186 761 391 593 1412 1152 1396 260 129 1381 229 242 356 990 1047 57 748 1176 730 990 1038 1119 294 339 114 696 1251 1267 617 567 357 471 163 1266 1281 0 536 1395 454 1104 1362 1039 892 1509 1086 129 649 1095 713 258 777 1394 753 299 599 648 876 414 1249 813 242 859 1305 552 1284 861 650 1249 261 520 470 519 957 1233 405 260 861 762 810 1248 891 916 1346 390 981 147 1323 390 732 618 1380 1038 756 989 225 633 910 204 1452 243 1119 860 1395 129 57 503 1267 1153 276 462 228 1215 114 1170 357 973 388 519 699 131 128 1120 648 1452 1055 632 333 1380 528 747 389 656 97 1167 779 1380 1280 942 115 1121 1152 1007 990 1006 1118 519 877 1378 471'''

    M, N, spectrum = data.split("\n", 2)
    M, N = int(M), int(N)
    spectrum = list(map(int, spectrum.split()))

    elements = convolution_cyclopeptide_sequencing(M, N, spectrum)

    with open(get_output_path(__file__), "w") as f:
        print(*elements, sep='-')
        print(*elements, sep='-', file=f)
