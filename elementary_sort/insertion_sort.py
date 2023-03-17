# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_1_A

# for i = 1 to A.length-1
#     key = A[i]
#     /* insert A[i] into the sorted sequence A[0,...,j-1] */
#     j = i - 1
#     while j >= 0 and A[j] > key
#         A[j+1] = A[j]
#         j--
#     A[j+1] = key

# 2 <= n <= 200000
N = int(input())

A = input().split()
print(' '.join(A))

A = [int(i) for i in A]

for i in range(1, len(A)):
    key = A[i]
    # insert A[i] into the sorted sequence A[0,...,j-1]
    j = i-1
    while j >= 0 and A[j] > key:
        A[j+1] = A[j]
        j = j-1
    A[j+1] = key

    print(' '.join([str(i) for i in A]))
