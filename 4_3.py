N, V = map(int, input().split())

dp = [0 for _ in range(V + 1)]


for i in range(N):
    v, w, amount = list(map(int, input().split()))
    dp_prev = dp[:]
    for j in range(v):
        q = []
        for k in range(j, V + 1, v):
            if q and q[0] < k - amount * v:
                del q[0]
            if q:
                dp[k] = max(dp[k], dp_prev[q[0]] + int((k - q[0]) / (v * w)))
            while q and dp_prev[q[-1]] - int((q[-1] - j) / (v * w)) <= dp_prev[k] - int(
                (k - j) / (v * w)
            ):
                del q[-1]
            q.append(k)

print(dp[-1])
