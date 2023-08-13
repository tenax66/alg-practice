# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_6_A

# Counting-Sort(A, B, k)
#     for i = 0 to k
#         do C[i] = 0
#     for j = 1 to length[A]
#         do C[A[j]] = C[A[j]]+1
#     /* C[i] now contains the number of elements equal to i */
#     for i = 1 to k
#     do C[i] = C[i] + C[i-1]
#     /* C[i] now contains the number of elements less than or equal to i */
#     for j = length[A] downto 1
#         do B[C[A[j]]] = A[j]
#             C[A[j]] = C[A[j]]-1

def counting_sort(A, B, k):
    C = [0 for _ in range(k)]

    for a in A:
        C[a] = C[a] + 1
    for i in range(k):
        C[i] = C[i] + C[i-1]
    for j in reversed(range(len(A))):
        B[C[A[j]]-1] = A[j]
        C[A[j]] = C[A[j]] - 1


if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    B = [0 for _ in range(len(A))]
    k = 10001
    counting_sort(A, B, k)
    print(' '.join(map(str, B)))
