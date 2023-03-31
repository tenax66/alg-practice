# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_2_D

# insertionSort(A, n, g)
#     for i = g to n-1
#         v = A[i]
#         j = i - g
#         while j >= 0 && A[j] > v
#             A[j+g] = A[j]
#             j = j - g
#             cnt++
#         A[j+g] = v
#
# shellSort(A, n)
#     cnt = 0
#     m = ?
#     G[] = {?, ?,..., ?}
#     for i = 0 to m-1
#         insertionSort(A, n, G[i])

import math


def insertSort(A, n, g) -> int:
    cnt = 0
    for i in range(g, n):
        v = A[i]
        j = i-g
        while j >= 0 and A[j] > v:
            A[j+g] = A[j]
            j = j-g
            cnt += 1
        A[j+g] = v
    return cnt


def shellSort(A, n) -> int:

    cnt = 0
    for g in G:
        cnt += insertSort(A, n, g)

    return cnt


if __name__ == '__main__':
    n = int(input())

    A = []
    for i in range(n):
        A.append(int(input()))

    # https://ja.wikipedia.org/wiki/%E3%82%B7%E3%82%A7%E3%83%AB%E3%82%BD%E3%83%BC%E3%83%88
    # knuth's sequence
    # (3^k - 1)/2 for 1 <= k <= ceil(n/3)
    G = []
    for i in range(1, math.ceil(n/3)+1):
        value = int((3**i - 1)/2)
        if value <= n:
            G.append(value)
        else:
            break

    G.reverse()
    m = len(G)

    print(m)
    print(' '.join([str(i) for i in G]))

    cnt = shellSort(A, n)

    print(cnt)

    for a in A:
        print(a)
