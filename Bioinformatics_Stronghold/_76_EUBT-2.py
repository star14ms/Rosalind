from util import get_data, get_output_path


data = get_data(__file__)
data = 'A B C D E F G'

leaves = data.split()
n = 1
n2 = 1

def build_all_possible_binary_trees(leaves: list, tree: str):
    global n, n2
    index_next_specie = tree.count(',') + 1
    trees = []

    for i in range(index_next_specie):
        new_tree = tree.replace(leaves[i], f'({leaves[i]},{leaves[index_next_specie]})')
        new_trees = [new_tree] if i != 0 else []
        
        # if f'({leaves[i]},' in tree and i != 0:
        #     new_tree2 = tree.replace(f'({leaves[i]},', f'({leaves[index_next_specie]},({leaves[i]},')
        #     index = new_tree2.find(')', new_tree2.index(leaves[i]))
        #     new_tree2 = new_tree2[:index] + f')' + new_tree2[index:]
        #     new_trees.append(new_tree2)
        # if f',{leaves[i]})' in tree and i != 0:
        #     new_tree2 = tree.replace(f',{leaves[i]})', f',{leaves[i]}),{leaves[index_next_specie]})')
        #     index = len(new_tree2) - new_tree2[::-1].find('(', new_tree2.index(leaves[i])) - 1
        #     new_tree2 = new_tree2[:index] + f'(' + new_tree2[index:]
        #     new_trees.append(new_tree2)
        if f'{leaves[i]},(' in tree:
            new_tree2 = tree.replace(f'{leaves[i]},(', f'{leaves[i]},({leaves[index_next_specie]},(')
            index = new_tree2.find(')', new_tree2.index(leaves[i]))
            new_tree2 = new_tree2[:index] + f')' + new_tree2[index:]
            new_trees.append(new_tree2)
        if f'),{leaves[i]}' in tree:
            new_tree2 = tree.replace(f'),{leaves[i]}', f'),{leaves[index_next_specie]}),{leaves[i]}')
            index = len(new_tree2) - new_tree2[::-1].find('(', new_tree2.index(leaves[i])) - 1
            new_tree2 = new_tree2[:index] + f'(' + new_tree2[index:]
            new_trees.append(new_tree2)
        if f'),({leaves[i]}' in tree:
            new_tree2 = tree.replace(f'),({leaves[i]}', f'),({leaves[index_next_specie]},({leaves[i]}')
            index = new_tree2.find(')', new_tree2.index(leaves[i]))
            new_tree2 = new_tree2[:index] + f')' + new_tree2[index:]
            new_trees.append(new_tree2)
        if f'{leaves[i]}),(' in tree:
            new_tree2 = tree.replace(f'{leaves[i]}),(', f'{leaves[i]}),{leaves[index_next_specie]}),(')
            index = len(new_tree2) - new_tree2[::-1].find('(', new_tree2.index(leaves[i])) - 1
            new_tree2 = new_tree2[:index] + f'(' + new_tree2[index:]
            new_trees.append(new_tree2)

        for new_tree in new_trees:
            if len(leaves) == index_next_specie + 1:
                trees.append(new_tree)
                # print(new_tree)
                n2 += 1
                continue

            if index_next_specie == 5:
                print(n, n2-1)
                n += 1
                n2 = 1

            trees_extended = build_all_possible_binary_trees(leaves, new_tree)
            trees.extend(trees_extended)

    return trees


trees = build_all_possible_binary_trees(leaves, tree=f'(({leaves[1]},{leaves[2]}),{leaves[0]});')
# print(*trees, sep='\n')
print(len(trees))

with open(get_output_path(__file__), 'w') as output_data:
  output_data.write('\n'.join(trees) + '\n')
