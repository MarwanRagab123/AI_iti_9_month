#include <iostream>
#define size 10
using namespace std;

int main() {
    int arr[size];

    cout << "Enter " << size << " numbers:\n";
    for (int i = 0; i < size; i++) {
        cin >> arr[i];
    }

    for (int i = 0; i < size - 1; i++) {
        bool swapped = false;

        for (int j = 0; j < size - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
                swapped = true;
            }
        }

        if (!swapped) {
            break;
        }
    }

    cout << "\nSorted array:\n";
    for (int i = 0; i < size; i++) {
        cout << arr[i] << "\t";
    }

    return 0;
}
