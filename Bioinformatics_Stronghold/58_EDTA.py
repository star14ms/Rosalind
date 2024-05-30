from util import get_data, get_output_path

data = get_data(__file__)
# data = '''>Rosalind_43
# PRETTY
# >Rosalind_97
# PRTTEIN'''

data = data.split('>')[1:]
s1, s2 = [x.split('\n', 1)[1].replace('\n', '') for x in data]


def get_augmented_str(s1_idx, s2_idx):
  if (s1_idx, s2_idx) in get_augmented_str.cache:
    return get_augmented_str.cache[(s1_idx, s2_idx)]
  
  if s1_idx == len(s1):
    return '-' * len(s2[s2_idx:]), s2[s2_idx:]
  
  if s2_idx == len(s2):
    return s1[s1_idx:], '-' * len(s1[s1_idx:])
  
  # If the current bases are the sames
  if s1[s1_idx] == s2[s2_idx]:
    suffix = get_augmented_str(s1_idx+1, s2_idx+1)
    augmented_str = [s1[s1_idx] + suffix[0],
                     s2[s2_idx] + suffix[1]]
    get_augmented_str.cache[(s1_idx, s2_idx)] = augmented_str
    return augmented_str

  augmented_strs = []

  # Assumming substitution
  suffix = get_augmented_str(s1_idx+1, s2_idx+1)
  augmented_strs.append((s1[s1_idx] + suffix[0], \
                         s2[s2_idx] + suffix[1]))
  # Assumming deletion
  suffix = get_augmented_str(s1_idx+1, s2_idx)
  augmented_strs.append((s1[s1_idx] + suffix[0], \
                         '-' + suffix[1]))
  # Assumming insertion
  suffix = get_augmented_str(s1_idx, s2_idx+1)
  augmented_strs.append(('-' + suffix[0], \
                         s2[s2_idx] + suffix[1]))

  # get the augmented string with the minimum edit distance
  max_n_matching = -1
  min_edit_distance = float('inf')
  optimal_alignment = None

  for str1, str2 in augmented_strs:
    n_matching = sum([1 for i in range(len(str1)) if str1[i] == str2[i]])
    edit_distance = sum([1 for i in range(len(str1)) if str1[i] != str2[i]])

    if edit_distance < min_edit_distance or \
       (edit_distance == min_edit_distance and n_matching > max_n_matching):
      min_edit_distance = edit_distance
      max_n_matching = n_matching
      optimal_alignment = str1, str2

  get_augmented_str.cache[(s1_idx, s2_idx)] = optimal_alignment
  return optimal_alignment


get_augmented_str.cache = {}
augmented_str1, augmented_str2 = get_augmented_str(0, 0)

edit_distance = sum([1 for i in range(len(augmented_str1)) if augmented_str1[i] != augmented_str2[i]])
print(edit_distance)
print(augmented_str1)
print(augmented_str2)

with open(get_output_path(__file__), 'w') as f:
  f.write(str(edit_distance) + '\n')
  f.write(augmented_str1 + '\n')
  f.write(augmented_str2 + '\n')


