N, V, M = list(map(int, input().split()))

dp = [[0 for _ in range(M + 1)] for _ in range(V + 1)]

for _ in range(N):
    v, m, w = list(map(int, input().split()))
    for i in range(V, v - 1, -1):
        for j in range(M, m - 1, -1):
            dp[i][j] = max(dp[i][j], dp[i - v][j - m] + w)

print(dp[-1][-1])
