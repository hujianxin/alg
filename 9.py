class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if not text1 or not text2:
            return 0

        n, m = len(text1), len(text2)
        # dp[i][j]表示text1的前i哥字符与text2前j个字符最长公共子序列的长度
        # dp[i][j] =
        dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[-1][-1]


print(Solution().longestCommonSubsequence(text1="abcde", text2="ace"))
print(Solution().longestCommonSubsequence(text1="abc", text2="abc"))
print(Solution().longestCommonSubsequence(text1="abc", text2="def"))
