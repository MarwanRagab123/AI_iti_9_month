#include <iostream>
#include <cstring>
using namespace std;



class Employee {
    int id;
    char name[50];
    int age;
    int salary;

public:
    Employee(int _id,char* _name){
        id=_id;
        strcpy(name,_name);
    }

        Employee(int _id,char* _name,int _age){
        id=_id;
        strcpy(name,_name);
        age=_age;
    }

        Employee(int _id,char* _name,int _age,int _salary){
        id=_id;
        strcpy(name,_name);
        age=_age;
        salary=_salary;
    }

    void setId(int _id) {
        if (_id <= 0) {
            cout << "Invalid ID! Please enter a positive number.\n";
        } else {
            id = _id;
        }
    }

    void setName(char* _name) {
         if (strlen(_name) > 50) {
            cout << "Max 50 characters allowed.\n";
        } else {
            strcpy(name, _name);
        }
    }

    void setAge(int _age) {
        if (_age < 18 || _age > 65) {
            cout << "Invalid age! Must be between 18 and 65.\n";
        } else {
            age = _age;
        }
    }

    void setSalary(int _salary) {
        if (_salary < 0) {
            cout << "Salary cannot be negative!\n";
        } else {
            salary = _salary;
        }
    }

    int getId() {
        return id;
    }

    char* getName() {
        return name;
    }

    int getAge() {
        return age;
    }

    int getSalary() {
        return salary;
    }
    //memberShip function
    void printf() {
        cout << "Employee Info:\n";
        cout << "ID: " << id << endl;
        cout << "Name: " << name << endl;
        cout << "Age: " << age << endl;
        cout << "Salary: " << salary << endl;
    }
};

void print(Employee e);

int main()
{
    //two arg
    Employee e1(2157,"marwan");
    e1.printf();

    cout<<"------------------------------------\n";

    //three arg
    Employee e2(2157,"marwan",20);
    e2.printf();

    cout<<"------------------------------------\n";

    //four arg
    Employee e3(2157,"marwan",20,5000);
    e3.printf();
    /*
    e1.setId(215179);
    e1.setName("Marwan Ragab");
    e1.setAge(60);
    e1.setSalary(10000);
    //e1.printf();
    print(e1);
    */

}
//standAlone function
void print(Employee e){
    cout << "Employee Info:\n";
    cout << "ID: " << e.getId() << endl;
    cout << "Name: " << e.getName() << endl;
    cout << "Age: " << e.getAge() << endl;
    cout << "Salary: " << e.getSalary() << endl;
}

