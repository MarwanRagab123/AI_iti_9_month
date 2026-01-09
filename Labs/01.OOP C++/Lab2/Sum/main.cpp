#include <iostream>

using namespace std;

int main()
{
    int sum=0;
    for(int i=0 ;i<5;i++){
        int num;
        cout<<"please Enter Number "<<(i+1)<<":";
        cin>>num;
        sum+=num;
    }

    cout<<sum;





}
