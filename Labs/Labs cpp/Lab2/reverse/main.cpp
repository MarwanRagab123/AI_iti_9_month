#include <iostream>
using namespace std;

int main() {
    int num;
    cout << "Enter Number: \n";
    cin >> num;

    int rev = 0;
    while (num != 0) {
        int digit = num % 10;  //1246 => 6   =>4
        rev = rev * 10 + digit;   // 60 + 4 =64
        num = num / 10; //124
    }

    cout << "Reversed: " << rev << endl;
    return 0;
}
