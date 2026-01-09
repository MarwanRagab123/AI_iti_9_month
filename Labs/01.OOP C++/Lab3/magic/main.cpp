#include <iostream>
#include <windows.h>
using namespace std;



void gotoxy(int x, int y)
{
    COORD c = { (short)x, (short)y };
    SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE), c);
}

int main()
{
    int n;
    cout << "Enter the order of the magic square ODD Number: ";
    cin >> n;

    if (n % 2 == 0) {
        cout << "Magic square generation without arrays is typically for odd orders." << endl;
        return 1;
    }
    system("cls");
    int current_num = 1;
    int row = 0;
    int col = n / 2;

    for (int i = 1; i <= n * n; ++i) {
        gotoxy(col * 4, row * 2);
        cout << i;

        int next_row = (row - 1 + n) % n;
        int next_col = (col + 1) % n;
        if (i % n == 0) {
            row = (row + 1) % n;
        } else {
            row = next_row;
            col = next_col;
        }
    }

    gotoxy(0, n * 2 + 2);
}
