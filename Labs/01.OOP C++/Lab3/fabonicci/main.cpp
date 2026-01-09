#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Enter the position: ";
    cin >> n;

    int a = 0, b = 1, next;

    if (n == 0) {
        cout << 0;
        return 0;
    } else if (n == 1) {
        cout << 1;
        return 0;
    }

    for (int i = 2; i <= n; ++i) {
        next = a + b;
        a = b;
        b = next;
    }

    cout << "Fibonacci number at position " << n << " is: " << b;
    return 0;
}
