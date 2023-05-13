# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_4_B

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


if __name__ == "__main__":
    n = int(input())
    S = list(map(int, input().split()))

    q = int(input())
    T = list(map(int, input().split()))

    result = 0
    RIGHT_MAX = 10**9 + 1

    for t in T:
        r = binsearch(0, RIGHT_MAX, lambda x: x >= t)
        if r in S:
            result += 1

    print(result)
