# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_1_D

# 2 <= n <= 200000
N = int(input())

# 1 <= R_t <= 10^9
R = [int(input()) for _ in range(N)]

# 1 - 10^9
max = -999999999

min_price = R[0]
R = R[1:]

for i, r in enumerate(R):
    local_max = r - min_price

    if local_max > max:
        max = local_max

    if(min_price > r):
        min_price = r

print(max)
