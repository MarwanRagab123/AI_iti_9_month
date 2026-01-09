#include <iostream>
#include<cstring>

using namespace std;
class BankAccount{
    int id;
    char name[50];
    int balance;
public:
    void setId(int _id){
        if(_id < 0){
            cout << "Enter a valid ID!\n";
        } else {
            id = _id;
        }
    }

    void setName(const char* _name){
        if(_name != nullptr)
            strcpy(name, _name);
    }

    void setBalance(double _balance){
        if(_balance < 0){
            cout << "Balance cannot be negative!\n";
        } else {
            balance = _balance;
        }
    }

    void printf() {
        cout << "Account Info:\n";
        cout << "ID: " << id << endl;
        cout << "Name: " << name << endl;
        cout << "Balance: " << balance << endl;
    }

    void withdraw(int amount){
        if(amount > balance){
            cout << "Insufficient balance!\n";

        } else {
            balance -= amount;
            cout << "Withdrawn from your account: " << amount << endl;
            cout << "New Balance: " << balance << endl;
        }
    }

    void deposit(int amount){
        if(amount < 0){
            cout << "Incorrect amount, try again!\n";
        } else {
            balance += amount;
            cout << "Deposited to your account: " << amount << endl;
            cout << "New Balance: " << balance << endl;
        }
    }

};

int main()
{

    BankAccount b1;
    b1.setId(215179);
    b1.setName("marwan ragab");
    b1.setBalance(2000);
    cout<<"------------------main info-----------------------\n";
    b1.printf();
    cout<<"------------------withdraw-----------------------\n";
    b1.withdraw(1000);
    cout<<"------------------main info-----------------------\n";
    b1.printf();
    cout<<"------------------deposit-----------------------\n";
    b1.deposit(5000);
    cout<<"------------------main info-----------------------\n";
    b1.printf();
}
