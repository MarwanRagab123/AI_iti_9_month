#include <iostream>
using namespace std;

int main()
{
    int* ptr = new int[5];

    if (ptr != nullptr)
    {
        for (int i = 0; i < 5; i++) {
            cout << "Enter the value for element " << (i + 1) << ": ";
            cin >> ptr[i];
        }

        cout << "\nValues and their addresses in memory:\n";
        for (int i = 0; i < 5; i++) {
            cout << "Element " << (i + 1)
                 << " -> Value: " << ptr[i]
                 << ", Address: " << (ptr + i) << endl;
        }

        delete[] ptr;

        cout << "\nMemory deleted successfully!" << endl;
    }
    else {
        cout << "Memory allocation failed!" << endl;
    }

    return 0;
}
