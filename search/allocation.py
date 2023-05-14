# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_4_D

n = 0
k = 0
W = []


def binsearch(l, r, pred):  # [l, r)
    assert l < r
    l -= 1
    while r - l > 1:
        m = (l + r) // 2
        if pred(m):
            r = m
        else:
            l = m
    return r


def check(P):
    i = 0
    for _ in range(k):
        s = 0
        while (s + W[i] <= P):
            s += W[i]
            i += 1
            if i == n:
                return True
    return False


if __name__ == "__main__":
    # number of packages, number of tracks
    n, k = map(int, input().split())

    # weights
    for _ in range(n):
        W.append(int(input()))

    RIGHT_MAX = 10**9 + 1

    r = binsearch(1, RIGHT_MAX, check)

    print(r)
