#include <iostream>

using namespace std;
void swap(int &x,int &b);
int main()
{
    int a;
    int b;

    cout<<"Enter a= ";
    cin>>a;
    cout<<"Enter b= ";
    cin>>b;

    // call by refrence

    swap(a,b);
    cout<<"First Number(a):"<<a<<"\t"<<"Second Number(b):"<<b<<endl;
}

void swap(int &x,int &y){
    int temp=x;
    x=y;
    y=temp;


}

