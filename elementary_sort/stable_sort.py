# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_2_C

# BubbleSort(C, N)
#   for i = 0 to N-1
#     for j = N-1 downto i+1
#       if C[j].value < C[j-1].value
#         C[j] と C[j-1] を交換
#
# SelectionSort(C, N)
#   for i = 0 to N-1
#     minj = i
#    for j = i to N-1
#      if C[j].value < C[minj].value
#        minj = j
#    C[i] と C[minj] を交換

import copy


class Card():
    def __init__(self, suit: str, value: int) -> None:
        self.suit = suit
        self.value = value

    def __str__(self) -> str:
        return self.suit + str(self.value)


def bubble_sort(C, N):
    for i in range(N):
        for j in reversed(range(i+1, N)):
            if C[j].value < C[j-1].value:
                C[j], C[j-1] = C[j-1], C[j]


def selection_sort(C, N):
    for i in range(N):
        minj = i
        for j in range(i, N):
            if C[j].value < C[minj].value:
                minj = j
        C[i], C[minj] = C[minj], C[i]


if __name__ == '__main__':
    N = int(input())

    input = [list(i) for i in input().split()]
    C1 = [Card(c[0], int(c[1])) for c in input]

    C2 = copy.deepcopy(C1)

    bubble_sort(C1, N)
    selection_sort(C2, N)

    C1_str = [str(c) for c in C1]
    C2_str = [str(c) for c in C2]

    print(' '.join(C1_str))
    # bubble sort is stable
    print('Stable')
    print(' '.join(C2_str))

    # compare with the result of bubble sort
    if C1_str == C2_str:
        print('Stable')
    else:
        print('Not stable')
