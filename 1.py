class Solution:
    def numDecodings(self, s: str) -> int:
        s = "0" + s
        n = len(s)
        dp = [0 for _ in range(n)]
        dp[0] = 1
        for i in range(1, n):
            if int(s[i]) > 0:
                dp[i] = dp[i-1]
            if i >= 2 and int(s[i-1:i+1]) >= 10 and int(s[i-1:i+1]) <= 26:
                dp[i] = dp[i] + dp[i-2]
        return dp[n-1]
