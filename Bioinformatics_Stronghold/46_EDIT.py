from util import get_data

data = get_data(__file__)
# data = '''>Rosalind_39
# PLEASANTLY
# >Rosalind_11
# MEANLY'''

data = data.split('>')[1:]
s1, s2 = [x.split('\n', 1)[1].replace('\n', '') for x in data]


def edit_distance(s1, s2):
    m, n = len(s1), len(s2)
    # Initialize the DP table
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Base case: transforming into an empty string or from an empty string
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]  # No operation needed
            else:
                dp[i][j] = 1 + min(
                    dp[i - 1][j],      # Deletion
                    dp[i][j - 1],      # Insertion
                    dp[i - 1][j - 1]   # Substitution
                )

    return dp[m][n]


print(edit_distance(s1, s2))
