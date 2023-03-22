# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_2_B

# SelectionSort(A)
# for i = 0 to A.length-1
#     mini = i
#     for j = i to A.length-1
#         if A[j] < A[mini]
#             mini = j
#     swap A[i] and A[mini]

N = int(input())

A = input().split()
A = [int(i) for i in A]

counter = 0
for i in range(len(A)):
    mini = i
    for j in range(i, len(A)):
        if A[j] < A[mini]:
            mini = j
    if (A[i] != A[mini]):
        A[i], A[mini] = A[mini], A[i]
        counter += 1

print(' '.join([str(i) for i in A]))
print(counter)
