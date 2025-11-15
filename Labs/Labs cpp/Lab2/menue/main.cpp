#include <iostream>
using namespace std;

int main() {
    int flag = 1;
    do {
        cout << "Menu:\nd) delete\nn) new\ne) exit\n";


        cout << "Enter choice: ";
        char ch;
        cin >> ch;

        switch (ch) {
            case 'd':
            case 'D':
                cout << "delete\n";
                break;
            case 'n':
            case 'N':
                cout << "New\n";
                break;
            case 'e':
            case 'E':
                cout << "Exit\n";
                flag = 0;
                break;
            default:
                cout << "Invalid choice\n";
                break;
        }
    } while (flag == 1);

    return 0;
}
