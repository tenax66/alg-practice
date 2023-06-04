# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_5_B

# merge(A, left, mid, right)
#   n1 = mid - left;
#   n2 = right - mid;
#   L[0...n1], R[0...n2] を生成
#   for i = 0 to n1-1
#     L[i] = A[left + i]
#   for i = 0 to n2-1
#     R[i] = A[mid + i]
#   L[n1] = INFTY
#   R[n2] = INFTY
#   i = 0
#   j = 0
#   for k = left to right-1
#     if L[i] <= R[j]
#       A[k] = L[i]
#       i = i + 1
#     else
#       A[k] = R[j]
#       j = j + 1

# mergeSort(A, left, right)
#   if left+1 < right
#     mid = (left + right)/2;
#     mergeSort(A, left, mid)
#     mergeSort(A, mid, right)
#     merge(A, left, mid, right)

import math

cnt = 0

def merge(A, left, mid, right):
    global cnt
    n1 = mid - left
    n2 = right - mid

    L = []
    R = []

    for i in range(n1):
        L.append(A[left + i])

    for i in range(n2):
        R.append(A[mid + i])

    L.append(math.inf)
    R.append(math.inf)

    i = 0
    j = 0

    for k in range(left, right):
        cnt += 1
        if L[i] <= R[j]:
            A[k] = L[i]
            i = i + 1
        else:
            A[k] = R[j]
            j = j + 1


def merge_sort(A, left, right):
    if left + 1 < right:
        mid = (left + right)//2
        merge_sort(A, left, mid)
        merge_sort(A, mid, right)

        merge(A, left, mid, right)

if __name__ == '__main__':
    N = int(input())
    S = list(map(int, input().split()))

    merge_sort(S, 0, len(S))
    print(' '.join(map(str, S)))
    print(cnt)
