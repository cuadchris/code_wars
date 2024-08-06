'''
https://www.codewars.com/kata/545cdb4f61778e52810003a2

Description:

In information theory and computer science, the Levenshtein distance is a string metric for measuring the
difference between two sequences. Informally, the Levenshtein distance between two words is the minimum
number of single-character edits (i.e. insertions, deletions or substitutions) required to change one
word into the other.

(http://en.wikipedia.org/wiki/Levenshtein_distance)

Your task is to implement a function which calculates the Levenshtein distance for two arbitrary strings.
'''

def levenshtein(a, b):

    n, m = len(a), len(b)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = i
    for j in range(m + 1):
        dp[0][j] = j

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j] + 1,
                               dp[i][j - 1] + 1,
                               dp[i - 1][j - 1] + 1)

    return dp[n][m]