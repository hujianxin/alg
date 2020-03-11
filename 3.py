N, V = map(int, input().split())

# 
dp = [[0 for _ in range(V + 1)] for _ in range(N + 1)]

for i in range(1, N + 1):
    [v, w] = list(map(int, input().split()))
    for j in range(1, V + 1):
        dp[i][j] = dp[i - 1][j]
        if j >= v:
            dp[i][j] = max(dp[i][j], dp[i][j - v] + w)

print(dp[-1][-1])
