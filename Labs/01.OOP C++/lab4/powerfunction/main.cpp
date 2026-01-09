#include <iostream>


using namespace std;
int power(int num,int pow);

int main()
{
    int num;
    int pow;
    cout<<"Enter Number :";
    cin>>num;
    cout<<"Enter Power :";
    cin>>pow;
    cout<<"result= "<<power(num,pow);


}

int power(int num,int pow){
    int total=num;
    for(int i=1;i<pow;i++){
       total=total*num;
    }
    return total;
}

