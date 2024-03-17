def count_noncrossing_rna_matchings(s):
    n = len(s)
    dp = [[0 for _ in range(n)] for _ in range(n)]
    
    # A utility function to check if two nucleotides can form a pair
    def can_pair(a, b):
        return (a == 'A' and b == 'U') or (a == 'U' and b == 'A') or \
               (a == 'C' and b == 'G') or (a == 'G' and b == 'C')
    
    # Initialize base cases for dynamic programming
    for i in range(n):
        dp[i][i] = 1  # No pairs, but we count it as one way to arrange it
    
    # Fill in the DP table
    for length in range(2, n+1, 2):  # Only even lengths can form perfect matchings
        for i in range(n-length+1):
            j = i + length - 1
            for k in range(i, j, 2):  # Iterate through possible pairings
                if can_pair(s[i], s[k+1]):  # Check if a valid pair can be formed
                    # Multiply ways to arrange the inside and outside of the pair
                    dp[i][j] += dp[i+1][k] * dp[k+2][j] if k + 2 <= j else dp[i+1][k]
                    dp[i][j] %= 1_000_000  # Modulo as per the problem statement
    
    return dp[0][n-1] if n > 0 else 1

# Example usage
rna_string = "AUAU"
print(count_noncrossing_rna_matchings(rna_string))