def color_alignment(str1, str2):
  str1 = 'AMGRTSLAIRGGSQRQFDSHPHWEAPECSGHSVWW----KNVNGQGFSSERIS--TSYY-----SWPYGEKIVWCMLHCFHDNFWAQLMDFHQWHGQNHYANEPPKECSSSSVCCCYLAAVMKVHQNI------ELVRFGWWQMYPDAHSAFLW------MPCWH--T---SI--QNFIDRKVVGYGTVEQDTLHPHKEHRCCRSLFDSTKYMVFFEIIMPKDNDCIDSLI--WTTFGGAVTPDVNSELAYVTNMS--TGVMRCCMCEQV---------LS---LWQTSSEMGRVGNVAHSAPLDSAHYNGDCHNQWFGWFKEGCMKPHEPDEWVIFQ--LTCP-TGWISKAPVCDSV--------TNGTKIDYSPGIYVIDQFTVLSPAKSRIDKWLFEDVDVWKGINKYHEQCWDRKFAVWHHHGGNHFKI-----LTCFMTEQKSTPFDKNKILHMAQDYCVQIKYDLL-E-TPMKEQAFSSDNAL--TQ---HVAVEEVTCWRWNFICFLGGY---NKDFRATKGRSWKNQPNCKARQWC-DSKNLPFTCR------SVNGD------GHKFMNCQHMLYEYCWWI---EYEEASVIFFHERRYNWDHVEC---MEHAYIPLFNLCDTFVCDRSYWTGNI------LRYKGAVKVKDNMHCYRHPT----F----YDGHCTKLEILYNMRS--PNHCWNVDYRYVHCWTE-WDRNKFEHHHMEIDDHHTWSPPALLEDQDHCVMRVIAGEPYTFMQQHHGYDITG-YGTV---EYGPLHWHKWTKANCSAPNLSITMESCKFTTMEPVVMNMNTIANIAFKIDSLP-MVLEDAAHCKNMVLADKGYTDLFCKTHVWYVKYMCTSYMPSKGGQQQWMHDFPGIRVRNDYAVSLYIRWVYQKIEYCFERACDRRSYIRTYKYTWPIMYASSICMHF----SRYGHH'
  str2 = 'MMGRVVLA---------DSHPHMEA-----HSVWAMACFKWFNGQGCSSNRNRKRT-YLCAKRPSWPRGTKIV--------DNFWAQLMDFHQWH----YRNESPKER---------LAAVMKVHQNLLNLMKKELVRFG---MYPDAASAGLVHVYCIHMPDWHDWTQCMSHAPQTFLDMKPHFK----QD-LHFHKEH----------------EI----DNDCIDSLWKSW---G-AVIPDVNSELARVW-MSPSTGQMRCCMCEQVDQAWWIHVVLLWPQLWQTSSED----N-A---PLDSAH----C---WFGWFKEGCMKPHEPDEWVIFPGWLTIWRTGWISKA---DSWEEHCQMWLTNGTKIDYSPGIYVIDQF----------D-----DVDVWKRINKYHEQC---KFAVWHQSWGNHFKSKGYVFLTCFMTEQKSTPFD-NKILMMAQDYCVQIKYDLSIEETPMKEQATSS--AYCHTCFIGHVAVEEVTCWRWNFICFLGGTHQMNKDFRAS-GRSWPNRPRCKALQWTADSKNLPFTHHVTPGFFSVN-DPYARLYGHKFMNCQRMLYEYCWVIQKIEWEEASLINFTERRYNWDHVEKLHTMEHAYIPLF----TFVV-RLNWTGGGVEYTSKLRYKPAV------HCYRHPTKCVVFPDQFYD--CTKLEILYSMMTGTP-HIWS---RYNHCWTVQWDRNKFEHHHMEIDDHHTWSPPALL------VGRVIAGEP------H-GTRISCVYG-VGHPEYGPLHWHKWTKANGSAP-----MESR-FTTMEPV------IA---FKIDSTDFMGLE---------LADKGYTDLFCKTHVWDV-----------G-QQQ--------RV------SLYLRWV---------------SYIWTYRYTWPKMYASSDCMHHEEDKSTYGHH'
  colored_str1 = ''
  colored_str2 = ''

  for i in range(len(str1)):
    if str1[i] != str2[i]:
      colored_str1 += str1[i]
      colored_str2 += str2[i]
    else:
      if str1[i] == '-':
        color = 'yellow'
      else:
        color = 'green'
      colored_str1 += f'[{color}]{str1[i]}[/{color}]'
      colored_str2 += f'[{color}]{str2[i]}[/{color}]'
      
  from rich import print as pprint
  pprint(colored_str1)
  pprint(colored_str2)
