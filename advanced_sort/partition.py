# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_6_B

# Partition(A, p, r)
# x = A[r]
# i = p-1
# for j = p to r-1
#     do if A[j] <= x
#        then i = i+1
#            exchange A[i] and A[j]
# exchange A[i+1] and A[r]
# return i+1

def partition(A, p, r):
    x = A[r]
    # A[i]: right end of "small" group
    i = p-1
    for j in range(p, r):
        # A[j]: target element
        if A[j] <= x:
            i = i+1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1


if __name__ == '__main__':
    n = int(input())
    A = list(map(int, input().split()))

    index = partition(A, 0, n-1)

    A_str = list(map(str, A))
    A_str[index] = '[' + A_str[index] + ']'
    print(' '.join(A_str))
