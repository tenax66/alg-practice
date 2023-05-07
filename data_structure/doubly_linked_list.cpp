// https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_3_C

#include <iostream>
#include <vector>

using std::cin;
using std::cout;

struct Node {
    int key;
    Node *prev;
    Node *next;
};

class DoublyLinkedList {
    Node *sentinel;

public:
    DoublyLinkedList() {
        sentinel = new Node;
        sentinel->prev = sentinel;
        sentinel->next = sentinel;
    }

    void insert(int key) {
        Node *node = new Node;
        node->key = key;

        node->next = sentinel->next;
        sentinel->next->prev = node;

        sentinel->next = node;
        node->prev = sentinel;
    }

    void del(Node *node) {
        if (node == sentinel) {
            return;
        }
        node->prev->next = node->next;
        node->next->prev = node->prev;
        delete node;
    }

    void delByKey(int k) {
        Node *node = sentinel->next;

        while (node != sentinel && node->key != k) {
            node = node->next;
        }

        del(node);
    }

    void delFirst() { del(sentinel->next); }

    void delLast() { del(sentinel->prev); }

    void print() {
        Node *node = sentinel->next;

        bool is_first = true;
        while (true) {
            if (node == sentinel) {
                break;
            }
            if (is_first == false) {
                cout << " ";
            }
            cout << node->key;
            node = node->next;
            is_first = false;
        }
        cout << std::endl;
    }
};

int main() {
    DoublyLinkedList dll;

    cin.tie(nullptr);
    std::ios_base::sync_with_stdio(false);

    int n;
    cin >> n;

    std::string command;
    int key;
    for (int i = 0; i < n; i++) {
        cin >> command;

        if (command == "insert") {
            cin >> key;
            dll.insert(key);
        } else if (command == "delete") {
            cin >> key;
            dll.delByKey(key);
        } else if (command == "deleteFirst") {
            dll.delFirst();
        } else {
            dll.delLast();
        }
    }

    dll.print();
    return 0;
}