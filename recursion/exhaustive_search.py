A = []


def solve(i, m):
    if i == len(A) and m != 0:
        return False
    if m == 0:
        return True

    return solve(i+1, m) or solve(i+1, m - A[i])


if __name__ == "__main__":
    n = int(input())
    A = list(map(int, input().split()))

    q = int(input())
    M = list(map(int, input().split()))

    for m in M:
        if solve(0, m):
            print('yes')
        else:
            print('no')
