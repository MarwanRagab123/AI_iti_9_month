#include <iostream>

using namespace std;
void swap(int* x,int* b);
int main()
{
    int a=5;
    int b=8;

    // call by address

    swap(&a,&b);
}

void swap(int* x,int* y){
    int temp=*x;
    *x=*y;
    *y=temp;

    cout<<"First Number(a):"<<*x<<"\t"<<"Second Number(b):"<<*y<<endl;
}

