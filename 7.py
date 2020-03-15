N, V = list(map(int, input().split()))

dp = [0 for _ in range(V + 1)]

for _ in range(N):
    group = []
    for _ in range(int(input())):
        group.append(list(map(int, input().split())))

    for i in range(V, -1, -1):
        for [v, w] in group:
            if i >= v:
                dp[i] = max(dp[i], dp[i-v] + w)

print(dp[-1])
