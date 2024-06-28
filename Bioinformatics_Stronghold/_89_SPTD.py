### hard
from util import get_data
from Bio import Phylo
from io import StringIO


def get_nontrivial_splits(tree, tree_basic=None):
    splits = []
    if tree.name:
        return []
    if not tree_basic:
        tree_basic = tree

    if getattr(tree, 'clades', None):
        split1 = set([clade.name for clade in tree.clades[0].get_terminals()])
        split2 = set([clade.name for clade in tree.clades[1].get_terminals()])

        # if len(split1) >= 2 and len(split2) >= 2:
        #     splits.append([split1, split2])

        if len(split1) >= 2:
            splits.append([split1, set([clade.name for clade in tree_basic.get_terminals()]) - split1])
        if len(split2) >= 2:
            splits.append([split2, set([clade.name for clade in tree_basic.get_terminals()]) - split2])

        if len(split1) >= 3:
            splits.extend(get_nontrivial_splits(tree.clades[0], tree_basic))
        if len(split2) >= 3:
            splits.extend(get_nontrivial_splits(tree.clades[1], tree_basic))

    elif getattr(tree, 'clade', None):
        split1 = set([clade.name for clade in tree.clade[0].get_terminals()])
        split2 = set([clade.name for clade in tree.clade[1].get_terminals()])
        split3 = set([clade.name for clade in tree.clade[2].get_terminals()])

        for split in [split1, split2, split3]:
            if len(split) >= 2:
                splits.append([split, set([clade.name for clade in tree_basic.get_terminals()]) - split])

        for i, split in enumerate([split1, split2, split3]):
            if len(split) >= 3:
                splits.extend(get_nontrivial_splits(tree.clade[i], tree_basic))

    return splits


if __name__ == '__main__':
    data = get_data(__file__)
#     data = '''dog rat elephant mouse cat rabbit
# (rat,(dog,cat),(rabbit,(elephant,mouse)));
# (rat,(cat,dog),(elephant,(mouse,rabbit)));'''

    data = data.split('\n')
    newick1 = data[1]
    newick2 = data[2]

    # print(newick1)
    # print(newick2)

    tree1 = Phylo.read(StringIO(newick1), "newick")
    tree2 = Phylo.read(StringIO(newick2), "newick")

    nontrivial_splits1 = get_nontrivial_splits(tree1)
    nontrivial_splits2 = get_nontrivial_splits(tree2)

    n_sharing = 0
    for nontrivial_split1 in nontrivial_splits1:
        for nontrivial_split2 in nontrivial_splits2:
            if nontrivial_split1 == nontrivial_split2 or nontrivial_split1 == nontrivial_split2[::-1]:
                n_sharing += 1

    print(len(nontrivial_splits1), len(nontrivial_splits2), n_sharing)
    split_distance = (len(tree1.get_terminals()) - 3) + (len(tree2.get_terminals()) - 3) - 2 * n_sharing
    print(split_distance)
    breakpoint()

    # check duplicated splits
    # for i, nontrivial_split1 in enumerate(nontrivial_splits1):
    #     for j, nontrivial_split2 in enumerate(nontrivial_splits1):
    #         if i != j and nontrivial_split1 == nontrivial_split2 or nontrivial_split1 == nontrivial_split2[::-1]:
    #             print(nontrivial_split1, nontrivial_split2)
