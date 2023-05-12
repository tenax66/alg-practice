# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_4_A

n = int(input())
S = list(map(int, input().split()))

q = int(input())
T = list(map(int, input().split()))

result = 0

for t in T:
    if t in S:
        result += 1
        continue

print(result)
