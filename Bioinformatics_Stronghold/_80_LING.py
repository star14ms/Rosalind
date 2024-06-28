from util import get_data


# dna_string = get_data(__file__)

# Example usage for a 100 kbp DNA string
dna_string = "ATTTGGATT"  # replace with your actual 100 kbp DNA string
alphabet_size = 4  # DNA has 4 bases: A, T, C, G


def build_suffix_array(s):
    suffixes = sorted((s[i:], i) for i in range(len(s)))
    suffix_arr = [suf[1] for suf in suffixes]
    return suffix_arr

def build_lcp_array(s, suffix_arr):
    n = len(s)
    rank = [0] * n
    lcp = [0] * n
    for i, suffix in enumerate(suffix_arr):
        rank[suffix] = i
    h = 0
    from rich import print as pprint
    print(rank)
    for i in range(n):
        if rank[i] > 0:
            j = suffix_arr[rank[i] - 1]
            while i + h < n and j + h < n and s[i + h] == s[j + h]:
                h += 1
            if i + h < n and j + h < n and h > 0 and s[i + h] == s[j + h]:
                pprint(s[:i] + '[green]' + s[i:i+h+1] + '[/green]' + s[i+h+1:])
                pprint(s[:j] + '[green]' + s[j:j+h+1] + '[/green]' + s[j+h+1:])
            else:
                pprint(s[:i] + '[green]' + s[i:i+h] + '[/green]' + s[i+h:])
                pprint(s[:j] + '[green]' + s[j:j+h] + '[/green]' + s[j+h:])
                
            lcp[rank[i]] = h
            print(lcp, h)
            if h > 0:
                h -= 1
    return lcp

def count_distinct_substrings(s):
    n = len(s)
    suffix_arr = build_suffix_array(s)
    lcp = build_lcp_array(s, suffix_arr)
    
    total_substrings = (n * (n + 1)) // 2
    lcp_sum = sum(lcp)
    print(total_substrings, lcp_sum)
    return total_substrings - lcp_sum

# def max_distinct_substrings(a, n):
#     if n <= a:
#         return (n * (n + 1)) // 2
#     return (a * (a + 1)) // 2 + a * (n - a)


def max_distinct_substrings(a, n):
    limit = 0
    for k in range(1, n+1):
        if a**k < n-k+1:
            limit += n-k+1 - a**k
        else:
            break

    if a <= n:
        return (n * (n + 1)) // 2 - limit
    else:
        return (n * (n + 1)) // 2


def linguistic_complexity(s, a):
    sub_s = count_distinct_substrings(s)
    m_a_n = max_distinct_substrings(a, len(s))
    print(sub_s, m_a_n)
    return sub_s / m_a_n

lc = linguistic_complexity(dna_string, alphabet_size)
print(f"Linguistic Complexity: {lc}")
