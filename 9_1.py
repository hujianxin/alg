class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)
        dp = [0 for _ in range(m + 1)]
        dp_prev = [0 for _ in range(m + 1)]

        for i in range(1, n + 1):
            dp_prev = dp[:]
            for j in range(1, m + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[j] = dp_prev[j - 1] + 1
                else:
                    dp[j] = max(dp_prev[j], dp[j - 1])

        return dp[-1]


print(Solution().longestCommonSubsequence(text1="abcde", text2="ace"))
print(Solution().longestCommonSubsequence(text1="abc", text2="abc"))
print(Solution().longestCommonSubsequence(text1="abc", text2="def"))
print(Solution().longestCommonSubsequence("ezupkr", "ubmrapg"))
