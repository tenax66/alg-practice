# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_5_D

# bubbleSort(A)
#   cnt = 0 // 反転数
#   for i = 0 to A.length-1
#     for j = A.length-1 downto i+1
#       if A[j] < A[j-1]
# 	swap(A[j], A[j-1])
# 	cnt++

#   return cnt
import math


def merge(A, left, mid, right):
    cnt = 0
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
        if L[i] <= R[j]:
            A[k] = L[i]
            i = i + 1
        else:
            A[k] = R[j]
            j = j + 1
            cnt += (n1 - i)
    return cnt


def merge_sort(A, left, right):
    if left + 1 < right:
        mid = (left + right)//2
        v1 = merge_sort(A, left, mid)
        v2 = merge_sort(A, mid, right)

        v3 = merge(A, left, mid, right)
        return v1 + v2 + v3
    else:
        return 0


if __name__ == "__main__":
    N = int(input())
    A = list(map(int, input().split()))

    print(merge_sort(A, 0, len(A)))
