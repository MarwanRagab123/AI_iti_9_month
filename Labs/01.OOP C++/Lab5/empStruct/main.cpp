#include <iostream>

using namespace std;

struct empolyee{
    int id;
    char name[20];
    int age;
};

int main()
{
    empolyee emp[3];
    for(int i=0;i<3;i++){
        cout<<"Enter Employee "<<(i+1)<<" :"<<endl;
        cout<<"Enter ID: ";
        cin>>emp[i].id;
        cout<<"Enter Name: ";
        cin>>emp[i].name;
        cout<<"Enter Age: ";
        cin>>emp[i].age;

    }

    for(int i=0;i<3;i++){
        cout<<"Empolyee "<<(i+1)<<" :"<<endl;
        cout<<"ID= "<<emp[i].id<<"\t";
        cout<<"Name= "<<emp[i].name<<"\t";
        cout<<"Age= "<<emp[i].age<<endl;
    }

}
