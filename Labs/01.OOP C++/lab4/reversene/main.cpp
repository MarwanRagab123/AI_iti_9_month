#include <iostream>

using namespace std;
int revers(int num);
int main()
{
    int num;
    cout<<"Enter Number to Need To reverse :";
    cin>>num;
    cout<<"Reverse Number= "<<revers(num);
}

int revers(int num){
    int re=0;
    while(num!=0){
        int k=num%10;
        re=re*10+k;//5
        num=num/10;


    }
    return re;
}
