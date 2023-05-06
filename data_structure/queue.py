# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_3_B

from collections import deque

N, Q = map(int, input().split())
processes = []

for i in range(N):
    name, time = input().split()
    processes.append((name, int(time)))

elapsed_time = 0

queue = deque()

for p in processes:
    queue.append(p)

while queue:
    p = queue.popleft()
    name, time = p

    if time <= Q:
        elapsed_time += time
        print(name, elapsed_time)
    else:
        elapsed_time += Q
        queue.append((name, time - Q))
