#include <iostream>
#include <string>
using namespace std;

int main() {
    int n;
    cout << "How many names? ";
    cin >> n;
    size_t total = 0;
    for (int i = 0; i < n; i++) {
        cout << "Enter name #" << (i + 1) << ": ";
        string name;
        cin>>name;
        total += name.length();
    }

    cout << "Total characters = " << total << endl;
    return 0;
}
