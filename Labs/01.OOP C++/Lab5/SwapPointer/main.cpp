#include <iostream>

using namespace std;
void swap(int* ptrx,int *ptry);

int main()
{
    int a,b;
    cout<<"Enter Two Number To Need Swap : \n";
    cout<<"Enter the first Number: ";
    cin>>a;
    cout<<"Enter the second Number: ";
    cin>>b;
    swap(&a,&b); //call by address


}

void swap(int* ptrx,int *ptry){

    int temp= *ptrx;
    *ptrx=*ptry;
    *ptry=temp;
    cout<<"First Number :"<<*ptrx<<" : "<<"second Number :"<<*ptry<<endl;
}
