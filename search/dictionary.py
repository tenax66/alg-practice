# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_4_C

import hashlib


class HashTable:
    SIZE = 1046527

    def __init__(self):
        self.hash_table = ['' for _ in range(HashTable.SIZE)]

    def insert(self, s):
        index = self.calculate(s)
        self.hash_table[index] = s

    def find(self, s):
        index = self.calculate(s)
        result = self.hash_table[index]
        if result:
            return 'yes'
        return 'no'

    def calculate(self, s):
        index = self.hash_to_int(hashlib.sha256(s.encode()))
        while self.hash_table[index] != '':
            if self.hash_table[index] == s:
                return index
            index = self.hash_to_int(hashlib.sha256(index.to_bytes(32, 'little')))
        return index

    def hash_to_int(self, hash):
        return int.from_bytes(hash.digest(), byteorder='little') % HashTable.SIZE


if __name__ == "__main__":
    n = int(input())
    A = []
    for _ in range(n):
        A.append(input().split())

    ht = HashTable()

    for a in A:
        if a[0] == 'insert':
            ht.insert(a[1])
        elif a[0] == 'find':
            print(ht.find(a[1]))
