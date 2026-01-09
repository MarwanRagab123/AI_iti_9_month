#include <iostream>
using namespace std;

int factorial(int num);

int main() {
    int n;
    cout << "Enter a number to compute its factorial: ";
    cin >> n;

    if (cin.fail()) {
        cout << "Invalid input! Please enter a number." << endl;
        return 1;
    }

    if (n < 0) {
        cout << "Please enter a positive number." << endl;
    }
    else {
        cout << "Factorial of " << n << " = " << factorial(n) << endl;
    }

    return 0;
}

int factorial(int num) {
    int fact = 1;
    for (int i = num; i > 0; i--) {
        fact *= i;
    }
    return fact;
}
