#include <iostream>
using namespace std;

int main()
{
    int degree;
    cout << "Enter your degree: ";
    cin >> degree;

    if (degree >= 90) {
        cout << "Excellent";
    }
    else if (degree >= 80) {
        cout << "Very Good";
    }
    else if (degree >= 70) {
        cout << "Good";
    }
    else if (degree >= 60) {
        cout << "Pass";
    }
    else {
        cout << "Fail";
    }

    return 0;
}
