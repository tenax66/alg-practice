import math
N, D = map(int, (input().split()))
P = []

INFECTED = {0}
ANS = ['No' for _ in range(N)]

for _ in range(N):
    x, y = map(int, input().split())
    P.append((x, y))

while INFECTED:
    i = INFECTED.pop()
    ANS[i] = 'Yes'

    for j in range(N):
        if ANS[j] == 'Yes':
            continue
        dist = math.sqrt((P[i][0] - P[j][0])**2 + (P[i][1] - P[j][1])**2)
        if dist <= D:
            INFECTED.add(j)

for a in ANS:
    print(a)
