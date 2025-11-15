#include <iostream>
#include <windows.h>
#include <conio.h>
#define null -32
using namespace std;

struct employee {
    int id;
    char name[50];
    int age;
};

void gotoxy(int column, int line) {
    COORD coord;
    coord.X = column;
    coord.Y = line;
    SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE), coord);
}

void textattr(int i) {
    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE), i);
}

int main() {
    int flag=0;
    int number;
    cout<<"Enter The Number Of Employees\n";
    cin>>number;
    employee* ptr=new employee[10];
    int count = 0;
    char menu[3][8] = {"new", "display", "exit"};
    int hintx = 0;
    char ch;

    do {
        system("cls");
        for (int i = 0; i < 3; i++) {
            gotoxy(10, 7 + i);
            if (i == hintx)
                textattr(0x04);
            else
                textattr(0x07);
            cout << menu[i];
        }

        ch = getch();
        if (ch == -32 || ch == 0) {
            ch = getch();
            switch (ch) {
                case 72:
                    hintx--;
                    if (hintx < 0) hintx = 2;
                    break;
                case 80:
                    hintx++;
                    if (hintx > 2) hintx = 0;
                    break;
            }
        }
        else if (ch == 13 || ch == 32) {
            system("cls");
            switch (hintx) {
                case 0: {
                    if(count<number){
                        cout << "Enter Employee ID: ";
                        cin >> ptr[count].id;

                        cin.ignore();
                        cout << "Enter Employee Name: ";
                        cin.getline(ptr[count].name, 50);

                        cout << "Enter Employee Age: ";
                        cin >> ptr[count].age;

                        count++;
                        cout << "\nEmployee Added Successfully \n";
                    }else{
                        cout<<"Array Of Empolyees is Full\n";
                    }
                    system("pause");
                    break;
                }
                case 1: {
                    if (count == 0) {
                        cout << "No Employees Added Yet.\n";
                    } else {
                        cout << "---------- Employees ----------\n";
                        for (int i = 0; i < count; i++) {
                            cout << "Employee " << (i + 1) << ":\n";
                            cout << "ID = " << (ptr+i)->id << "\t";//ptr[i].id
                            cout << "Name = " <<(ptr+i)->name  << "\t";
                            cout << "Age = " << (ptr+i)->age << "\n\n";
                        }
                    }
                    system("pause");
                    break;
                }
                case 2:
                    flag=1;
                    textattr(0x07);
                    cout << "Exiting Program...\n";
                    delete[]ptr;
                    break;
            }
        }

    } while (flag!= 1);
}
