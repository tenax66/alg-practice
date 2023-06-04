import math


class UnionFind():
    def __init__(self, n) -> None:
        self.data = [-1] * n

    def is_root(self, i) -> bool:
        return self.data[i] < 0

    def find_root(self, i) -> int:
        if self.is_root(i):
            return i
        else:
            self.data[i] = self.find_root(self.data[i])
            return self.data[i]

    def tree_size(self, i) -> int:
        return - self.data[self.find_root(i)]

    def unite_trees(self, i, j) -> int:
        i = self.find_root(i)
        j = self.find_root(j)

        if i != j:
            if self.tree_size(i) < self.tree_size(j):
                i, j = j, i
            self.data[i] += self.data[j]
            self.data[j] = i

        return i

    def is_same(self, i, j) -> bool:
        return self.find_root(i) == self.find_root(j)


if __name__ == '__main__':
    N, D = map(int, (input().split()))
    P = []

    for _ in range(N):
        x, y = map(int, input().split())
        P.append((x, y))

    uf = UnionFind(N)

    for i in range(N):
        for j in range(N):
            dist = math.sqrt((P[i][0] - P[j][0])**2 + (P[i][1] - P[j][1])**2)
            if dist <= D:
                uf.unite_trees(i, j)

    for i in range(N):
        if uf.is_same(0, i):
            print('Yes')
        else:
            print('No')
