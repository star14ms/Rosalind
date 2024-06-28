from util import get_data, get_output_path
from _42_BA4G import LeaderboardCyclopeptideSequencing
from _41_BA4F import score_cyclic


def convolution_of_spectrum(spectrum):
    convolution_elements = [spectrum[j] - spectrum[i] \
        for i in range(len(spectrum)-1) \
            for j in range(i+1, len(spectrum)) if spectrum[j] - spectrum[i] > 0]

    return sorted(sorted(convolution_elements), key=convolution_elements.count, reverse=True)


if __name__ == "__main__":
    # data = get_data(__file__)
    data ='''20
60
57 57 71 99 129 137 170 186 194 208 228 265 285 299 307 323 356 364 394 422 493'''
#     data = '''20
# 373
# 853 113 585 796 924 502 423 1210 342 186 761 391 593 1412 1152 1396 260 129 1381 229 242 356 990 1047 57 748 1176 730 990 1038 1119 294 339 114 696 1251 1267 617 567 357 471 163 1266 1281 0 536 1395 454 1104 1362 1039 892 1509 1086 129 649 1095 713 258 777 1394 753 299 599 648 876 414 1249 813 242 859 1305 552 1284 861 650 1249 261 520 470 519 957 1233 405 260 861 762 810 1248 891 916 1346 390 981 147 1323 390 732 618 1380 1038 756 989 225 633 910 204 1452 243 1119 860 1395 129 57 503 1267 1153 276 462 228 1215 114 1170 357 973 388 519 699 131 128 1120 648 1452 1055 632 333 1380 528 747 389 656 97 1167 779 1380 1280 942 115 1121 1152 1007 990 1006 1118 519 877 1378 471'''

    M, N, spectrum = data.split("\n", 2)
    M, N = int(M), int(N)
    spectrum = list(map(int, spectrum.split()))

    elements = convolution_of_spectrum(spectrum)
    elements = [e for e in elements if e >= 57 and e <= 200]

    top_M_elements = set()
    while len(top_M_elements) < M:
        top_M_elements.add(elements.pop(0))

    leader_peptide = LeaderboardCyclopeptideSequencing(spectrum, N, masses=top_M_elements, verbose=True)
    print("-".join(map(str, leader_peptide)))
    
    # print(score_cyclic(leader_peptide, spectrum))
    # print(score_cyclic([99, 71, 137, 57, 72, 57], spectrum))

    # with open(get_output_path(__file__), "w") as f:
    #     print(*elements)
    #     print(*elements, file=f)
