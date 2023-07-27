import copy
# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_6_C

# Quicksort(A, p, r)
# 1 if p < r
# 2    then q = Partition(A, p, r)
# 3        run Quicksort(A, p, q-1)
# 4        run Quicksort(A, q+1, r)


def partition(A, p, r):

    x = A[r][1]
    # A[i]: right end of "small" group
    i = p-1
    for j in range(p, r):
        # A[j]: target element
        if A[j][1] <= x:
            i = i+1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1


def quick_sort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quick_sort(A, p, q-1)
        quick_sort(A, q+1, r)


if __name__ == '__main__':

    n = int(input())
    A = []

    for _ in range(n):
        card = input().split()
        card[1] = int(card[1])
        A.append(tuple(card))

    B = copy.copy(A)

    quick_sort(A, 0, n-1)
    B.sort(key=lambda x: x[1])

    print('Stable') if A == B else print('Not stable')

    for a in A:
        print('{} {}'.format(a[0], a[1]))
