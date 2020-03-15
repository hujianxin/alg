N, V = map(int, input().split())

dp = [0 for _ in range(V + 1)]


def complete_pack(v, w) -> None:
    for i in range(v, V + 1):
        dp[i] = max(dp[i], dp[i - v] + w)


def zero_one_pack(v, w) -> None:
    for i in range(V, v - 1, -1):
        dp[i] = max(dp[i], dp[i - v] + w)


def multiple_pack(v, w, amount) -> None:
    if v * amount >= V:
        complete_pack(v, w)
        return
    k = 1
    while k < amount:
        zero_one_pack(k * v, k * w)
        amount -= k
        k *= 2
    zero_one_pack(amount * v, amount * w)


for i in range(N):
    v, w, s = list(map(int, input().split()))
    if s == -1:
        zero_one_pack(v, w)
    elif s == 0:
        complete_pack(v, w)
    else:
        multiple_pack(v, w, s)

print(dp[-1])
