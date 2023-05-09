// https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_3_D
#include <iostream>
#include <stack>

using std::cin;
using std::cout;

int main() {
    std::stack<int> S1;
    std::stack<std::pair<int, int> > S2;
    constexpr char endl = '\n';

    char ch;
    int S = 0;

    for (int i = 0; cin >> ch; i++) {
        if (ch == '\\') {
            S1.push(i);
        } else if (ch == '/' && !S1.empty()) {
            int start = S1.top();
            S1.pop();

            S += i - start;
            int area = i - start;
            while (!S2.empty() && S2.top().first > start) {
                area += S2.top().second;
                S2.pop();
            }
            S2.push({i, area});
        }
    }

    // first line
    cout << S << endl;

    // second line
    cout << S2.size();

    std::stack<int> result;
    while (!S2.empty()) {
        result.push(S2.top().second);
        S2.pop();
    }

    while (!result.empty()) {
        cout << " ";
        cout << result.top();

        result.pop();
    }

    cout << endl;

    return 0;
}
