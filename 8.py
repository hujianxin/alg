from typing import List


class Solution:
    def minPathSum(self, A: List[List[int]]) -> int:
        if not A:
            return 0
        n, m = len(A), len(A[0])

        dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if i == 1:
                    dp[i][j] = dp[i][j-1] + A[i-1][j-1]
                if j == 1:
                    dp[i][j] = dp[i-1][j] + A[i-1][j-1]
                if i != 1 and j != 1:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + A[i - 1][j - 1]

        return dp[n][m]


print(Solution().minPathSum([
  [1,3,1],
  [1,5,1],
  [4,2,1]
]))
