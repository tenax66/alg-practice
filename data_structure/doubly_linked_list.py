# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_3_C

class Node:
    def __init__(self, key, prev, next):
        self.key = key
        self.prev = prev
        self.next = next


class DoublyLinkedList:
    def __init__(self):
        self.sentinel = Node(None, None, None)
        self.sentinel.prev = self.sentinel
        self.sentinel.next = self.sentinel

    def insert(self, key):
        node = Node(key, self.sentinel, self.sentinel.next)
        self.sentinel.next.prev = node
        self.sentinel.next = node

    def delete(self, key):
        node = self.sentinel.next

        while node is not self.sentinel:
            if node.key == key:
                node.prev.next = node.next
                node.next.prev = node.prev
                break
            node = node.next

    def deleteFirst(self):
        self.sentinel.next = self.sentinel.next.next
        self.sentinel.next.prev = self.sentinel

    def deleteLast(self):
        node = self.sentinel.prev

        node.prev.next = self.sentinel
        self.sentinel.prev = node.prev

    def print(self):
        node = self.sentinel.next

        buffer = []
        while node is not self.sentinel:
            buffer.append(str(node.key))
            node = node.next

        print(*buffer)


if __name__ == "__main__":
    n = int(input())

    commands = []

    for _ in range(n):
        command = input().split()
        if len(command) == 2:
            commands.append((command[0], int(command[1])))
        if len(command) == 1:
            commands.append((command[0], None))

    dll = DoublyLinkedList()

    for c in commands:
        if c[0] == 'insert':
            dll.insert(c[1])
        elif c[0] == 'delete':
            dll.delete(c[1])
        elif c[0] == 'deleteFirst':
            dll.deleteFirst()
        elif c[0] == 'deleteLast':
            dll.deleteLast()

    dll.print()
