N, V = map(int, input().split())


# dp[i] 表示总体积为i的情况下，最大化价值
# 与01背包的区别是，在压缩为1维的情况下，完全背包是从小到大遍历体积
dp = [0 for _ in range(V + 1)]

for i in range(N):
    v, w = list(map(int, input().split()))
    for j in range(v, V + 1):
        dp[j] = max(dp[j], dp[j - v] + w)


print(dp[V])
