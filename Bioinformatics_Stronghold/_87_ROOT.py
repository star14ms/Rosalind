from util import get_data, get_output_path


def possible_rooted_binary_trees(n_taxa):
    if n_taxa == 2:
        return 1

    # number of edges of a rooted binary tree with n_taxa taxa is 2n-2
    # number of possible way to add one more taxa (2n-2)+1
    # number of possible rooted binary trees ({2(n-1)-2}+1)!! = (2n-3)!!
    return possible_rooted_binary_trees(n_taxa-1) * ((2 * (n_taxa-1) - 2) + 1)


if __name__ == '__main__':
    data = get_data(__file__)
    # data = '4'

    n_taxa = int(data)
    n_possible_binary_trees = possible_rooted_binary_trees(n_taxa)
    print(n_possible_binary_trees % 1_000_000)
