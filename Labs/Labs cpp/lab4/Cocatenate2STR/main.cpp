#include <iostream>
#include <cstring>
using namespace std;

int main()
{
    char fname[50];
    char lname[50];
    cout << "Enter your First Name: ";
    cin >> fname;
    cout << "Enter your Last Name: ";
    cin >> lname;

    strcat(fname, " ");
    strcat(fname, lname);

    cout << "Full Name: " << fname << endl;
}
