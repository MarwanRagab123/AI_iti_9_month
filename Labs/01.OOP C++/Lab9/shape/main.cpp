#include <iostream>
#include <cstring>
using namespace std;

class Person{
protected:
    int id;
    char name[50];
    int age;
public:
    Person(){id=0;strcpy(name,"undified");age=0;}
    Person(int _id){id=_id;}
    Person(int _id,char* _name){id=_id;strcpy(name,_name);}
    Person(int _id,char* _name,int _age){id=_id;strcpy(name,_name);age=_age;}

    void setid(int _id){
        id=_id;
    }
    void setname(char* _name){
        strcpy(name,_name);
    }

    void setage(int _age){
        age=_age;
    }

    int getid(){return id;}
    char* getname(){return name;}

    void print(){
        cout << "ID: " << id << ", Name: " << name << ", Age: " << age;
    }
};

class Employee:public Person{
    float salary;
public:
    Employee(int _id,char* _name,int _age,float _salary):Person(_id,_name, _age){
        salary=_salary;
    }

    void setsalary(float _salary){
        salary=_salary;
    }
    float getsalary(){
        return salary;
    }

    void print(){
        Person::print();
        cout<<", salary: "<<salary<<endl;
    }
};

class Student:public Person{
    int grade;
public:
    Student(int _id,char* _name,int _age,int _grade):Person(_id,_name, _age){
        grade=_grade;
    }

    void setgrade(int _grade){
        grade=_grade;
    }

    int getgrade(){
        return grade;
    }

    void print(){
        Person::print();
        cout<<", Grade:"<<grade<<endl;
    }

};


int main() {
    // Use case 1:
    Employee e(101, "Marwan", 22, 7500.5);
    e.print();

    //  Use case 2:
    Student s(202, "Omar", 20, 92.3);
    s.print();

    //  Use case 3:
    e.setsalary(8000);
    e.setname("Marwan Ragab");
    cout << "\nAfter update:\n";
    e.print();

    return 0;
}


