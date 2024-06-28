
def count_noncrossing_matchings(s):
    n = len(s)
    dp = [[0] * n for _ in range(n)]

    # Initialize base cases: empty pairs and single nucleotides
    for i in range(n):
        dp[i][i] = 1
    for i in range(n-1):
        dp[i][i+1] = 1 if s[i] == s[i+1] else 0

    # Fill dp table for substrings of length 2 and more
    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            # Check all possible splits
            for k in range(i, j, 2): # Ensure we only pair with valid opposite types
                if (s[i] == 'A' and s[k+1] == 'U') or (s[i] == 'U' and s[k+1] == 'A') or \
                   (s[i] == 'C' and s[k+1] == 'G') or (s[i] == 'G' and s[k+1] == 'C'):
                    # Safe to assume dp[i+1][k] and dp[k+2][j] are within bounds due to loop setup
                    dp[i][j] += dp[i+1][k] * dp[k+2][j]
                    dp[i][j] %= 1_000_000

    return dp[0][n-1]

# Example usage
rna_string = "AUAU"
print(count_noncrossing_matchings(rna_string))


