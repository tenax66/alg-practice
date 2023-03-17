# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_2_A

# BubbleSort(A)
# for i = 0 to A.length-1
#     for j = A.length-1 downto i+1
#         if A[j] < A[j-1]
#             swap A[j] and A[j-1]

N = int(input())

A = input().split()
A = [int(i) for i in A]

counter = 0

for i in range(len(A)):
    for j in reversed(range(i+1, len(A))):
        if A[j] < A[j-1]:
            #swap
            A[j], A[j-1] = A[j-1], A[j]
            counter = counter + 1

print(' '.join([str(i) for i in A]))
print(counter)