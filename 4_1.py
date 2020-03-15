N, V = list(map(int, input().split()))

dp = [0 for _ in range(V + 1)]

for i in range(N):
    v, w, amount = list(map(int, input().split()))
    for j in range(V, v - 1, -1):
        k = 1
        while k * v <= j and k <= amount:
            dp[j] = max(dp[j], dp[j - k * v] + k * w)
            k += 1


print(dp[-1])
