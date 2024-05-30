from util import get_data, get_output_path


# tree = get_data(__file__)
tree = '''((((Aa,aa),(Aa,Aa)),((aa,aa),(aa,AA))),Aa);'''
x = 0

def contract_tree(tree, weight=1):
  global x
  x += 1
  index = None

  if len(tree) == 3:
    return tree.rstrip(';'), weight
  if (tree, weight) in contract_tree.cache:
    return contract_tree.cache[(tree, weight)]
  # else:
  #   while index is None or (tree[index+1] == '(' or tree[index-1] == ')'):
  #     index = tree.find(',', start)
  #     start = index + 1

  for allele1, allele2 in [ # sorted by priority for time complexity
    ('AA', 'AA'), ('aa', 'aa'), ('AA', 'aa'), ('aa', 'AA'), # 1st priority
    ('AA', 'Aa'), ('Aa', 'AA'), ('aa', 'Aa'), ('Aa', 'aa'), # 2nd priority
    ('Aa', 'Aa') # 3rd priority
  ]:
    if f'{allele1},{allele2}' in tree:
      index = tree.find(f'{allele1},{allele2}') + 2
      break

  # allele1 = tree[index-2:index]
  # allele2 = tree[index+1:index+3]

  # posibility of 3 alleles at a root node
  alleles_offspring = None
  if allele1 == 'AA' and allele2 == 'AA':
    alleles_offspring = [('AA', weight * 4)]
  elif allele1 == 'aa' and allele2 == 'aa':
    alleles_offspring = [('aa', weight * 4)]
  elif (allele1 == 'AA' and allele2 == 'aa') or (allele1 == 'aa' and allele2 == 'AA'):
    alleles_offspring = [('Aa', weight * 4)]
  elif (allele1 == 'AA' and allele2 == 'Aa') or (allele1 == 'Aa' and allele2 == 'AA'):
    alleles_offspring = [('AA', weight * 2), ('Aa', weight * 2)]
  elif (allele1 == 'aa' and allele2 == 'Aa') or (allele1 == 'Aa' and allele2 == 'aa'):
    alleles_offspring = [('aa', weight * 2), ('Aa', weight * 2)]
  elif allele1 == 'Aa' and allele2 == 'Aa':
    alleles_offspring = [('AA', weight * 1), ('Aa', weight * 2), ('aa', weight * 1)]
    
  alleles_root = []
  for allele_offspring, weight_new in alleles_offspring:
    tree_contracted = tree[:index-3] + allele_offspring + tree[index+4:]
    alleles_root.append((contract_tree(tree_contracted, weight_new)))

  contract_tree.cache[(tree, weight)] = alleles_root

  print(x, end='\r')
  return alleles_root


def get_mendelian_prob(alleles_root):
  for allele in alleles_root:
    if type(allele) is list:
      get_mendelian_prob(allele)
    else:
      if allele[0] == 'AA':
        get_mendelian_prob.cache['AA'] += allele[1]
      elif allele[0] == 'Aa':
        get_mendelian_prob.cache['Aa'] += allele[1]
      elif allele[0] == 'aa':
        get_mendelian_prob.cache['aa'] += allele[1]
        
  return get_mendelian_prob.cache


contract_tree.cache = {}
alleles_root = contract_tree(tree)

get_mendelian_prob.cache = {'AA': 0, 'Aa': 0, 'aa': 0}
mendelian_prob = get_mendelian_prob(alleles_root)

total = sum(mendelian_prob.values())
prob = {k: round(v/total, 3) for k, v in mendelian_prob.items()}

print(x)
print(len(contract_tree.cache))
print(*prob.values())
