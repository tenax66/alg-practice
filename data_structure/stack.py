# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_3_A

S = []

def push_s(i):
    S.append(i)


def pop_s() -> int:
    return S.pop()


if __name__ == "__main__":
    F = input().split()

    for f in F:
        if f == '+':
            push_s(pop_s() + pop_s())
        elif f == '-':
            second = pop_s()
            first = pop_s()
            push_s(first - second)
        elif f == '*':
            push_s(pop_s() * pop_s())
        else:
            push_s(int(f))

    print(pop_s())
