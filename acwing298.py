import collections


<<<<<<< HEAD
Carpenter = collections.namedtuple("Carpenter", ["l", "p", "s"])

=======
>>>>>>> 围栏问题
N, M = list(map(int, input().split()))
q = collections.deque()
dp = [[0 for _ in range(N + 1)] for _ in range(M + 1)]
car = []
<<<<<<< HEAD
for _ in range(M):
    l, p, s = list(map(int, input().split()))
    car.append(Carpenter(l, p, s))

car = sorted(car, key=lambda c: c.s)

for i in range(1, M + 1):
    for j in range(0, N + 1):
        dp[i][j] = max(dp[i - 1][j], -1 if j == 0 else dp[i][j - 1])
        l = car[i - 1].l
        p = car[i - 1].p
        s = car[i - 1].s
        if q and q[0] < j - l:
            q.popleft()
        if q and j >= s:
            k = q[0]
            dp[i][j] = max(dp[i][j], dp[i - 1][k] + (j - k) * p)

=======

for _ in range(M):
    l, p, s = list(map(int, input().split()))
    car.append({"l": l, "p": p, "s": s})

car = sorted(car, key=lambda c: c["s"])

# dp[i][j] 表示...
# dp[i-1][j]
# dp[i][j-1]
for i in range(1, M + 1):
    for j in range(0, N + 1):
        dp[i][j] = max(dp[i - 1][j], -1 if j == 0 else dp[i][j - 1])
        l = car[i - 1]["l"]
        p = car[i - 1]["p"]
        s = car[i - 1]["s"]
        if q and q[0] < j - l:
            q.popleft()
>>>>>>> 围栏问题
        if j < s:
            while q and dp[i - 1][q[-1]] - q[-1] * p <= dp[i - 1][j] - j * p:
                q.pop()
            q.append(j)
<<<<<<< HEAD
=======
        if q and j >= s:
            k = q[0]
            dp[i][j] = max(dp[i][j], dp[i - 1][k] + (j - k) * p)
>>>>>>> 围栏问题


print(dp[M][N])
